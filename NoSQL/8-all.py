#!/usr/bin/env python3
"""Task 8"""


import pymongo


def list_all(mongo_collection):
    """Task 8"""

    return list(mongo_collection.find())
