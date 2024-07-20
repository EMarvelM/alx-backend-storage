#!/usr/bin/env python3
""" This module contains the implementation of the Cache class.
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable):
    """ A decorator that increments a Redis key each time a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)  # Increment the method call count in Redis
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable):
    """ A decorator that adds to the end of a list
    """
    @wraps(method)
    def inner(self, *args, **kwargs):
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        key = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(key))
        return key
    return inner


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

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key under which the data is stored.
        """
        id: str = str(uuid4())
        self._redis.mset({id: data})
        return id

    def get(self, key: str, fn: Callable = None) -> \
            Union[str, float, int, None]:
        """
        Retrieve data from Redis by key and convert it using a given function.

        Args:
            key (str): The key for the data to retrieve.
            fn (Callable, optional): A function to convert the data from bytes.

        Returns:
            Union[bytes, str, int, None]: The retrieved and converted data,
            or None if the key doesn't exist.
        """
        data = self._redis.get(key)
        if data and fn:
            data = fn(data)

        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string value from Redis.

        Args:
            key (str): The key for the data to retrieve.

        Returns:
            Union[str, None]: The string data, or None if
            the key doesn't exist.

        """
        return self.get(key, lambda b: b.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer value from Redis.

        Args:
            key (str): The key for the data to retrieve.

        Returns:
            Union[int, None]: The integer data, or
            None if the key doesn't exist.
        """
        return self.get(key, int)


def replay(fn):
    """
    """
    _redis = redis.Redis()
    inputs = _redis.lrange(f"{fn.__qualname__}:inputs", 0, -1)
    outputs = _redis.lrange(f"{fn.__qualname__}:outputs", 0, -1)

    inputs = [i.decode('utf-8') for i in inputs]
    outputs = [i.decode('utf-8') for i in outputs]

    print(f"{fn.__qualname__} was called {len(inputs)} times:")
    for inp, outp, i in zip(inputs, outputs, range(len(inputs))):
        print(f"{fn.__qualname__}(*{inputs[i]}) -> {outputs[i]}")
