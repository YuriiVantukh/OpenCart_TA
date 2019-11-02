"""
Contains the Zone class for interacting with the database.
"""
from sqlalchemy import Column, String, Integer
from .base import BASE


# pylint: disable=too-few-public-methods
class Zone(BASE):
    """
    Representing the oc_zone table from the opencart database.
    """
    __tablename__ = 'oc_zone'

    zone_id = Column(Integer, primary_key=True)
    name = Column(String)

    # pylint: disable=duplicate-code
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'
