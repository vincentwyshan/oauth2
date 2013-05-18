#coding=utf8
"""RFC6749 - client.
"""




class Client(object):
    
    @property
    def client_id(self):
        "client_id in rfc6749"
        pass

    @property
    def client_secret(self):
        "client_secret in rfc6749"
        pass


class User(object):
    """User interface.
    """
    id = None
    name = None
    url = None

    def __init__(self):
        pass
