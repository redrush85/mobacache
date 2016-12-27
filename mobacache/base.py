class BaseProvider:
    """
    Base memory-broker provider (Has the same methods as redis)
    """
    def set(self, key, value):
        pass

    def get(self, key):
        pass

    def expire(self, key, ttl):
        pass

    def delete(self, key):
        pass