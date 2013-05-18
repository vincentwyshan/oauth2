#coding=utf8
"""RFC6749, 4.1 Authorization Code Grant.
Using flask as server-side Framework.
"""


try:
    import simplejson as json
except:
    import json


from flask import request
from flask import render_template

from . import utils

@utils.app.route('/authorize', methods=['POST', 'GET'])
def auth_request():
    """Check RFC6749 4.1.1 for more information.

    :param response_type : Value MUST be "code".
    :param client_id string: client id.
    :param redirect_uri string: 
    :param scope string:
    :param state string:

    Customlize template:
    """
    return render_template("decision.html")


def auth_response_succed():
    """Check RFC6749 4.1.2 for more information.

    If authorization is success, return code, state, redirect user agent to
    client.
    """
    

def auth_response_error():
    """
    """
