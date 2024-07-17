import redis
from uuid import uuid4

""" This module contains the implementation of the Cache class.
"""


class Cache:
    """
    A class that stores data in Redis
    """
    def __init__(self) -> None:
        """
        Initializes the Redis connection.
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """
        Stores the data in Redis under a unique UUID and returns the UUID.
        """
        id: str = str(uuid4())
        self._redis.set(id, data)
        return id
