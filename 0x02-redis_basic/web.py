#!/usr/bin/env python3
""" This module contains a function that fetches a web page and stores the
    number of times the page has been fetched in a Redis database.
"""
import requests
import redis
from functools import wraps


def count_history(method):
    """ A decorator that increments a Redis key each time a method is called.
    """
    @wraps(method)
    def wrapper(url, *args, **kwargs):
        result = method(url, *args, **kwargs)
        _redis = redis.Redis()
        before = _redis.get(f"count:{url}")
        _redis.set(f"count:{url}",
                   int(before.decode('utf-8')) + 1 if before else 1)
        _redis.expire(f"count:{url}", 1000)
        return result
    return wrapper


@count_history
def get_page(url: str) -> str:
    """ Fetch a web page and return its content.
    """
    res = requests.get(url)
    return res.text
