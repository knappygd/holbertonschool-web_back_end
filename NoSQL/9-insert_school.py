#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    d = {}
    for k, v in kwargs.items():
        d[k] = v
    mongo_collection.insert(d)
    return d["_id"]
