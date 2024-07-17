""" This module contains the implementation of the Cache class.
"""
import redis
from uuid import uuid4


class Cache:
    """
    """
    def __init__(self) -> None:
        """
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """
        Stores the data in Redis under a unique UUID and returns the UUID.
        """
        id = str(uuid4())
        self._redis.set(id, data)
        return id
