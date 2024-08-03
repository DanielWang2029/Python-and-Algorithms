
class Heap:

    def __init__(self, arr=None, allow_duplicates=True):
        self.heap = []
        self.location_map = dict()
        self.allow_duplicates = allow_duplicates
        if arr is not None:
            self._heapify(arr)

    def _heapify(self, arr):
        for x in arr:
            self.insert(x)

    def _get_height(self):
        if not self.heap:
            return 0
        if len(self.heap) == 1:
            return 1

        height = 0
        length = len(self.heap)
        while length:
            length //= 2
            height += 1

        return height

    def _get_parent_index(self, index):
        if index == 0:
            return None
        return (index - 1) // 2

    def _get_left_child_index(self, index):
        result = index * 2 + 1
        if result >= len(self.heap):
            return None
        else:
            return result

    def _get_right_child_index(self, index):
        if (result := self._get_left_child_index(index)) is not None:
            return result + 1 if result < len(self.heap) - 1 else None
        else:
            return None

    def get_min(self):
        return self.heap[0]

    def insert(self, value):

        if not self.allow_duplicates and value in self.location_map:
            raise ValueError('Cannot insert duplicate values in heap. Set allow_duplicates=True to avoid this check.')

        self.heap.append(value)
        new_set = self.location_map.get(value, set())
        new_set.add(len(self.heap) - 1)
        self.location_map[value] = new_set

        self_index = len(self.heap) - 1
        while (parent_index := self._get_parent_index(self_index)) is not None:
            if (parent_value := self.heap[parent_index]) > value:
                self.heap[parent_index] = value
                self.heap[self_index] = parent_value
                self.location_map[parent_value].remove(parent_index)
                self.location_map[parent_value].add(self_index)
                self.location_map[value].remove(self_index)
                self.location_map[value].add(parent_index)
                self_index = parent_index
            else:
                break

    def add(self, value):
        return self.insert(value)

    def delete_min(self):
        if len(self.heap) == 0:
            raise ValueError('Cannot delete min from empty heap.')

        if len(self.heap) == 1:
            result = self.heap.pop()
            self.location_map = dict()
            return result

        result = self.heap[0]
        self.delete(result)
        return result

    def pop(self):
        return self.delete_min()

    def delete(self, value):
        if len(self.heap) == 0:
            raise ValueError(f"Cannot delete from empty heap.")

        if value not in self.location_map:
            raise ValueError(f"{value} does not exist in heap.")

        if value == self.heap[-1]:
            self.heap.pop()
            self.location_map[value].remove(len(self.heap))
            if len(self.location_map[value]) == 0:
                del self.location_map[value]
            return

        curr_index, curr_value = min(self.location_map[value]), self.heap[-1]
        self.heap[curr_index] = self.heap.pop()
        self.location_map[value].remove(curr_index)
        if len(self.location_map[value]) == 0:
            del self.location_map[value]
        self.location_map[curr_value].remove(len(self.heap))
        self.location_map[curr_value].add(curr_index)

        while (left_index := self._get_left_child_index(curr_index)) is not None:
            if (right_index := self._get_right_child_index(curr_index)) is not None:
                target_index = left_index if self.heap[left_index] <= self.heap[right_index] else right_index
            else:
                target_index = left_index
            target_value = self.heap[target_index]
            if target_value >= curr_value:
                break
            self.heap[target_index] = curr_value
            self.heap[curr_index] = target_value
            self.location_map[curr_value].remove(curr_index)
            self.location_map[curr_value].add(target_index)
            self.location_map[target_value].remove(target_index)
            self.location_map[target_value].add(curr_index)
            curr_index = target_index

    def decrease_key(self, old_value, new_value, apply_all=False):
        if old_value not in self.location_map:
            raise ValueError(f"{old_value} does not exist in heap.")

        if old_value < new_value:
            raise ValueError(f"Cannot decrease key to a higher value (from {old_value} to {new_value}).")

        if old_value == new_value:
            return

        self_index = min(self.location_map[old_value])
        self.heap[self_index] = new_value
        if new_value in self.location_map:
            self.location_map[new_value].add(self_index)
        else:
            self.location_map[new_value] = {self_index}
        self.location_map[old_value].remove(self_index)
        if len(self.location_map[old_value]) == 0:
            del self.location_map[old_value]
        while (parent_index := self._get_parent_index(self_index)) is not None:
            if (parent_value := self.heap[parent_index]) > new_value:
                self.heap[parent_index] = new_value
                self.heap[self_index] = parent_value
                self.location_map[parent_value].remove(parent_index)
                self.location_map[parent_value].add(self_index)
                self.location_map[new_value].remove(self_index)
                self.location_map[new_value].add(parent_index)
                self_index = parent_index
            else:
                break

        if apply_all and old_value in self.location_map:
            self.decrease_key(old_value, new_value, apply_all=True)

    def length(self):
        return len(self.heap)

    def print(self,
              display=True,
              fill_slash_inside_char='-',
              fill_slash_connect_char=' ',
              fill_number_connect_char=' ',
              fill_empty_char=' ',
              leading_zero=False):
        if len(self.heap) == 0:
            return 'empty'

        results = []
        height = self._get_height()
        level = height
        number_length = max([len(str(x)) for x in self.heap])
        number_filler_length = 2 + number_length
        slash_inside_filler_length = number_length
        slash_connect_filler_length = number_filler_length + 2 * number_length

        while True:
            if level == 1:
                results.append(f'{self.heap[0]}')
                break

            elements = [str(x).rjust(number_length, '0' if leading_zero else ' ')
                        for x in self.heap[(1 << level >> 1) - 1: (1 << level) - 1]]
            if level == height:
                elements += [fill_empty_char * number_length for _ in range((1 << level) - len(self.heap) - 1)]
            results.append((fill_number_connect_char * number_filler_length).join(elements))

            if level == height:
                elements = []
                slashes = ['/' if i % 2 == 1 else '\\' for i in range((1 << level >> 1) - 1, len(self.heap))]
                slashes += ['-'] * ((1 << level) - len(self.heap) - 1)
                for i in range(1 << level >> 2):
                    if slashes[2 * i] == '/' and slashes[2 * i + 1] == '\\':
                        elements.append('/' + fill_slash_inside_char * slash_inside_filler_length + '\\')
                    elif slashes[2 * i] == '/':
                        elements.append('/' + fill_slash_connect_char * slash_inside_filler_length + fill_empty_char)
                    else:
                        elements.append(fill_empty_char
                                        + fill_slash_connect_char * slash_inside_filler_length
                                        + fill_empty_char)
            else:
                elements = ['/' + fill_slash_inside_char * slash_inside_filler_length + '\\'] * (1 << level >> 2)
            results.append((fill_slash_connect_char * slash_connect_filler_length).join(elements))

            number_filler_length = slash_connect_filler_length + slash_inside_filler_length - number_length + 2
            slash_inside_filler_length = number_filler_length - 2
            slash_connect_filler_length = number_filler_length + 2 * number_length
            level -= 1

        representation = '\n'.join([x.center(len(results[0])) for x in results[::-1]])
        if display:
            print(representation)
        return representation

    def _sanity_check(self):
        if not self.allow_duplicates:
            assert all([len(x) == 1 for x in self.location_map.values()]), \
                "A heap that does not allow duplicates cannot have elements that have 0 or 2+ locations in it."
        assert all([all([self.heap[y] == x for y in self.location_map[x]]) for x in self.location_map]), \
            "The location_map is not properly maintained."

    def __len__(self):
        return self.length()

    def __getitem__(self, index):
        return self.heap[index]

    def __setitem__(self, index, value):
        return self.decrease_key(self.heap[index], value)

    def __str__(self):
        return self.print(display=False)


h = Heap([x for x in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]])
print(h)
# prints
#                      0
#            /--------------------\
#           1                       5
#      /--------\              /--------\
#     4           2           9           6
#   /--\        /--\
# 10     7     8     3

h.pop()
print(h)
# prints
#                      1
#            /--------------------\
#           2                       5
#      /--------\              /--------\
#     4           3           9           6
#   /--\        /
# 10     7     8

h.delete(2)
print(h)
# prints
#                      1
#            /--------------------\
#           3                       5
#      /--------\              /--------\
#     4           8           9           6
#   /--\
# 10     7

h.insert(11)
print(h)
# prints
#                      1
#            /--------------------\
#           3                       5
#      /--------\              /--------\
#     4           8           9           6
#   /--\        /
# 10     7    11

h.decrease_key(7, 2)
print(h)
# prints
#                      1
#            /--------------------\
#           2                       5
#      /--------\              /--------\
#     3           8           9           6
#   /--\        /
# 10     4    11

# this implementation also supports tuples and other comparable and immutable objects
h = Heap([(x, -x) for x in range(0, -10, -1)])
print(h)
# prints
#                                                         (-9, 9)
#                                /-------------------------------------------------------\
#                         (-8, 8)                                                         (-5, 5)
#                /-----------------------\                                       /-----------------------\
#         (-6, 6)                         (-7, 7)                         (-1, 1)                         (-4, 4)
#        /-------\                       /
#  (0, 0)         (-3, 3)         (-2, 2)

h.delete_min()
print(h)
# prints
#                                                         (-8, 8)
#                                /-------------------------------------------------------\
#                         (-7, 7)                                                         (-5, 5)
#                /-----------------------\                                       /-----------------------\
#         (-6, 6)                         (-2, 2)                         (-1, 1)                         (-4, 4)
#        /-------\
#  (0, 0)         (-3, 3)

h.decrease_key((0, 0), (-7, 0))
print(h)
# prints
#                                                         (-8, 8)
#                                /-------------------------------------------------------\
#                         (-7, 0)                                                         (-5, 5)
#                /-----------------------\                                       /-----------------------\
#         (-7, 7)                         (-2, 2)                         (-1, 1)                         (-4, 4)
#        /-------\
# (-6, 6)         (-3, 3)
