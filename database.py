import os

import pymongo
from dotenv import load_dotenv

load_dotenv('.env')


class Database(object):

    def __init__(self):
        self.__uri = os.getenv('DATABASE_URI')
        self.client = pymongo.MongoClient(self.__uri)
