import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes 
      # for us to call `insert` on them 
        if value < self.value:
          # check if self.left is a valid node 
            if self.left:
                self.left.insert(value)
          # the left side is empty 
            else:
              # we've found a valid parking spot 
              self.left = BinarySearchTree(value)
      # otherwise, value >= self.value
        else:
            if self.right:
              self.right.insert(value)
            else:
              self.right = BinarySearchTree(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        print(type(target), type(self.value))
        print(target == self.value)
        if target == self.value:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else: 
            if self.left:
                return self.left.contains(target)
            else:
                return False
       
  

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

           


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
