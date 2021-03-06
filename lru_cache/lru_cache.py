
import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode



class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()

        self.limit = limit
        self.size = 0
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.storage.move_to_end(node)
        else: 
            return
          

        # if key in self.cache:
        #     # fetch the DLL node which is the value of this key
        #     node = self.cache[key]
        #     self.storage.move_to_end(node)
        #     return node.value[1]
        # else:
        #     return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
          # check if the key is in the cache 
        # if key in self.cache:
        #     node = self.cache[key]
        #     # overwrite the old value 
        #     node.value = (key, value)
        #     # move this node to the tail 
        #     self.storage.move_to_end(node)
        #     return
        # if self.size == self.limit:
        #     # first evict the least-recently used element
        #     oldest_key = self.storage.head.value[0]
        #     del self.cache[oldest_key]
        #     # remove the head node from the DLL
        #     self.storage.remove_from_head()
        #     self.size -= 1
        # # key is not in self.cache and we still have room in our cache
        # # add the key and value
        # self.storage.add_to_tail((key, value))
        # self.cache[key] = self.storage.tail
        # self.size += 1

        if key in self.cache:
            node = key, value
            print("node", node)
            self.storage.move_to_front(node)
            return value
        if self.size == self.limit:
            self.storage.remove_from_tail()
            self.size -= 1
        self.size += 1
        self.storage.add_to_head(value)
        self.cache[key] = value
        return value

        

        
    

