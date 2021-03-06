######## Using linked list
#!python

from linkedlist import LinkedList
# from listogram import Listogram
from utils import time_it
# from dictogram import Dictogram


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        # self.buckets = [Listogram() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def __iter__(self, bucket_index):
        return self.buckets[bucket_index].next()

    def __getitem__(self, key):
        # return getattr(self, key)
        return self.get(key)

    # @time_it
    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        Since it has to visit each key, value pair in each bucket"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    # @time_it
    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        Since it has to visit each key, value pair in each bucket"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values


    # @time_it
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        Since it has to visit each key, value pair in each bucket"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    # @time_it
    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) Why and under what conditions?
        If you count all the node each time function is called. O(1) if you have a variable
        to keep track of length"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        # count = 0
        # for bucket in self.buckets:
        #     if not bucket.is_empty():
        #         for key, value in bucket.items():
        #             count += 1
        # return count
        return self.size

    # @time_it
    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(n/b) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        keys = self.keys()
        if key in keys:
            return True
        return False

    # @time_it
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(length of bucket) Why and under what conditions?
        Since we can caluculate which bucket a given key is in, we just check that bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        ### for linked list
        index = self._bucket_index(key)

        try:
            item = self.buckets[index].find(lambda item: item[0] == key)
            return item[1]
        except:
            raise KeyError('Key not found: {}'.format(key))

    # @time_it
    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(length of bucket) Why and under what conditions?
        Since we can caluculate which bucket a given key is in, we just check that bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        ### for linked list
        index = self._bucket_index(key)

        try:
            item = self.buckets[index].find(lambda item: item[0] == key)
            self.buckets[index].replace((key, item[1]), (key, value))
        except:
            self.buckets[index].append((key, value))
            self.size += 1

    # @time_it
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(length of bucket) Why and under what conditions?
        Since we can caluculate which bucket a given key is in, we just check that bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        ### for linked list
        index = self._bucket_index(key)

        try:
            item = self.buckets[index].find(lambda item: item[0] == key)
            self.buckets[index].delete((key, item[1]))
            self.size -= 1
        except:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))
        #test subscripting
        print(ht['I'])

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()

######################## for Listogram
#!python
#
# from listogram import Listogram
# from utils import time_it
# # from dictogram import Dictogram
#
#
# class HashTable(object):
#
#     def __init__(self, init_size=8):
#         """Initialize this hash table with the given initial size."""
#         # Create a new list (used as fixed-size array) of empty linked lists
#         self.buckets = [Listogram() for _ in range(init_size)]
#         self.size = 0
#
#     def __str__(self):
#         """Return a formatted string representation of this hash table."""
#         items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
#         return '{' + ', '.join(items) + '}'
#
#     def __repr__(self):
#         """Return a string representation of this hash table."""
#         return 'HashTable({!r})'.format(self.items())
#
#     def _bucket_index(self, key):
#         """Return the bucket index where the given key would be stored."""
#         # Calculate the given key's hash code and transform into bucket index
#         return hash(key) % len(self.buckets)
#
#     def __iter__(self, bucket_index):
#         return self.buckets[bucket_index].next()
#
#     # @time_it
#     def keys(self):
#         """Return a list of all keys in this hash table.
#         TODO: Running time: O(n) Why and under what conditions?
#         Since it has to visit each key, value pair in each bucket"""
#         # Collect all keys in each bucket
#         all_keys = []
#         for bucket in self.buckets:
#             for key, value in bucket.items():
#                 all_keys.append(key)
#         return all_keys
#
#     # @time_it
#     def values(self):
#         """Return a list of all values in this hash table.
#         TODO: Running time: O(n) Why and under what conditions?
#         Since it has to visit each key, value pair in each bucket"""
#         # TODO: Loop through all buckets
#         # TODO: Collect all values in each bucket
#         all_values = []
#         for bucket in self.buckets:
#             for key, value in bucket.items():
#                 all_values.append(value)
#         return all_values
#
#
#     # @time_it
#     def items(self):
#         """Return a list of all items (key-value pairs) in this hash table.
#         TODO: Running time: O(n) Why and under what conditions?
#         Since it has to visit each key, value pair in each bucket"""
#         # Collect all pairs of key-value entries in each bucket
#         all_items = []
#         for bucket in self.buckets:
#             all_items.extend(bucket.items())
#         return all_items
#
#     # @time_it
#     def length(self):
#         """Return the number of key-value entries by traversing its buckets.
#         TODO: Running time: O(n) Why and under what conditions?
#         If you count all the node each time function is called. O(1) if you have a variable
#         to keep track of length"""
#         # TODO: Loop through all buckets
#         # TODO: Count number of key-value entries in each bucket
#         # count = 0
#         # for bucket in self.buckets:
#         #     if not bucket.is_empty():
#         #         for key, value in bucket.items():
#         #             count += 1
#         # return count
#         return self.size
#
#     def len(self):
#         # TODO: Loop through all buckets
#         # TODO: Count number of key-value entries in each bucket
#         count = 0
#         for bucket in self.buckets:
#             for key, value in bucket.items():
#                 count += 1
#         return count
#     # @time_it
#     def contains(self, key):
#         """Return True if this hash table contains the given key, or False.
#         TODO: Running time: O(n/b) Why and under what conditions?"""
#         # TODO: Find bucket where given key belongs
#         # TODO: Check if key-value entry exists in bucket
#         keys = self.keys()
#         if key in keys:
#             return True
#         return False
#
#     # @time_it
#     def get(self, key):
#         """Return the value associated with the given key, or raise KeyError.
#         TODO: Running time: O(length of bucket) Why and under what conditions?
#         Since we can caluculate which bucket a given key is in, we just check that bucket"""
#         # TODO: Find bucket where given key belongs
#         # TODO: Check if key-value entry exists in bucket
#         # TODO: If found, return value associated with given key
#         # TODO: Otherwise, raise error to tell user get failed
#         # Hint: raise KeyError('Key not found: {}'.format(key))
#         ### for Listogram
#         index = self._bucket_index(key)
#
#         if_contains = self.buckets[index].__contains__(key)
#         if if_contains:
#             for item in self.buckets[index]:
#                 if item[0] is key:
#                     return item[1]
#         else:
#             raise KeyError('Key not found: {}'.format(key))
#
#     # @time_it
#     def set(self, key, value):
#         """Insert or update the given key with its associated value.
#         TODO: Running time: O(length of bucket) Why and under what conditions?
#         Since we can caluculate which bucket a given key is in, we just check that bucket"""
#         # TODO: Find bucket where given key belongs
#         # TODO: Check if key-value entry exists in bucket
#         # TODO: If found, update value associated with given key
#         # TODO: Otherwise, insert given key-value entry into bucket
#         ### for Listogram
#         index = self._bucket_index(key)
#
#         try:
#             item = self.buckets[index].__contains__(key)
#             self.buckets[index].delete(key)
#             self.buckets[index].append((key, value))
#         except:
#             self.buckets[index].append((key, value))
#             self.size += 1
#
#
#     # @time_it
#     def delete(self, key):
#         """Delete the given key from this hash table, or raise KeyError.
#         TODO: Running time: O(length of bucket) Why and under what conditions?
#         Since we can caluculate which bucket a given key is in, we just check that bucket"""
#         # TODO: Find bucket where given key belongs
#         # TODO: Check if key-value entry exists in bucket
#         # TODO: If found, delete entry associated with given key
#         # TODO: Otherwise, raise error to tell user delete failed
#         # Hint: raise KeyError('Key not found: {}'.format(key))
#         ### for listogram
#         index = self._bucket_index(key)
#
#         try:
#             item = self.buckets[index].index_of(key)
#             self.buckets[index].delete(key)
#             self.size -= 1
#         except:
#             raise KeyError('Key not found: {}'.format(key))
#
#
# def test_hash_table():
#     ht = HashTable()
#     print('hash table: {}'.format(ht))
#
#     print('\nTesting set:')
#     for key, value in [('I', 1), ('V', 5), ('X', 10)]:
#         print('set({!r}, {!r})'.format(key, value))
#         ht.set(key, value)
#         print('hash table: {}'.format(ht))
#
#     print('\nTesting get:')
#     for key in ['I', 'V', 'X']:
#         value = ht.get(key)
#         print('get({!r}): {!r}'.format(key, value))
#
#     print('contains({!r}): {}'.format('X', ht.contains('X')))
#     print('length: {}'.format(ht.length()))
#
#     # Enable this after implementing delete method
#     delete_implemented = True
#     if delete_implemented:
#         print('\nTesting delete:')
#         for key in ['I', 'V', 'X']:
#             print('delete({!r})'.format(key))
#             ht.delete(key)
#             print('hash table: {}'.format(ht))
#
#         print('contains(X): {}'.format(ht.contains('X')))
#         print('length: {}'.format(ht.length()))
#
#
# if __name__ == '__main__':
#     test_hash_table()
