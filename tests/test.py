from unittest import TestCase
from mobacache.base import BaseProvider
from mobacache import CacheBuilder

class MockRedis(BaseProvider):
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, None)

    def expire(self, key, ttl):
        return True

    def delete(self, key):
        data = self.data.pop(key, None)
        if data:
            return True
        else:
            return False


class TestRedisClient(TestCase):
    def setUp(self):
        self.cache = CacheBuilder(conn=MockRedis())

    def test_getset(self):
        data = self.cache.set("key1", "value1")
        self.assertEqual(data, "value1")
        self.assertNotEqual(data, "key1")
        result = self.cache.get("key1")
        self.assertEqual(result, "value1")

    def test_fgetset(self):

        @self.cache.cache()
        def func1(a=1, b=2):
            return a + b

        func1(a=1, b=2)

        key = self.cache.fkeygen(func1, a=1, b=2)
        data = self.cache.get(key)
        self.assertEqual(data, 3)

        data = self.cache.get(key)
        self.assertNotEqual(data, 4)

    def test_del(self):
        self.cache.set("key1", "value1")
        data = self.cache.get("key1")
        self.assertEqual(data, "value1")

        del_result = self.cache.delete("key1")
        self.assertTrue(del_result)

        del_result = self.cache.delete("key1")
        self.assertFalse(del_result)

        data = self.cache.get("key1")
        self.assertFalse(data)

    def test_advance_cache(self):
        @self.cache.advance_cache("variable_a:{a}:variable_b:{b}")
        def func1(a, b):
            return a * b

        func1(a=4, b=5)

        data = self.cache.get("variable_a:4:variable_b:5")
        self.assertEqual(data, 20)

    def test_advance_cache_execption(self):
        cache = CacheBuilder(conn=MockRedis(), silence_mode=False)

        @cache.advance_cache("variable_a:{a}:variable_b:{c}")
        def func1(a, b):
            return a * b

        with self.assertRaises(KeyError):
            func1(a=4, b=5)






