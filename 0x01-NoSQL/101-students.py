#!/usr/bin/env python3
"""
Module to calculate the average scores of students stored in MongoDB collection
"""


def top_students(mongo_collection):
    """
    Calculate the average score for each student in the mongo_collection.

    Args:
    mongo_collection: A pymongo collection instance representing the students.

    Returns:
    A list of dictionaries, each containing the student's original data
    and their average score.
    """
    result = []
    students = mongo_collection.find({})
    for student in students:
        topics = student.get("topics", [])
        average = sum(i['score'] for i in topics) / len(topics) if topics else 0
        student['averageScore'] = average
        result.append(student)

    sorted_result = sorted(result, key=lambda x: x['averageScore'], reverse=True)
    return result
