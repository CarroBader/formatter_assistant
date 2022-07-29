# #!/usr/bin/python3

# import os
# import sys
# import logging
# import certifi
# from dotenv import load_dotenv
# from pymongo import MongoClient

# load_dotenv()

# DB_CONNECTION = os.getenv('connection_string')
# DB_STRING = os.getenv('db_string')

# logger = logging.getLogger(__name__)
# db = None
# collection = None
# config = {}


# def _setup_db():
#     # Open connection to the database and choose collection.

#     logger.debug(f'Database name: {DB_STRING}')
#     ca = certifi.where()

#     try:
#         client = MongoClient(DB_CONNECTION, tlsCAFile=ca)
#         logger.info('Connected successfully')
#     except Exception as error:
#         logger.error(error)
#         logger.info('Could not connect to MongoDB')
#         sys.exit(1)

#     db = client.get_database(DB_STRING)
#     return db


# def _set_collection(db_collection):
#     # Set the collection variable to global.

#     logger.info('Set global collection')
#     if db is not None:
#         collection = db[db_collection]
#     return collection


# def _init_config():
#     global config
#     config['db'] = db
#     config['collection'] = collection


# def init(db_collection):
#     global db
#     if db is None:
#         db = _setup_db()
#     global collection
#     if collection is None:
#         collection = _set_collection(db_collection)
#     _init_config()
