import pickle
import logging
from functools import wraps

cache_logger = logging.getLogger(name='cache.logger')

class CacheBuilder:
    """
    class for caching everything
    """

    cache_func_key = "cache:func:{}:{}"

    def __init__(self, conn=None, enable_log=False):
        """
        Init
        :param conn: memory_broker connection
        """
        self.conn = conn
        self.enable_log = enable_log

    def _write_log(self, message):
        if self.enable_log:
            cache_logger.info(message)

    def set(self, key, value, ttl=None):
        """
        cache value in memory_broker
        :param key: cache key
        :param value: cache value
        :param ttl: value expires in ttl seconds
        :return:
        """
        self.conn.set(key, pickle.dumps(value))

        if ttl:
            self.conn.expire(key, ttl)

        return value

    def get(self, key):
        """
        try to get cached value from memory_broker
        :param key:
        :return:
        """
        value = self.conn.get(key)

        if value:
            self._write_log("hit cache. key: {}".format(key))
            value = pickle.loads(value)
        else:
            self._write_log("miss cache. key: {}".format(key))

        return value

    def fkeygen(self, func, *args, **kwargs):
        """
        generate cache key for function
        :param func: function (func.__name__)
        :param args: function args
        :param kwargs: function kwargs
        :return: cache key (string)
        """
        items = args + tuple(sorted(kwargs.items()))
        key = pickle.dumps(items)

        return self.cache_func_key.format(func.__name__, key)

    def delete(self, key):
        """
        Delete key from cache
        :param key: cache key
        :return: True if key was in cache, else - False
        """
        value = self.conn.get(key)

        if value:
            self.conn.delete(key)
            return True

        return False

    def finvalidate(self, func, *args, **kwargs):
        """
        Invalidate cache in memory_broker by func name in its args/kwargs
        :param func: function (func.__name__)
        :param args: function args
        :param kwargs: function kwargs
        :return: True if key was in cache, else - False
        """
        key = self.fkeygen(func, *args, **kwargs)
        return self.delete(key)

    def cache(self, ttl=None):
        """
        cache decorator
        Example:
                cache = CacheBuilder(redis_conn)
                @cache.cache(ttl=10)
                def test(a=1, b=2, c=0):
                    print("func calculations")
                    return a + b + c

        :param ttl:  cache expires in ttl seconds
        """
        def wrap(func):
            @wraps(func)
            def wrapped(*args, **kwargs):
                if self.conn:
                    # convert func's args to bytes
                    key = self.fkeygen(func, *args, **kwargs)

                    # get data from cache or run func and store its result in cache
                    return self.get(key=key) or self.set(key=key, value=func(*args, **kwargs), ttl=ttl)

                return func(*args, **kwargs)
            return wrapped
        return wrap


