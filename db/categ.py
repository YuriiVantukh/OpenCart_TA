""" Count subcategore in DB"""
from sqlalchemy import create_engine

from helpers.settings import BASE_CONNECTION

ENGINE = create_engine(BASE_CONNECTION)
for row in ENGINE.execute('SELECT COUNT(parent_id) FROM `oc_category` WHERE `parent_id`=20'):
    desctops = dict(row)
    quantity_desktops = (desctops['COUNT(parent_id)'])
for row in ENGINE.execute('SELECT COUNT(parent_id) FROM `oc_category` WHERE `parent_id`=18'):
    laptops = dict(row)
    quantity_laptops = (laptops['COUNT(parent_id)'])
for row in ENGINE.execute('SELECT COUNT(parent_id) FROM `oc_category` WHERE `parent_id`=25'):
    components = dict(row)
    quantity_components = (components['COUNT(parent_id)'])
