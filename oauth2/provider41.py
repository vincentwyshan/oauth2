#coding=utf8
"""RFC6749, 4.1 Authorization Code Grant.
"""


try:
    import simplejson as json
except:
    import json



def auth_request(
