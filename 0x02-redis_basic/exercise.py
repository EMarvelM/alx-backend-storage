#!/usr/bin/env python3
""" This module contains the implementation of the Cache class.
"""
import redis
from uuid import uuid4
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key under which the data is stored.
        """
        id: str = str(uuid4())
        self._redis.set(id, data)
        return id
