"""
This module encapsulates the DB abstraction layer.

Make sure the mongodb server is available locally while developing.
This could be done via running a docker container from
https://hub.docker.com/_/mongo

See the PyMongo documentation at
https://pymongo.readthedocs.io/en/stable/tutorial.html
"""


def get(number):
    """
    Extracts original long URL from DB by its ID.
    """


def put(link):
    """
    Writes new link into the DB and returns its ID.
    """


def find(link):
    """
    Checks if this link already was saved to DB. Returns ID if found.
    """
