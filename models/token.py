__author__ = 'alexandreferreira'


class Token:
    def __init__(self):
        self.token = None
        self.usuario = None
        self.created = None
        self.expired = False

    def generate_token(self, usuario):
        pass

    def expired_token(self):
        self.expired = True

    def validate_token(self):
        pass
