#!/usr/bin/env python3
""" This module contains a function that fetches a web page and stores the
    number of times the page has been fetched in a Redis database.
"""
import requests
import redis
from functools import wraps


def count_history(fn):
    """ A decorator that increments a Redis key each time a method is called.
    """
    @wraps(fn)
    def wrapper(url):
        """ Wrapper for decorator guy """
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
    
    return wrapper


@count_history
def get_page(url: str) -> str:
    """ Fetch a web page and return its content.
    """
    res = requests.get(url)
    return res.text
