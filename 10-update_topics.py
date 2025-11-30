#!/usr/bin/env python3
"""TASK 10"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """TASK 10"""

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
