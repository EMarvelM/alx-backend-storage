#!/usr/bin/env python3
""" inserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a specified MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object where the document will be inserted.
        **kwargs: Arbitrary keyword arguments representing the fields and values of the document to be inserted.

    Returns:
        The ID of the inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id 
