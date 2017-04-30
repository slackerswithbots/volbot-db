#!/usr/bin/python

# Copyright (c) 2017 ObjectLabs Corporation
# Distributed under the MIT license - http://opensource.org/licenses/MIT

__author__ = 'mLab'

# Written with pymongo-3.4
# Documentation: http://docs.mongodb.org/ecosystem/drivers/python/
# A python script connecting to a MongoDB given a MongoDB Connection URI.

import sys
import json
import pymongo




### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://heroku_21hlwbt1:tr9tqb8do6pfins93i9sn95b1f@ds123371.mlab.com:23371/heroku_21hlwbt1' 

CLIENT = pymongo.MongoClient(uri)
DB = CLIENT.get_default_database()
###############################################################################
# main
###############################################################################

def insert_many(collection, datafile):
    with open(datafile) as mock_data_file:
        datafile = json.load(mock_data_file)
    collection = DB[collection]
    collection.insert_many(datafile)



def main(args):
    insert_many('events_test', 'MOCK_DATA.json')
    if __name__ == '__main__':
        main(sys.argv[1:])
