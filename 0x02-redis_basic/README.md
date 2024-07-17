# 0x02. Redis Basic

## Curriculum
- **Short Specializations Average:** 77.43%
- **Back-end**: Redis

**Project Details:**
- **Weight:** 1
- **Project Start:** Jul 17, 2024, 6:00 AM
- **Project End:** Jul 18, 2024, 6:00 AM
- **Checker Release:** Jul 17, 2024, 12:00 PM
- **Auto Review:** Launched at the deadline

## Resources
Read or watch:
- [Redis Crash Course Tutorial](https://example.com)
- [Redis Commands](https://example.com)
- [Redis Python Client](https://example.com)
- [How to Use Redis With Python](https://example.com)

## Learning Objectives
- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache

## Requirements
- All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7)
- All of your files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5)
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated

## Install Redis on Ubuntu 18.04

```sh
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
