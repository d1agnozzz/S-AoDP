# Простое ре-хеширование | С помощью псевдослучайных чисел | Метод цепочек
import hashlib
import random
import sys


class HashTableSimple:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def rehash_index(self, collision_ind):
        # Find index of first blank bucket
        # for _ in range(self.size-1):
        new_ind = collision_ind + 1
        new_ind %= self.size
        # if len(self.hash_table[collision_ind]) == 0:
        return new_ind

    # return "Table is full, no place for new records"

    def get_hash(self, key):
        # hashed_bytes = hashlib.sha256(str.encode(key)).digest()
        # hashed_int = int.from_bytes(hashed_bytes, byteorder='big', signed=False)
        hashed_int = ord(key[0])
        hashed_key = hashed_int % self.size
        return hashed_key

    # Insert values into hash map
    def set_val(self, key, val):        
        hashed_key = self.get_hash(key)

        bucket = self.hash_table[hashed_key]

        if len(bucket) == 0:
            bucket.append((key, val))
            return
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                bucket.pop()
                bucket.append((key, val))
                return
        else:
            for _ in range(self.size - 1):
                hashed_key = self.rehash_index(hashed_key)
                bucket = self.hash_table[hashed_key]
                if len(bucket) == 0:
                    bucket.append((key, val))
                    return
                for index, record in enumerate(bucket):
                    record_key, record_val = record
                    if record_key == key:
                        bucket.pop()
                        bucket.append((key, val))
                        return

    # Return searched value with specific key
    def get_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = self.get_hash(key)

        # Get the bucket corresponding to index

        for _ in range(self.size - 1):
            bucket = self.hash_table[hashed_key]

            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_val = record

                # check if the bucket has same key as
                # the key being searched
                if record_key == key:
                    found_key = True
                    break

            # If the bucket has same key as the key being searched,
            # Return the value found
            # Otherwise indicate there was no record found
            if found_key:
                return record_val
            else:
                hashed_key = self.rehash_index(hashed_key)
        return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = self.get_hash(key)

        # Get the bucket corresponding to index
        for _ in range(self.size - 1):
            bucket = self.hash_table[hashed_key]

            found_key = False
            for index, record in enumerate(bucket[:]):
                record_key, record_val = record

                # check if the bucket has same key as
                # the key to be deleted
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                bucket.pop(index)
            else:
                hashed_key = self.rehash_index(hashed_key)
        return

    # To print the items of hash map
    def __str__(self):
        return "\n".join(str(item) for item in self.hash_table)


class HashTablePseudoRandom(HashTableSimple):
    def rehash_index(self, collision_ind):
        random.seed(collision_ind)
        new_ind = collision_ind + random.randint(1, sys.maxsize)
        new_ind %= self.size
        return new_ind


class HashTableChaining(HashTableSimple):
    def set_val(self, key, val):
        hashed_key = self.get_hash(key)

        bucket = self.hash_table[hashed_key]

        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                bucket[index] = (key, val)
                return

        bucket.append((key, val))

    def get_val(self, key):
        hashed_key = self.get_hash(key)

        bucket = self.hash_table[hashed_key]

        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                return record_val

    def delete_val(self, key):
        hashed_key = self.get_hash(key)

        bucket = self.hash_table[hashed_key]

        for index, record in enumerate(bucket[:]):
            record_key, record_val = record
            if record_key == key:
                del bucket[index]


print()

table_size = 10

hash_table = HashTableSimple(table_size)

hash_table.set_val("a", "va")
hash_table.set_val("ab", "vab")
hash_table.set_val("abc", "vabc")
hash_table.set_val("bcd", "vbcd")
hash_table.set_val("ab", "AB")
hash_table.set_val("abcd", "vabcd")



print(hash_table)
print(hash_table.get_val("ab"))
print()

# hash_table = HashTablePseudoRandom(table_size)

# hash_table.set_val("a", "v")
# hash_table.set_val("ab", "vab")
# hash_table.set_val("abc", "v")
# hash_table.set_val("bcd", "v")
# hash_table.set_val("abcd", "v")
# hash_table.delete_val("a")
# hash_table.delete_val("bcd")

# print(hash_table)
# print(hash_table.get_val("ab"))
# print()

hash_table = HashTableChaining(table_size)

hash_table.set_val("a", "v")
hash_table.set_val("ab", "vab")
hash_table.set_val("abc", "v")
hash_table.set_val("ab", "AB")
hash_table.set_val("bcd", "v")
hash_table.set_val("abcd", "v")
# hash_table.delete_val("a")
# hash_table.delete_val("bcd")


print(hash_table)
print(hash_table.get_val("ab"))
print()