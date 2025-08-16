
# https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees
# Binary index trees, or Fenwick trees, are used to store frequencies and manipulating cumulative frequency


# Consider the following problem: There are n boxes that undergo the following queries:
# q1: add a marble to box i
# q2: sum number of marbles from box i to box j
# To implement these queries, a naive solution has time complexity of O(1) for q1 and O(n) for q2.
# However, with binary index trees, the average and worst time complexity for q2 could be reduced to O(log(n))

# Here's three main ideas for binary index trees:
# 1) store all possible nodes in a complete binary search tree, whose inorder traversal is 1 to n.
# 2) all nodes store cumulative frequencies for itself and its left subtree
# 3) use binary representation (bits) to iterate through the tree


# For idea #1, we want to build up a tree like this (each value in [] representing index):
#                     [8]
#            /--------------------\
#          [4]                    [12]
#      /--------\              /--------\
#    [2]         [6]        [10]        [14]
#   /--\        /--\        /--\        /--\
# [1]   [3]   [5]   [7]   [9]  [11]  [13]  [15]


# For idea #2, lets say the marbles/frequencies for each box/node is as follows:
# {1:4, 2:2, 3:5, 4:11, 5:-1, 6:8, 7:3, 8:8, 9:6, 10:3, 11:8, 12:4, 13:9, 14:4: 15:6}
# Then we want to build up a tree like this:
#                     [8]
#                 22+7+3+8=40
#            /--------------------\
#          [4]                    [12]
#       5+6+11=22               8+9+4=21
#      /--------\              /--------\
#    [2]         [6]        [10]        [14]
#   4+2=6      -1+8=7      6+3=9       9+4=13
#   /--\        /--\        /--\        /--\
# [1]   [3]   [5]   [7]   [9]  [11]  [13]  [15]
#  4     5    -1     3     6     8     9     6      sum = [8]:40 + [12]:21 + [14]:13 + [15]:6 = 80

# Now let's suppose we want to find the cumulative sum from start (i.e. 1) to 13.
# What we need to do is maintain a result counter and iterate downwards until we find the target node.
# During the way down, we add current value to result if we arrived at the node, or we are moving to the right child.
# In this case, we would add 40 and 21 to result since we are about to move right from node 8 and node 12,
# and add 9 to result since we just found node 13, which tells us the total sum is 70.

# Think about why this is correct.
# When we add the value of node 8, i.e. 40, to result, we are essentially adding the cumulative sum of node 1-8.
# Similarly, when we add the value of node 12, i.e. 21, to result, we are adding the cumulative sum of node 9-12.
# We don't want to add the value of node 14 to result because it contains a node higher indexed than node 13 (node 14)
# and we know this by identifying that moving left will go to a node with smaller index.

# Let's take another example and try to find the cumulative sum from start to 6.
# We start at node 8, ignoring its value, go to node 4 and add 22, the cumulative sum of node 1-4, to result.
# Then we reached node 6 and add 7 to result giving us a total of 29.
# We do not want to iterate further to node 5 or node 7 because result already contains the value of node 5,
# and we don't want to do anything with the value of node 7 or beyond as they have larger index than node 6.


# For idea #3, let's take a look at the tree but this time using binary representation for the indexes:
#                    [1000]
#                  22+7+3+8=40
#             /--------------------\
#         [0100]                  [1100]
#        5+6+11=22               8+9+4=21
#       /--------\              /--------\
#   [0010]      [0110]      [1010]      [1110]
#    5+2=6      -1+8=7      6+3=9       9+4=13
#    /--\        /--\        /--\        /--\
# [0001][0011][0101][0111][1001][1011][1101][1111]
#   4     5    -1     3     6     8     9     6

# Now we erase the last significant bit and all the zeros trailing it, i.e. the last 1 and all 0 following it:
#                      []
#                  22+7+3+8=40
#             /--------------------\
#           [0]                    [1]
#        5+6+11=22               8+9+4=21
#       /--------\              /--------\
#     [00]       [01]        [10]        [11]
#    5+2=6      -1+8=7      6+3=9       9+4=13
#    /--\        /--\        /--\        /--\
# [000] [001] [010] [011] [100] [101] [110] [111]
#   4     5    -1     3     6     8     9     6

# Notice that for each node, use 0 for left and 1 for right from the most significant bit to the least significant bit
# would give us the path from root to that node.
# For example, to reach node 5, we could look at its binary representation (w/o last 1 and trailing 0): 001.
# This means we have to go left on root to reach node 4 w/ representation 0,
# go left again to reach node 2 w/ representation 00,
# and then go right to reach node 5 w/ representation 001.

# Therefore with this algorithm, we can iterate through the tree using the binary representation of the index,
# eliminating the need to build an actual tree with nodes.


# Using the ideas above, we could write several function for our binary index tree:

# To get a node's index using its path-corresponding binary representation:
#     def _get_index(self, binary):
#         return int((binary + '1').ljust(self._height, '0'), 2)

# To get the path-corresponding binary representation of a node using index:
#     def _get_binary(self, index):
#         result = bin(index)[2:].rjust(self._height, '0')
#         index = len(result) - 1
#         while index >= 0 and result[index] == '0':
#             index -= 1
#         return result[0: index]

# To get the cumulative sum from start to node:
#     def get_cumulative_sum(self, index):
#         binary = self._get_binary(index)
#         result = self.tree[self._get_index(binary) - 1]
#         while len(binary) > 0:
#             if binary[-1] == '1':
#                 result += self.tree[self._get_index(binary[:-1]) - 1]
#             binary = binary[:-1]
#         return result

# Notice that we have to convert between numeric index and path-corresponding binary representation multiple times.
# Is there a way to iterate through the tree using only its index in binary form (not path-corresponding)?
# The answer is YES!

# Observe that we don't have to go through every parent nodes to get the cumulative sum of a node.
# We only need to visit the left parents, i.e. parents that are left of our node.
# This is why we update only if the last bit for path-corresponding binary is '1', i.e. moving to parent's right child
# Take the cumulative sum of node 11 for example (binary: 1011, path-corresponding binary: 101):
# Since 101 ends with 1, we add the value of node 10 (binary: 1010, path corresponding binary: 10) to result.
# The next bit in 101 is 0, so we don't add the value of node 12 (binary: 1100, path corresponding binary: 1).
# Finally, the last bit in 101 is 1, so we add the value of node 8 (binary: 1000, path corresponding binary: N/A).

# We can also apply the "ignore 0 rule" to the binary representation of the index:
# Starting from the least significant bit, we change 1 into 0 one by one until we reach 0.
# For 1011, we change the last 1 to 0 and get 1010. Then we change another 1 to 0 and get 1000. Finally, we'll reach 0.
# So result = the value of the node itself (1011) + the value of its left parents (1010 and 1000).
# Using the above method, we've successfully got rid of the path-corresponding binary representation!

# The last piece of the puzzle is to derive a method for changing the last/rightmost 1 to 0 in bits operation.
# We observe that for any number, num, that is not 0, we can write it in form of A1B,
# where A is also a binary number and B are all zeros.
# We also know that -num = (A1B)' + 1 = A'0B' + 1.
# Since B is all zeros, B' is all ones, giving us -num = A'0B' + 1 = A'1B
# Therefore changing the last/rightmost 1 to 0 could be done using:
# num_new = num - (-num & num) = A1B - A'1B & A1B = A1B - 01B = A0B


# With these, we could rewrite our get_cumulative_sum. Here's the final implementation of the binary index tree:
class BinaryIndexTree:

    def __init__(self, arr):
        self._length = len(arr)
        self._height = self._get_height()
        self.tree = [0 for _ in range((1 << self._height) - 1)]
        for i, v in enumerate(arr):
            self.increment_value(i + 1, v)

    def _get_height(self):
        if self._length <= 0:
            return 0
        if self._length == 1:
            return 1

        height = 0
        length = self._length
        while length:
            length //= 2
            height += 1

        return height

    def increment_value(self, index, value):
        if index <= 0:
            raise ValueError(f'{index} is not a valid index. Must be a positive integer.')
        if index > self._length:
            raise ValueError(f'Cannot set value on index {index} for a binary index tree with size {self._length}.')

        # here we want to find all right parents to update instead of left, therefore algorithm has been inverted
        binary = index
        while binary <= self._length:
            self.tree[binary - 1] += value
            binary += -binary & binary  # A1B + (A'1B & A1B) = A1B + 1B = (A + 1)0B

    def get_cumulative_sum(self, index):
        if index <= 0:
            raise ValueError(f'{index} is not a valid index. Must be a positive integer.')
        if index > self._length:
            raise ValueError(f'Cannot get sum on index {index} for a binary index tree with size {self._length}.')

        # this is the algorithm describe earlier
        binary = index
        result = 0
        while binary != 0:
            result += self.tree[binary - 1]
            binary -= -binary & binary  # A1B - (A'1B & A1B) = A1B - 1B = A0B

        return result

    def __len__(self):
        return self._length

    def __str__(self):
        if len(self.tree) == 0:
            return 'empty'

        results = []
        height = self._height
        level = height
        number_length = max([len(str(x)) for x in self.tree])
        number_filler_length = 2 + number_length
        slash_inside_filler_length = number_length
        slash_connect_filler_length = number_filler_length + 2 * number_length

        while True:
            if level == 1:
                results.append(f'{self.tree[(1 << height >> 1) - 1]}')
                break

            elements = [str(self.tree[index]).rjust(number_length, ' ')
                        if (index := (1 << (height - level)) * (2 * i + 1) - 1) < self._length
                        else (' ' * number_length).rjust(number_length, ' ')
                        for i in range(1 << level >> 1)]
            results.append((' ' * number_filler_length).join(elements))

            elements = []
            for i in range(1 << level >> 2):
                elements.append('/' + '-' * slash_inside_filler_length + '\\')
            results.append((' ' * slash_connect_filler_length).join(elements))

            number_filler_length = slash_connect_filler_length + slash_inside_filler_length - number_length + 2
            slash_inside_filler_length = number_filler_length - 2
            slash_connect_filler_length = number_filler_length + 2 * number_length
            level -= 1

        return '\n'.join([x.center(len(results[0])) for x in results[::-1]])


t = BinaryIndexTree([4, 2, 5, 11, -1, 8, 3, 8, 6, 3, 8, 4, 9, 4, 6])
print(t)
# prints
#                      40
#            /--------------------\
#          22                      21
#      /--------\              /--------\
#     6           7           9          13
#   /--\        /--\        /--\        /--\
#  4     5    -1     3     6     8     9     6

print(t.get_cumulative_sum(15))  # prints 80
print(t.get_cumulative_sum(5))  # prints 21
print(t.get_cumulative_sum(9) - t.get_cumulative_sum(7))  # prints n8.value + n9.value = 8 + 6 = 14


# The input/value dimension could be more than 1, in which case we'll build up NESTED binary index trees.
# Let's say boxes are now arranged in a square of n x m,
# and we want to count the total number of marbles in all squares within a range defined by (0, 0) and (a, b).

# For this, our BIT is set up in a way that the size of the tree is n and each node is another BIT of size m,
# where tree[i][j] represents the number of marbles in boxes whose row and column indexes are in the subtree of i and j.
# For each "sum" operation describe above, we perform the "binary -= -binary & binary" step for all x,
# and for each of these x, we perform "binary -= -binary & binary" step for all y, adding them all together.
# This would give us a total of O(log(n)log(m)) runtime complexity for each operation.
