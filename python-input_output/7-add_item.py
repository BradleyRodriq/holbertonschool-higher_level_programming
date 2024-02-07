#!/usr/bin/python3
"""add item"""
import json


def load_from_json_file(filename):
    """add item"""
    with open(filename) as f:
        return json.load(f)
