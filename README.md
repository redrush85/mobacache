# mobacache [![Build Status](https://travis-ci.org/redrush85/mobacache.svg?branch=master)](https://travis-ci.org/redrush85/mobacache)
mobacache is a pythonic interface for creating a cache over redis. It provides simple decorators that can be added to any function to cache its return values.

# Requirements:
`Python 2.7+`


# Installation
`pip install moba-cache`

or to get the latest version

    git clone https://github.com/redrush85/mobacache.git
    cd mobacache
    python setup.py install


# Usage

## Setup
```python
from mobacache import CacheBuilder
import redis

redis_conn = redis.StrictRedis()
cb = CacheBuilder(redis_conn)

```

## Cache

```python
@cb.cache(ttl=10)
def my_method(a=1, b=2, c=0):
    return a + b + c
```


# Contributors
- Alexander Kuts
- Roman Gorin

# Tests
`nosetests`
