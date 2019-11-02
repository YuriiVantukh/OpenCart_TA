"""
Contains methods for creating, deleting and updating database.
"""

import logging
from sqlalchemy.engine import reflection
from sqlalchemy import create_engine, text
from sqlalchemy.schema import (
    MetaData,
    Table,
    DropTable,
    ForeignKeyConstraint,
    DropConstraint)
from helpers.settings import BASE_CONNECTION


def drop_all_db_tables():
    """
    Drop current database.
    """
    engine = create_engine(BASE_CONNECTION)

    conn = engine.connect()

    # the transaction only applies if the DB supports
    # transactional DDL, i.e. PostgreSQL, MS SQL Server
    trans = conn.begin()

    inspector = reflection.Inspector.from_engine(engine)

    # gather all data first before dropping anything.
    # some DBs lock after things have been dropped in
    # a transaction.

    metadata = MetaData()

    tbs = []
    all_fks = []

    for table_name in inspector.get_table_names():
        fks = []
        for foreign_key in inspector.get_foreign_keys(table_name):
            if not foreign_key['name']:
                continue
            fks.append(
                ForeignKeyConstraint((), (), name=foreign_key['name'])
            )
        table = Table(table_name, metadata, *fks)
        tbs.append(table)
        all_fks.extend(fks)

    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))

    for table in tbs:
        conn.execute(DropTable(table))

    trans.commit()


def create_all_db_tables(database):
    """
    Create db tables from selected file.

    :param database: sql file with db tables.
    """
    drop_all_db_tables()

    # Open the .sql file
    sql_file = open(r'{}'.format(database), 'r')

    # Create an empty command string
    sql_command = ''

    engine = create_engine(BASE_CONNECTION)

    conn = engine.connect()

    # the transaction only applies if the DB supports
    # transactional DDL, i.e. PostgreSQL, MS SQL Server
    trans = conn.begin()

    # Iterate over all lines in the sql file
    for line in sql_file:
        # Ignore commented lines
        if not line.startswith('--') and line.strip('\n'):
            # Append line to the command string
            sql_command += line.strip('\n')
            # If the command string ends with ';', it is a full statement
            if sql_command.endswith(';'):
                # Try to execute statement and commit it
                try:
                    conn.execute(text(sql_command))

                # Assert in case of error
                # pylint: disable=broad-except
                except Exception as err:
                    logging.error(f"{sql_command} {err}")

                # Finally, clear command string
                finally:
                    sql_command = ''
    trans.commit()
