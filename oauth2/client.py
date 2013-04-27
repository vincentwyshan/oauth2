#coding=utf8
"""RFC6749 - client.
"""




class Client(object):
    
    @property
    def id(self):
        "client_id in rfc6749"
        pass

    @property
    def secret(self):
        "client_secret in rfc6749"
        pass


class User(object):
    id = None
    name = None
    url = None
