"""
Contains DbAddress class for interacting
with a table oc_address from opencart database.
"""
import logging
from db.country import Country
from db.zone import Zone
from db.address import Address
from db.base import session_factory
from models.addressbook import AddressBook


# pylint: disable=too-few-public-methods
class DbAddress:
    """
    Contains methods for obtaining information from oc_address table.
    """

    @staticmethod
    def get_address_by_id(user: AddressBook) -> AddressBook:
        """
        Receives address_id data from the AddressBook object,
        on their basis searches for records in the oc_address table
        and returns them as an AddressBook object.

        :param user: object AddressBook with address_id.
        :return: object AddressBook with data from oc_address table.
        """
        session = session_factory()
        logging.info("Query address entry from oc_address table.")
        query = session.query(Address)
        address = query.filter(Address.address_id == user.address_id).first()
        zone = session.query(Zone.name).filter(Zone.zone_id == address.zone_id).first()
        country = session.query(
            Country.name).filter(Country.country_id == address.country_id).first()
        session.close()
        return AddressBook(address_id=address.address_id,
                           first_name=address.firstname,
                           last_name=address.lastname,
                           company=address.company,
                           address_1=address.address_1,
                           address_2=address.address_2,
                           city=address.city,
                           country=country[0],
                           region_state=zone[0])

    @staticmethod
    def get_id_list_from_db():
        """
        Get id's from db.

        :return: list with id's.
        """
        session = session_factory()
        query = session.query(Address.address_id).all()
        session.close()
        id_data = []
        for data in query:
            id_data.append(data[0])
        return sorted(id_data)
