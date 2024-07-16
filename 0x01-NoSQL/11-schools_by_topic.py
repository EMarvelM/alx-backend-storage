#!/usr/bin/env python3
""" function that returns the list of school having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for in the topics list.

    Returns:
        List[dict]: A list of dictionaries representing the schools that have the specified topic.
    """
    return list(mongo_collection.find({'topics': topic}))
