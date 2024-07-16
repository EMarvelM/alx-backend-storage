#!/usr/bin/env python3
""" function that changes all topics of a school document based on the name
"""
from pymongo import MongoClient
from typing import List

def update_topics(mongo_collection: MongoClient, name: str, topics: List[str]):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The school name to update.
        topics (List[str]): The list of topics to set.
    """
    mongo_collection.update_one({"name": name}, {$set: {"topics": topics}})
