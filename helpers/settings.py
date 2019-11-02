"""
Module contains settings.
"""
import logging

import os

BASE_HOST = "http://localhost/opencart"
BASE_USER_EMAIL = "taqc296@gmail.com"
BASE_USER_PASSWORD = "root"
BASE_CONNECTION = "mysql://root@localhost/opencart"

TEST_DATA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "data"))
TEST_DATA = {
    "addressbook_valid": os.path.join(TEST_DATA_PATH, "user", "addressbook_valid.json"),
    "addressbook_invalid": os.path.join(TEST_DATA_PATH, "user", "addressbook_invalid.json"),
    "personalinfo_valid": os.path.join(TEST_DATA_PATH, "user", "personalinfo_valid.json"),
    "personalinfo_invalid": os.path.join(TEST_DATA_PATH, "user", "personalinfo_invalid.json")
}

PRESET_BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "dbpresets"))
DB_PRESET = {
    "user_base": os.path.join(PRESET_BASE_PATH, "user", "base.sql"),
    "guest_base": os.path.join(PRESET_BASE_PATH, "guest", "base.sql")
}

logging.basicConfig(filename="sample.log",
                    filemode='w',
                    format=('# %(levelname)-8s [%(asctime)s] '
                            '%(filename)-20s [LINE:%(lineno)s]   %(message)s'),
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
try:
    from .local_settings import *
except ImportError:
    pass
