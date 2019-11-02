"""
Contains the Country class for interacting with the database.
"""
from sqlalchemy import Column, String, Integer
from .base import BASE


# pylint: disable=too-few-public-methods
class Country(BASE):
    """
    Representing the oc_country table from the opencart database.
    """
    __tablename__ = 'oc_country'

    country_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'
