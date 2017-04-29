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

with open('MOCK_DATA.json') as mock_data_file:
    MOCK_DATA = json.load(mock_data_file)



### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://heroku_21hlwbt1:tr9tqb8do6pfins93i9sn95b1f@ds123371.mlab.com:23371/heroku_21hlwbt1' 

###############################################################################
# main
###############################################################################

def main(args):

    client = pymongo.MongoClient(uri)

    db = client.get_default_database()
    events = db['events']
    events.insert_many(MOCK_DATA)

    # Then we need to give Boyz II Men credit for their contribution to
    # the hit "One Sweet Day".

    #query = {'song': 'One Sweet Day'}

    #songs.update(query, {'$set': {'artist': 'Mariah Carey ft. Boyz II Men'}})

    # Finally we run a query which returns all the hits that spent 10 or
    # more weeks at number 1.

    #cursor = songs.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)

    #for doc in cursor:
    #     print ('In the %s, %s by %s topped the charts for %d straight weeks.' %
    #           (doc['decade'], doc['song'], doc['artist'], doc['weeksAtOne']))
    
    ### Since this is an example, we'll clean up after ourselves.

    #db.drop_collection('events')

    ### Only close the connection when your app is terminating

    #client.close()


if __name__ == '__main__':
    main(sys.argv[1:])