# 0x01. NoSQL

## Curriculum Overview
**Specializations Average:** 70.87%

**Module Focus:** NoSQL Databases with MongoDB

### Resources
- **NoSQL Databases Explained**
- **What is NoSQL?**
- **MongoDB with Python Crash Course - Tutorial for Beginners**
- **MongoDB Tutorial 2: Insert, Update, Remove, Query**
- **Aggregation**
- **Introduction to MongoDB and Python**
- **mongo Shell Methods**
- **Mongosh**

### Learning Objectives
By the end of this project, you should be able to:
1. Explain what NoSQL means.
2. Differentiate between SQL and NoSQL databases.
3. Define ACID properties.
4. Describe document storage.
5. Identify various NoSQL types.
6. Enumerate the benefits of NoSQL databases.
7. Query information from a NoSQL database.
8. Insert, update, and delete information in a NoSQL database.
9. Use MongoDB effectively.

### Requirements

#### MongoDB Command Files
- Interpret/compile on Ubuntu 18.04 LTS using MongoDB 4.2.
- End all files with a new line.
- Include a comment at the beginning of all files: `// my comment`
- Include a README.md file in the root of the project folder.
- Test file length using `wc`.

#### Python Scripts
- Interpret/compile on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10.
- End all files with a new line.
- Include the shebang `#!/usr/bin/env python3` at the beginning of all files.
- Include a README.md file in the root of the project folder.
- Use pycodestyle (version 2.5.*).
- Test file length using `wc`.
- Include documentation for all modules and functions.
- Prevent code execution upon import with `if __name__ == "__main__":`.

### Setup

#### Install MongoDB 4.2 on Ubuntu 18.04
```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
$ mongo --version
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'

