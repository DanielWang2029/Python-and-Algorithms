
class FibonacciHeapNode:

    def __init__(self, value, marked=False, parent=None, children=None, prev_peer=None, next_peer=None):
        self.value = value
        self.marked = marked
        self.parent = parent
        self.prev_peer = prev_peer if prev_peer is not None else self
        self.next_peer = next_peer if next_peer is not None else self
        self.children = []
        if children is not None:
            for x in children:
                self.add_child(x if isinstance(x, FibonacciHeapNode) else FibonacciHeapNode(x))
        self.degree = len(self.children)

    def add_child(self, node):
        if not isinstance(node, FibonacciHeapNode):
            assert ValueError(f"Invalid input type: expected FibonacciHeapNode, got {type(node)}")

        if len(self.children) == 0:
            node.next_peer = node.prev_peer = node
        elif len(self.children) == 1:
            node.next_peer = node.prev_peer = self.children[0]
            self.children[0].next_peer = self.children[0].prev_peer = node
        else:
            node.next_peer = self.children[0]
            node.prev_peer = self.children[-1]
            self.children[0].prev_peer = self.children[-1].next_peer = node
        node.parent = self
        self.children.append(node)
        self.degree = len(self.children)

    def remove_child(self, node):
        if not isinstance(node, FibonacciHeapNode):
            assert ValueError(f"Invalid input type: expected FibonacciHeapNode, got {type(node)}")

        if node.parent is not self:
            assert ValueError("Invalid input: node to be removed is not a child.")

        if self.degree == 1:
            self.children = []
        else:
            node.next_peer.prev_peer, node.prev_peer.next_peer = node.prev_peer, node.next_peer
            node.next_peer = node.prev_peer = node
            self.children.remove(node)

        node.parent = None
        self.degree = len(self.children)
        return node

    def print(self, level=0, display=True):
        results = ['|---' * level + f'{self.value}']
        for x in self.children:
            results += x.print(level=level + 1, display=False)
        if display:
            print('\n'.join(results) + '\n')
        return results

    def __str__(self):
        return '\n'.join(self.print(display=False)) + '\n'


n3 = FibonacciHeapNode(3, children=[10, 11, 12])
n2 = FibonacciHeapNode(2, children=[7, 8, 9])
n1 = FibonacciHeapNode(1, children=[4, 5, 6])
n0 = FibonacciHeapNode(0, children=[n1, n2])
n0.add_child(n3)

print(n0)
# prints
# 0
# |---1
# |---|---4
# |---|---5
# |---|---6
# |---2
# |---|---7
# |---|---8
# |---|---9
# |---3
# |---|---10
# |---|---11
# |---|---12

print(n3.next_peer)
# prints
# 1
# |---4
# |---5
# |---6

print(n3.children[0].prev_peer)
# prints
# 12


class FibonacciHeap:

    def __init__(self, arr):
        self.roots = []
        self.min = None
        self.node_map = dict()
        for x in arr:
            self.insert(FibonacciHeapNode(x))

    def insert(self, node):
        if not isinstance(node, FibonacciHeapNode):
            return self.insert(FibonacciHeapNode(node))

        if len(self.roots) == 0:
            node.next_peer = node.prev_peer = node
            self.min = node
        elif len(self.roots) == 1:
            node.next_peer = node.prev_peer = self.roots[0]
            self.roots[0].next_peer = self.roots[0].prev_peer = node
            self.min = node if node.value < self.min.value else self.min
        else:
            node.next_peer = self.roots[0]
            node.prev_peer = self.roots[-1]
            self.roots[0].prev_peer = self.roots[-1].next_peer = node
            self.min = node if node.value < self.min.value else self.min

        node.parent = None
        node.marked = False
        self.roots.append(node)
        if node.value in self.node_map:
            self.node_map[node.value].add(node)
        else:
            self.node_map[node.value] = {node}

    def find_min(self):
        return self.min.value

    def delete_min(self):
        if len(self.roots) == 0:
            assert ValueError('Cannot delete min from an empty heap.')

        self.min.next_peer.prev_peer, self.min.prev_peer.next_peer = self.min.prev_peer, self.min.next_peer
        self.min.next_peer = self.min.prev_peer = self.min
        self.roots.remove(self.min)
        self.node_map[self.min.value].remove(self.min)
        if len(self.node_map[self.min.value]) == 0:
            del self.node_map[self.min.value]

        for x in self.min.children:
            self.insert(x)

        degree_dic = dict()
        for x in self.roots:
            curr = x
            while curr.degree in degree_dic:
                if curr.value < degree_dic[curr.degree].value:
                    curr.add_child(degree_dic[curr.degree])
                    del degree_dic[curr.degree - 1]
                else:
                    degree_dic[curr.degree].add_child(curr)
                    curr = degree_dic[curr.degree]
                    del degree_dic[curr.degree - 1]
            degree_dic[curr.degree] = curr

        self.roots = []
        self.min = None
        for x in degree_dic.values():
            self.roots.append(x)
            self.min = x if self.min is None or x.value < self.min.value else self.min

    def decrease_key(self, old_value, new_value):
        if old_value not in self.node_map:
            raise ValueError(f"{old_value} does not exist in heap.")

        if old_value < new_value:
            raise ValueError(f"Cannot decrease key to a higher value (from {old_value} to {new_value}).")

        if old_value == new_value:
            return

        node = list(self.node_map[old_value])[0]
        if node.parent is None or node.parent.value <= new_value:
            node.value = new_value
            self.node_map[old_value].remove(node)
            if len(self.node_map[old_value]) == 0:
                del self.node_map[old_value]
            if new_value in self.node_map:
                self.node_map[new_value].add(node)
            else:
                self.node_map[new_value] = {node}
            return

        node.value = new_value
        parent_node = node.parent
        parent_node.remove_child(node)
        self.insert(node)
        while parent_node.parent is not None and parent_node.marked:
            parent_node, node = parent_node.parent, parent_node
            parent_node.remove_child(node)
            self.insert(node)
        if parent_node.parent is not None:
            parent_node.marked = True

    def print(self, display=True):
        result = '&\n'.join([str(x) for x in self.roots])
        if display:
            print(result)
        return result

    def __str__(self):
        return self.print(display=False)


h = FibonacciHeap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
# print(h)
# prints 10\n&\n9\n&\n8\n&\n7\n&\n6\n&\n5\n&\n4\n&\n3\n&\n2\n&\n1\n&\n0

h.delete_min()
print(h)
# prints
# 3
# |---4
# |---5
# |---|---6
# |---7
# |---|---8
# |---|---9
# |---|---|---10
# &
# 1
# |---2

h.decrease_key(9, 0)
print(h)
# prints
# 3
# |---4
# |---5
# |---|---6
# |---7
# |---|---8
# &
# 1
# |---2
# &
# 0
# |---10

h.decrease_key(8, -1)
print(h)
# prints
# 3
# |---4
# |---5
# |---|---6
# &
# 1
# |---2
# &
# 0
# |---10
# &
# -1
# &
# 7

h.delete_min()
print(h)
# 0
# |---10
# |---1
# |---|---2
# |---3
# |---|---4
# |---|---5
# |---|---|---6
# &
# 7
