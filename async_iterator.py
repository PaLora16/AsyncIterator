import asyncio


async def all_keys(key):

    keys = {"key1": 1234, "key2": 2345,
            "key3": 3456, "key4": 4567,
            "key5": 5678}

    return keys.get(key)


class KeyTaker:
    """
    Example of async iterator
    """

    def __init__(self, iter_keys):
        # Mandatory iterator definition
        self.iter_keys = iter(iter_keys)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            # extract the keys one at a time
            k = next(self.iter_keys)
        except StopIteration as e:
            # raise stopasynciteration at the end of iterator
            raise StopAsyncIteration from e
        # return values for a key
        return await all_keys(k)


async def main():
    async for c in KeyTaker(["key1", "key2", "key3"]):
        print(c)

asyncio.run(main())
