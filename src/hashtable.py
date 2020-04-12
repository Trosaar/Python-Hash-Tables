# '''
# Linked List hash table key/value pair
# '''

import time

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # print(f'start size {self.count} / {self.capacity} = {self.count / self.capacity}')

        if self.count / self.capacity >= 0.7:
            self.resize()
            
        # find spot in array
        index = self._hash_mod(key)

        # if spot is None create new LP
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
            self.count += 1
        else:
            LPCheck = self.storage[index]

            # if spot has something and it matches key, update value
            # if spot has something that didnt match, check next LP
            while LPCheck is not None:

                # check
                if LPCheck.key is key:
                    LPCheck.value = value
                    break
            
                LPCheck = LPCheck.next

            # if we've checked all LPs and none match, create new LP at head.
            if LPCheck is None:
                newLP = LinkedPair(key, value)
                newLP.next = self.storage[index]
                self.storage[index] = newLP
                self.count += 1

        # print(f'End size {self.count} / {self.capacity} = {self.count / self.capacity}')

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # find spot in array
        index = self._hash_mod(key)

        # if spot is None, return error
        if self.storage[index] is None:
            print(f'nothing is in spot {key} -> {index}')
        elif self.storage[index].key is key:
            self.storage[index] = None
            self.count -= 1
        else:
            LPCheck = self.storage[index]
            LPNext = self.storage[index].next

            # if spot has something and it matches key, change pointers
            # if spot has something that didnt match, check next LP
            while LPNext is not None:

                # check
                if LPNext.key is key:
                    LPCheck.next = LPNext.next
                    self.count -= 1
                    break
            
                LPCheck = LPNext
                LPNext = LPNext.next

            # if we've checked all LPs and none match, return error.
            if LPNext is None:
                print(f'no Linked Pair for {key} -> {index}')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # find spot in array
        index = self._hash_mod(key)

        # if spot is None return None
        if self.storage[index] is None:
            return None
        else:
            LPCheck = self.storage[index]

            # if spot has something and it matches key, return value
            # if spot has something that didnt match, check next LP
            while LPCheck is not None:

                # check
                if LPCheck.key is key:
                    return LPCheck.value
            
                LPCheck = LPCheck.next

            # if we've checked all LPs and none match, return None.
            if LPCheck is None:
                return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double capacity
        self.capacity *= 2

        # save old stage to loop over later and rewrite storage with new capactiy.
        old_storage = self.storage
        self.storage = [None] * self.capacity

        # loop though old storage and copy to new storage
        for LPi in old_storage:
            if LPi is not None:
                curLP = LPi

                while curLP is not None:
                    self.count -= 1
                    self.insert(curLP.key, curLP.value)
                    curLP = curLP.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")


# ht = HashTable(8)

# ht.insert("key-0", "val-0")
# ht.insert("key-1", "val-1")
# ht.insert("key-2", "val-2")
# ht.insert("key-3", "val-3")
# ht.insert("key-4", "val-4")
# ht.insert("key-5", "val-5")
# ht.insert("key-6", "val-6")
# ht.insert("key-7", "val-7")
# ht.insert("key-8", "val-8")
# ht.insert("key-9", "val-9")