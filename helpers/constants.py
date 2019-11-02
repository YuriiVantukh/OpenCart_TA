"""
Contains Return class
"""


# pylint: disable=too-few-public-methods
class Returns:
    """
    Contains constants
    """
    TEXT_DANGER_FIRST_NAME = 'First Name must be between 1 and 32 characters!'
    TEXT_DANGER_LAST_NAME = 'Last Name must be between 1 and 32 characters!'
    TEXT_DANGER_EMAIL = 'E-Mail Address does not appear to be valid!'
    TEXT_DANGER_TELEPHONE = 'Telephone must have 14 characters'
    TEXT_DANGER_ORDER_ID = 'Order ID required!'
    TEXT_DANGER_PRODUCT_NAME = 'Product Name must be greater than 3 and less than 255 characters!'
    TEXT_DANGER_PRODUCT_CODE = 'Product Model must be greater than 3 and less than 64 characters!'

    TEXT_DANGER_FIRST_NAME_INVALID = 'First Name must be between 1 and 32 characters!'
    TEXT_DANGER_LAST_NAME_INVALID = 'Last Name must be between 1 and 32 characters!'
    TEXT_DANGER_EMAIL_INVALID = 'E-Mail Address does not appear to be valid!'
    TEXT_DANGER_TELEPHONE_INVALID = 'Telephone must have 14 characters'
    TEXT_DANGER_ORDER_ID_INVALID = 'Order ID required!'
    TEXT_DANGER_ADDRESS1_INVALID = 'Address must be between 3 and 128 characters!'
    TEXT_DANGER_CITY_INVALID = 'City must be between 2 and 128 characters!'
    TEXT_DANGER_POSTCODE_INVALID = 'Postcode must be between 2 and 10 characters!'
    TEXT_DANGER_REGION_STATE_INVALID = 'Please select a region / state!'
    TEXT_DANGER_TELEPHONE_FORM = 'Telephone must be between 3 and 32 characters!'

    TEXT_SUCCESS_ADDRESS_ADDED = 'Your address has been successfully added'
    TEXT_SUCCESS_ADDRESS_UPDATED = 'Your address has been successfully updated'
    TEXT_SUCCESS_ACCOUNT_UPDATED = 'Success: Your account has been successfully updated.'

    DANGER_COLOR = 'rgba(169, 68, 66, 1)'


# pylint: disable=too-few-public-methods
class Outputs:
    """
    Contains displayed on Page messages or text
    """
    TEXT_ALERT_PRODUCT_ADD = 'Success: You have added'
    TEXT_ALERT_TOO_MUCH_PRODUCT = 'Products marked with *** are not available'
    TEXT_ZERO_PRODUCT_QUANTITY = '0 item(s)'

    @staticmethod
    def get_edited_product_quantity(count: int) -> str:
        """
        Contains static method that pass string with edited product quantity.

        :param count: New product quantity in Cart.
        :return: String with new quantity of product in Cart.
        """
        return f'{count} item(s)'

    @staticmethod
    def get_edited_product_price(count: float) -> str:
        """
        Contains static method that pass string with edited product price.

        :param count: New product price in Cart.
        :return: String with new price of product in Cart.
        """
        return f'${count}'
