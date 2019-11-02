"""
Contains PersonalDetails class that provides help with
interacting with the Edit Account page.
"""


# pylint: disable=too-few-public-methods
class PersonalDetails:
    """
    Use to edit user's personal info
    on the Edit Account page.
    """

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 email=None,
                 telephone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telephone = telephone

    def __repr__(self):
        return "{} {} {} {}".format(self.first_name,
                                    self.last_name,
                                    self.email,
                                    self.telephone)

    def __eq__(self, other):
        return self.first_name == other.first_name \
               and self.last_name == other.last_name \
               and self.email == other.email \
               and self.telephone == other.telephone
