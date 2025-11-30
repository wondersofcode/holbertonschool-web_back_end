#!/usr/bin/env python3
"""TASK 11"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """TASK 11"""

    return list(mongo_collection.find({"topics": topic}))
