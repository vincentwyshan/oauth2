#coding=utf8
"""RFC6749, 4.1 Authorization Code Grant.
Using flask as server-side Framework.
"""

import uuid
import urllib

try:
    import simplejson as json
except:
    import json


from flask import request
from flask import render_template
from flask import make_response
from flask import redirect

from . import utils
from oauth2.structure import (
    Client, User, Scope, ClientNotExists
)

from oauth2.storage import (
    set, get, del, exists
)

AUTH_ERROR = (
    (101, 'invalid_request'),
    (102, 'unauthorized_client'),
    (103, 'access_denied'),
    (104, 'unsupported_response_type'),
    (105, 'invalid_scope'),
    (106, 'server_error'),
    (107, 'temporarily_unavailable'),
)
AUTH_ERROR = dict(AUTH_ERROR)


@utils.app.route('/authorize', methods=['POST', 'GET'])
def auth_request():
    """Check RFC6749 4.1.1 for more information.

    :param response_type : Value MUST be "code".
    :param client_id string: client id.
    :param redirect_uri string: 
    :param scope string: list of space-delimited strings, `structure.Scope`
    :param state string:

    Customlize template:
    """

    # validate client
    client_id = request.values.get('client_id')
    scopes = request.values.get('scope')
    redirect_uri = request.values.get('redirect_uri')
    if not auth_request_validate():
        return auth_response_error(client_id, redirect_uri,
                                   request.values.get('state'), AUTH_ERROR[101])
    try:
        Client.valid_codeauth(client_id, scopes)
    except ClientNotExists:
        # if not validate, return a 404 page.
        return auth_response_error(client_id, redirect_uri,
                                   request.values.get('state'), AUTH_ERROR[102])

    # if validate success, return decision.html.
    return render_template("decision.html")

def auth_request_validate():
    if request.values.get('response_type') != 'code':
        return False
    if not request.values.get('redirect_uri') :
        return False
    if not request.values.get('scope'):
        return False
    return True


@utils.app.route('/authorize_decision', methods=['POST', 'GET'])
def auth_response():
    """Check RFC6749 4.1.2 for more information.

    Need all parameters which present in `auth_request`, and another more
    `grant`.
    
    :param grant: [YES/NO]

    If authorization is success, return code, state, redirect user agent to
    client.
    """
    # validate client
    client_id = request.values.get('client_id')
    scopes = request.values.get('scope')
    redirect_uri = request.values.get('redirect_uri')
    state = request.values.get('state')
    grant = request.values.get('grant')
    try:
        Client.valid_codeauth(client_id, scopes)
    except ClientNotExists:
        return auth_response_error(client_id, redirect_uri, state,
                                   AUTH_ERROR[102])

    if grant == 'NO':
        return auth_response_error(client_id, redirect_uri, state,
                                   AUTH_ERROR[103])

    if request.values.get('response_type') != 'code':
        return auth_response_error(client_id, redirect_uri, state,
                                   AUTH_ERROR[104])

    if Scope.validate(scopes) == False:
        return auth_response_error(client_id, redirect_uri, state,
                                   AUTH_ERROR[105])

    # authorization
    if grant == 'YES':
        return auth_response_succed(client_id, redirect_uri, state)
    else:
        return auth_response_error(client_id, redirect_uri, state,
                                   AUTH_ERROR[106])
    # TODO, server_error, temporarily_unavailable

def auth_response_succed(client_id, redirect_uri, state):
    """RFC6749 4.1.2

    Issue code.
    """
    # issue code, code expired in 20 minutes
    code = str(uuid.uuid1())
    auth_info = dict(client_id=client_id, redirect_uri=redirect_uri)
    set(code, auth_info, 60*20)

    url_paras = urllib.urlencode(dict(code=code, state=(state or '')))
    url_full = redirect_uri + '?' + url_paras
    return redirect(url_full)
    

    
def auth_response_error(client_id, redirect_uri, state, error_code):
    """ RFC6749 4.1.2.1

    Return standard error_code, error_description, error_uri, state.
    """
    url_paras = urllib.urlencode(error=error_code, state=state)
    url_full = redirect_uri + '?' + url_paras
    return redirect(url_full)

@utils.app.route('/token', methods=['POST', 'GET'])
def access_token_request():
    """RFC6749 4.1.3

    :param grant_type: fix value: 'authorization_code'.
    :param code: authorization code, obtain from `auth_response_succed`.
    :param redirect_uri: if redirect_uri was present in `auth_request`, it
                         should be same with that.
    :param client_id: client_id
    """
    # 1, client auth by HTTP Basic authorization

def _request_access_token_response():
    """RFC6749 4.1.4
    :param grant_type: MUST be 'authorization_code'.
    :param code: code was issued in `auth_response_succed`.
    :param redirect_uri: if redierct_uri present in `auth_response`, they are
                         match.
    :param client_id: 
    """
    
