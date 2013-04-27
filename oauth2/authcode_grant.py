#coding=utf8
"""RFC6749, 4.1 Authorization Code Grant.
Using flask as server-side Framework.
"""


try:
    import simplejson as json
except:
    import json


from flask import request

from . import utils

@utils.app.route('/authorize', methods=['POST'])
def auth_request():
    """Check RFC6749 4.1.1 for more information.
    
    :param response_type string: Value MUST be "code".
    :param client_id string: client id.
    :param redirect_uri string: 
    :param scope string:
    :parame state string:

    Customlize template:
    """


def auth_response():
    pass
    
