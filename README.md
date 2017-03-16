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

## Advance cache
```python
@cb.advance_cache(key_format="{a}:{b}:var_c={c}", ttl=10)
def my_method(a=0, b=0, c=0):
    return a + b + c
    
my_method(1, 2, 3)
data = cb.get("1:2:var_c=3")
print(data) # 6
```


# Contributors
- Alexander Kuts
- Roman Gorin

# Tests
`python -m unittest`
