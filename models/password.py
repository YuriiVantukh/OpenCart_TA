"""
Contains Password class that provides help with
interacting with the Password page.
"""


# pylint: disable=too-few-public-methods
class Password:
    """
    Use to edit user's password
    on the Password page.
    """

    def __init__(self,
                 password=None,
                 salt=None):
        self.password = password
        self.salt = salt

    def __repr__(self):
        return "{} {}".format(self.password, self.salt)

    def __eq__(self, other):
        return self.password == other.password
