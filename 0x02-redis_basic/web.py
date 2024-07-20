#!/usr/bin/env python3
""" 
"""
import requests
import redis
from functools import wraps


def count_history(method):
    @wraps(method)
    def wrapper(url, *args, **kwargs):
        result = method(url, *args, **kwargs)
        _redis = redis.Redis()
        before = _redis.get(f"count:{url}")
        _redis.set(f"count:{url}", int(before.decode('utf-8')) + 1 if before else 1)
        _redis.expire(f"count:{url}", 1000)
        return result
    return wrapper

@count_history
def get_page(url: str) -> str:
    res = requests.get(url)
    return res.text
