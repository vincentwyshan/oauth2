#coding=utf8
"""Define objects were used in oauth2.
"""


class ClientNotExists(BaseException):
    pass

class UserNotExists(BaseException):
    pass


class User:
    """Resource owner descriped in RFC6749.
    """

    id = None
    email = None
    phonenumber = None
    name = None

ResourceOwner = User



class Client:
    """
    """

    id = None

    # client_type: [confidential, public]
    client_type = None

    # client specified its identifier, unique string.
    # exactly like a unique `username`.
    client_identifier = None
    
    client_password = None


    redirect_uri = None

    app_name = None
    website = None
    description = None
    logo_uri = None

    @classmethod
    def exists(cls, client_id):
        return True

    @classmethod
    def valid_codeauth(cls, client_id, scope):
        if not cls.exists(client_id):
            raise ClientNotExists


class Scope:
    BASIC = 'BASIC'
    values = ('BASIC', )
    
    @classmethod
    def description(cls, scopes, lang='CN'):
        """
        :param scopes: space-delimited scopes.
        :param lang: [ CN, EN ]
        :rtype: pairs of (scope, description).
        """

    def validate(cls, scopes):
        """
        :param scopes: space-delimited scopes.
        """
        for scope in scopes.split(' '):
            if scope not in cls.values:
                return False
        return True



class AuthGrants:
    pass


