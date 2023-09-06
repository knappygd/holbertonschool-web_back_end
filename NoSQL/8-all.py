#!/usr/bin/env python3
"""lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    c = mongo_collection.find()
    l = []
    for i in c:
        l.append(i)
    return l
