#!/usr/bin/env python3
"""Task 9"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """TASK 9"""

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
