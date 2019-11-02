"""
Contains DbCustomer class for interacting
with a table oc_address from opencart database.
"""
import logging
from db.customer import Customer
from db.base import session_factory
from models.personaldetails import PersonalDetails
from models.password import Password


# pylint: disable=too-few-public-methods
class DbCustomer:
    """
    Contains methods for obtaining information from oc_customer table.
    """

    @staticmethod
    def get_from_db_by_email(user: PersonalDetails) -> PersonalDetails:
        """
        Receives email data from the PersonalDetails object,
        on their basis searches for records in the oc_customer table
        and returns them as an PersonalDetails object.

        :param user: object PersonalDetails with user's email.
        :return: object PersonalDetails with data from oc_customer table.
        """
        session = session_factory()
        logging.info("Query customer row from oc_customer table.")
        query = session.query(Customer)
        customer = query.filter(Customer.email == user.email).first()
        session.close()
        return PersonalDetails(first_name=customer.firstname,
                               last_name=customer.lastname,
                               email=customer.email,
                               telephone=customer.telephone)

    @staticmethod
    def get_password_by_email(user: PersonalDetails) -> Password:
        """
        Take email data from PersonalDetails object, on its basis,
        make a request to the database and return the value of the password.

        :param user: PersonalDetails object with email data.
        :return: Password object with password data.
        """
        session = session_factory()
        logging.info("Query customer's password from oc_customer table.")
        query = session.query(Customer.password)
        data = query.filter(Customer.email == user.email).first()
        session.close()
        return Password(password=data.password)

    @staticmethod
    def get_salt_by_email(user: PersonalDetails) -> Password:
        """
        Take email data from PersonalDetails object, on its basis,
        make a request to the database and return the value of the salt.

        :param user: PersonalDetails object with email data.
        :return: Password object with salt data.
        """
        session = session_factory()
        logging.info("Query customer's salt from oc_customer table.")
        query = session.query(Customer.salt)
        data = query.filter(Customer.email == user.email).first()
        session.close()
        return Password(salt=data.salt)
