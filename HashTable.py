from Package import *

# Created a chaining hash table class to store the data for each package and quickly retrieve it.
class ChainingHashTable:
    # Constructor allows for initial capacity
    # Assigns buckets with empty list
    def __init__(self, capacity=10):
        # Initialize hash table with empty buckets list
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Inserts / Updates item in the hash table
    def insert(self, key, package):
        # Get location of bucket being used
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # If key is in bucket, update the package info
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = package
                return True
        # If not in bucket, insert package info at end of bucket list
        key_value = [key, package]
        bucket_list.append(key_value)

    # Searches for package with key in the hash table
    # Returns item if found
    def search(self, key):
        # Get location of bucket where key should be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Search for key in the bucket
        for kv in bucket_list:
            # Find item's key and return item in the bucket
            if kv[0] == key:
                return kv[1]

    # Remove item using key from the hash table
    def remove(self, key):
        # Get location of bucket where key should be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Remove item from bucket list
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove(kv[0], kv[1])

# Create and load the hash table
myHash = ChainingHashTable()
loadPackageData('WGUPS Package File.csv', myHash)