#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    connection = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = connection.logs.nginx
    logs = nginx_collection.find({})
    print("{} logs\nMethods:".format(nginx_collection.count_documents({})))

    methods = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    get_satus = 0

    for log in logs:
        if log["method"] in methods:
            if log["method"] == 'GET' and log['path'] == '/status':
                get_satus += 1
            methods[log["method"]] += 1

    for method in methods:
        print('\tmethod {}: {:d}'.format(method, methods[method]))

    print('{} status check'.format(get_satus))
