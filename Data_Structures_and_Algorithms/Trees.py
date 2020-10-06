

from typing import List
from Data_Structures_and_Algorithms.Stack_and_Queue import Queue


class Node:
    def __init__(self, data=-1, *args):
        self._data = data
        self._roots = [item for item in args]

    def set_data(self, data):
        self._data = data

    def set_roots(self, *args):
        self._roots = [item for item in args]

    def get_data(self):
        return self._data

    def get_roots(self) -> List:
        return self._roots

    def at_bottom(self):
        if len(self._roots) == 0:
            return True
        for value in self._roots:
            if value is not None:
                return False
        return True

    def is_leaf(self):
        return self.at_bottom()


class BinaryNode(Node):
    def __init__(self, data=-1, left=None, right=None):
        super().__init__(data, *[left, right])

    def get_left_node(self):
        return self.get_roots()[0]

    def get_right_node(self):
        return self.get_roots()[1]

    def set_roots(self, *args):
        assert len(args) == 2 or len(args) == 0, 'Invalid Input. Too many roots to set for a binary node'
        if len(args) == 0:
            super().set_roots(*[None, None])
        else:
            super().set_roots(*args)


class Tree:
    def __init__(self, root: Node = None):
        self._root = root

    def set_root(self, root: Node):
        self._root = root

    def get_root(self) -> Node:
        return self._root

    def get_sum(self):
        return self._get_sum_helper(self.get_root())

    @staticmethod
    def _get_sum_helper(currentNode: BinaryNode) -> int:
        if currentNode is None:
            return 0
        if currentNode.at_bottom():
            return currentNode.get_data()
        result = currentNode.get_data()
        for value in currentNode.get_roots():
            result += BinaryTree._get_sum_helper(value)
        return result

    def get_height_node(self, node: Node):
        return self._get_height_helper(node)

    def get_height(self):
        return self._get_height_helper(self.get_root())

    @staticmethod
    def _get_height_helper(currentNode: Node) -> int:
        if currentNode is None:
            return -1
        if currentNode.at_bottom():
            return 0
        rts = currentNode.get_roots()
        maxHeight = -1
        for value in rts:
            currentHeight = Tree._get_height_helper(value)
            maxHeight = currentHeight + 1 if currentHeight >= maxHeight else maxHeight
        return maxHeight

    def get_depth(self, node: Node):
        return Tree._get_depth_helper(node, self.get_root())

    @staticmethod
    def _get_depth_helper(node: Node, currentNode: Node):
        if currentNode is None:
            return -1
        if currentNode is node:
            return 0
        for value in currentNode.get_roots():
            result = Tree._get_depth_helper(node, value)
            if result != -1:
                return result + 1
        return -1

    def get_path(self, node: Node):
        result = self._get_path_helper(node, self.get_root(), []) or []  # returns [] if helper function returns None
        result.reverse()
        return result

    @staticmethod
    def _get_path_helper(node: Node, currentNode: Node, arr: List[Node]) -> List[Node]:
        if currentNode is None:
            return []
        if node is currentNode:
            arr.append(currentNode)
            return arr
        for value in currentNode.get_roots():
            result = Tree._get_path_helper(node, value, arr)
            if result:  # note that [] is evaluated to False
                arr.append(currentNode)
                return result
        return []

    def get_parent(self, node: Node) -> Node:
        if self.get_root() is node:
            return None
        else:
            return self.get_path(node)[-2]

    def get_tree_top_to_bottom(self):
        result = []
        if self._root is None:
            return result
        queue = Queue(self._root)
        while len(queue) != 0:
            currentNode = queue.pop()
            result.append(currentNode)
            for value in currentNode.get_roots():
                if value is not None:
                    queue.push(value)
        return result

    def print_tree_top_to_bottom(self):  # Breadth First Search or BFS
        result = self.get_tree_top_to_bottom()
        print([val.get_data() for val in result])
        print()

    def print_tree_top_to_bottom_recursion(self):
        result = BinaryTree._print_tree_top_to_bottom_recursion_helper(self.get_root(), Queue(), [])
        print(result)
        print()

    @staticmethod
    def _print_tree_top_to_bottom_recursion_helper(currentNode: Node, queue: Queue, result: List) -> List:
        result.append(currentNode.get_data())
        for value in currentNode.get_roots():
            if value is not None:
                queue.push(value)
        if len(queue) != 0:
            nextNode = queue.pop()
            result = BinaryTree._print_tree_top_to_bottom_recursion_helper(nextNode, queue, result)
        return result

    def mirror(self):
        BinaryTree._mirror_helper(self.get_root())

    @staticmethod
    def _mirror_helper(currentNode: Node):
        if currentNode is None:
            return
        arr = currentNode.get_roots()
        arr.reverse()
        currentNode.set_roots(*arr)
        for value in arr:
            BinaryTree._mirror_helper(value)

    def is_sibling(self, firstNode: Node, secondNode: Node):
        firstPath = self.get_path(firstNode)
        secondPath = self.get_path(secondNode)
        firstPath.pop()
        secondPath.pop()
        for index, value in enumerate(firstPath):
            if value is not secondPath[index]:
                return False
        return True

    def num_of_nodes(self) -> int:
        return Tree._num_of_nodes_helper(self.get_root())

    @staticmethod
    def _num_of_nodes_helper(node: Node) -> int:
        if node is None:
            return 0
        result = 0
        for value in node.get_roots():
            result += Tree._num_of_nodes_helper(value)
        return result + 1


class BinaryTree(Tree):
    def __init__(self, root: BinaryNode = None):
        super().__init__(root)

    def print_tree_left_to_right(self):  # Depth First Search or DFS
        result = BinaryTree._print_tree_left_to_right_helper(self.get_root(), [])
        print([val.get_data() for val in result])
        print()

    @staticmethod
    def _print_tree_left_to_right_helper(currentNode: BinaryNode, result: List) -> List:
        if currentNode is None:
            return result
        if currentNode.at_bottom():
            result.append(currentNode)
            return result
        result = BinaryTree._print_tree_left_to_right_helper(currentNode.get_left_node(), result)
        result.append(currentNode)
        result = BinaryTree._print_tree_left_to_right_helper(currentNode.get_right_node(), result)
        return result

    def is_proper(self) -> bool:
        return BinaryTree._is_proper_helper(self.get_root())

    @staticmethod
    def _is_proper_helper(node: BinaryNode) -> bool:
        if node.get_left_node() is None and node.get_right_node() is None:
            return True
        elif node.get_left_node() is None or node.get_right_node() is None:
            return False
        else:
            return BinaryTree._is_proper_helper(node.get_left_node()) and \
                   BinaryTree._is_proper_helper(node.get_right_node())

    #  algorithm for determining the completeness using nodes on height - 1 level:
    #  variable names:
    #  full    left       right       Execution
    #  according variable value:
    #  True    None       None        continue
    #  True    not None   None        return False
    #  True    None       not None    return False
    #  True    not None   not None    return False
    #  False   None       None        full = True
    #  False   not None   None        full = True
    #  False   None       not None    return False
    #  False   not None   not None    continue
    def is_complete(self) -> bool:
        arr = self.get_tree_top_to_bottom()
        index = 0
        height = self.get_height()
        full = False
        for i in range(height):
            for _ in range(2 ** i):
                if len(self.get_path(arr[index])) != i + 1:
                    return False
                # determine completeness using nodes on height - 1 level
                if i == height - 1:
                    left = arr[index].get_left_node()
                    right = arr[index].get_right_node()
                    # when to return False
                    if full and (left is not None or right is not None):
                        return False
                    if left is None and right is not None:
                        return False
                    # when to change full
                    if left is None or right is None:
                        full = True
                index += 1
        return True

    def is_perfect(self):
        return len(self.get_tree_top_to_bottom()) == 2 ** (self.get_height() + 1) - 1

    def is_balanced(self) -> bool:
        return self._is_balanced_helper(self.get_root())

    def is_balanced_by_node(self, node: BinaryNode) -> bool:
        return self._is_balanced_helper(node)

    def _is_balanced_helper(self, node: BinaryNode) -> bool:
        if node is None or node.at_bottom():
            return True
        return self._is_balanced_helper(node.get_left_node()) and \
               self._is_balanced_helper(node.get_right_node()) and \
               abs(self.get_height_node(node.get_left_node()) - self.get_height_node(node.get_right_node())) <= 1

    def num_of_universal_value_trees(self):
        return BinaryTree._num_of_universal_value_trees_helper(self.get_root())[0]

    @staticmethod
    def _num_of_universal_value_trees_helper(currentNode: BinaryNode) -> List:
        if currentNode is None:
            return [0, True]
        currentBool = True
        lf = BinaryTree._num_of_universal_value_trees_helper(currentNode.get_left_node())
        rt = BinaryTree._num_of_universal_value_trees_helper(currentNode.get_right_node())
        if lf[1] is False or rt[1] is False:
            currentBool = False
        if currentNode.get_left_node() is not None and currentNode.get_left_node().get_data() != currentNode.get_data():
            currentBool = False
        if currentNode.get_right_node() is not None and \
                currentNode.get_right_node().get_data() != currentNode.get_data():
            currentBool = False
        return [lf[0] + rt[0] + 1, True] if currentBool else [lf[0] + rt[0], False]

    def num_of_semi_universal_value_trees(self):
        return BinaryTree._num_of_semi_universal_value_trees_helper(self.get_root())[0]

    @staticmethod
    def _num_of_semi_universal_value_trees_helper(currentNode: BinaryNode) -> List:
        if currentNode is None:
            return [0, True, set()]
        currentBool = True
        lf = BinaryTree._num_of_semi_universal_value_trees_helper(currentNode.get_left_node())
        rt = BinaryTree._num_of_semi_universal_value_trees_helper(currentNode.get_right_node())
        if lf[1] is False or rt[1] is False:
            currentBool = False
        currentSet = lf[2].union(rt[2]).union({currentNode.get_data()})
        if len(currentSet) > 2:
            currentBool = False
        return [lf[0] + rt[0] + 1, True, currentSet] if currentBool else [lf[0] + rt[0], False, currentSet]


class BinarySearchTree(BinaryTree):
    def __init__(self, root: BinaryNode = None, *args):
        super().__init__(root)
        for value in args:
            self.add_by_value(value)

    def add_by_value(self, value):
        if self.get_root() is None:
            self.set_root(BinaryNode(value))
        else:
            self.set_root(self.balance(self._add_by_value_helper(self.get_root(), value)))

    def _add_by_value_helper(self, currentNode: BinaryNode, value) -> BinaryNode:
        if value <= currentNode.get_data():
            if currentNode.get_left_node() is None:
                currentNode.set_roots(BinaryNode(value), currentNode.get_right_node())
                return currentNode
            else:
                bottomNode = self._add_by_value_helper(currentNode.get_left_node(), value)
                if not self.is_balanced_by_node(bottomNode):
                    currentNode.set_roots(self.balance(bottomNode), currentNode.get_right_node())
                return currentNode
        else:
            if currentNode.get_right_node() is None:
                currentNode.set_roots(currentNode.get_left_node(), BinaryNode(value))
                return currentNode
            else:
                bottomNode = self._add_by_value_helper(currentNode.get_right_node(), value)
                if not self.is_balanced_by_node(bottomNode):
                    currentNode.set_roots(currentNode.get_left_node(), self.balance(bottomNode))
                return currentNode

    # return None if value not found
    def search(self, value) -> BinaryNode:
        return self._search_helper(self.get_root(), value)

    def _search_helper(self, currentNode: BinaryNode, value) -> BinaryNode:
        if currentNode is None:
            return None
        elif currentNode.get_data() == value:
            return currentNode
        elif value < currentNode.get_data():
            return self._search_helper(currentNode.get_left_node(), value)
        else:
            return self._search_helper(currentNode.get_right_node(), value)

    @ staticmethod
    def left_shift(root: BinaryNode) -> BinaryNode:
        rootRight = root.get_right_node()
        root.set_roots(root.get_left_node(), rootRight.get_left_node())
        rootRight.set_roots(root, rootRight.get_right_node())
        return rootRight

    @ staticmethod
    def right_shift(root: BinaryNode) -> BinaryNode:
        rootLeft = root.get_left_node()
        root.set_roots(rootLeft.get_right_node(), root.get_right_node())
        rootLeft.set_roots(rootLeft.get_left_node(), root)
        return rootLeft

    @ staticmethod
    def left_right_shift(root: BinaryNode) -> BinaryNode:
        rootLeft = root.get_left_node()
        rootLeftRight = rootLeft.get_right_node()
        rootLeft.set_roots(rootLeft.get_left_node(), rootLeftRight.get_left_node())
        rootLeftRight.set_roots(rootLeft, rootLeftRight.get_right_node())
        root.set_roots(rootLeftRight, root.get_right_node())
        return BinarySearchTree.right_shift(root)

    @ staticmethod
    def right_left_shift(root: BinaryNode) -> BinaryNode:
        rootRight = root.get_right_node()
        rootRightLeft = rootRight.get_left_node()
        rootRight.set_roots(rootRightLeft.get_right_node(), rootRight.get_right_node())
        rootRightLeft.set_roots(rootRightLeft.get_left_node(), rootRight)
        root.set_roots(root.get_left_node(), rootRightLeft)
        return BinarySearchTree.left_shift(root)

    def balance(self, node: BinaryNode) -> BinaryNode:
        left = node.get_left_node()
        right = node.get_right_node()
        diff = self.get_height_node(left) - self.get_height_node(right)
        if abs(diff) <= 1:
            return node
        elif diff > 1:
            if self.get_height_node(left.get_left_node()) - self.get_height_node(left.get_right_node()) > 0:
                return BinarySearchTree.right_shift(node)
            else:
                return BinarySearchTree.left_right_shift(node)
        else:
            if self.get_height_node(right.get_left_node()) - self.get_height_node(right.get_right_node()) > 0:
                return BinarySearchTree.right_left_shift(node)
            else:
                return BinarySearchTree.left_shift(node)


n1, n2, n3, n4, n5, n6, n7, n8, n9 = BinaryNode(1), BinaryNode(2), BinaryNode(3), BinaryNode(4), BinaryNode(5), \
                                     BinaryNode(6), BinaryNode(7), BinaryNode(8), BinaryNode(9)

n1.set_roots(n2, n3)
n2.set_roots(n4, n6)
n3.set_roots(n7, None)
n4.set_roots(None, n5)
n7.set_roots(n8, n9)

t1 = BinaryTree(n1)
t1.print_tree_left_to_right()
t1.print_tree_top_to_bottom_recursion()
t1.print_tree_top_to_bottom()
print(t1.get_height())  # print 3
print(t1.get_sum())  # print 45
print(t1.num_of_nodes())  # print 9
print(t1.get_depth(n1))  # print 0
print(t1.get_depth(n9))  # print 3
print([node.get_data() if node is not None else node for node in t1.get_path(n5)])  # print [1, 2, 4, 5]
print(t1.is_sibling(n8, n9))  # print True
print(t1.is_sibling(n6, n7))  # print False
print()

t1.mirror()
t1.print_tree_left_to_right()
t1.print_tree_top_to_bottom_recursion()
t1.print_tree_top_to_bottom()
print(t1.get_height())

n11, n12, n13, n14, n15, n16, n17 = BinaryNode(0), BinaryNode(1), BinaryNode(0), BinaryNode(1), \
                                    BinaryNode(0), BinaryNode(1), BinaryNode(1)
n11.set_roots(n12, n13)
n13.set_roots(n14, n15)
n14.set_roots(n16, n17)
t2 = BinaryTree(n11)
print(t2.num_of_universal_value_trees())  # print 5
print(t2.num_of_semi_universal_value_trees())  # print 7 which is the num of nodes

n21, n22, n23, n24, n25, n26, n27, n28, n29, n20 = BinaryNode(0), BinaryNode(0), BinaryNode(0), BinaryNode(0), \
                                                   BinaryNode(0), BinaryNode(0), BinaryNode(0), BinaryNode(0), \
                                                   BinaryNode(0), BinaryNode(0)
n21.set_roots(n22, n23)
n22.set_roots(n24, n25)
n25.set_roots(n26, n27)
n23.set_roots(n28, n29)
n29.set_roots(None, n20)
t3 = BinaryTree(n21)
print(t3.num_of_universal_value_trees())  # print 10
print(t3.num_of_semi_universal_value_trees())  # print 10 which is the num of nodes

n31, n32, n33, n34, n35, n36, n37, n38 = BinaryNode(2), BinaryNode(2), BinaryNode(1), BinaryNode(1), \
                                         BinaryNode(2), BinaryNode(1), BinaryNode(2), BinaryNode(1)
n39 = BinaryNode(1, n31, n32)
n40 = BinaryNode(2, n33, n34)
n41 = BinaryNode(2, n35, n36)
n42 = BinaryNode(1, n37, n38)
n43 = BinaryNode(2, n39, n40)
n44 = BinaryNode(1, n41, n42)
n45 = BinaryNode(3, n43, n44)
t4 = BinaryTree(n45)
print(t4.num_of_universal_value_trees())  # print 8 which is the num of bottom nodes
print(t4.num_of_semi_universal_value_trees())  # print 14 which is the num of nodes - 1 (the root)
print()

n01, n02, n03, n04, n05, n06, n07, n08, n111 = BinaryNode(1), BinaryNode(2), BinaryNode(3), BinaryNode(4), \
                                         BinaryNode(5), BinaryNode(6), BinaryNode(7), BinaryNode(8), BinaryNode(111)
n09 = BinaryNode(9, n01, n02)
n010 = BinaryNode(10, n03, n04)
n011 = BinaryNode(11, n09, n010)
t5 = BinaryTree(n011)
print(t5.is_complete())  # True
n01.set_roots(None, n05)
print(t5.is_complete())  # False
n01.set_roots(n05, None)
print(t5.is_complete())  # True
n01.set_roots(n05, n06)
print(t5.is_complete())  # True
n02.set_roots(None, n07)
print(t5.is_complete())  # False
n02.set_roots(n07, None)
print(t5.is_complete())  # True
n04.set_roots(n08, n111)
print(t5.is_complete())  # False
print()

n01, n02, n03, n04, n05, n06, n07, n08, n111 = BinaryNode(1), BinaryNode(2), BinaryNode(3), BinaryNode(4), \
                                         BinaryNode(5), BinaryNode(6), BinaryNode(7), BinaryNode(8), BinaryNode(111)
n09 = BinaryNode(9, n01, n02)
n010 = BinaryNode(10, n03, n04)
n011 = BinaryNode(11, n09, n010)
t6 = BinaryTree(n011)
print(t6.is_balanced())  # True
n01.set_roots(n05, None)
print(t6.is_balanced())  # True
n05.set_roots(n06, None)
print(t6.is_balanced())  # False
n01.set_roots(n05, n111)
n02.set_roots(n07, None)
n03.set_roots(n08, None)
print(t6.is_balanced())  # True
n03.set_roots(BinaryNode(0, n08), None)
print(t6.is_balanced())  # False
n04.set_roots(BinaryNode(-1), None)
print(t6.is_balanced())  # False
n03.set_roots(BinaryNode(0, n08), BinaryNode(-2))
print(t6.is_balanced())  # True
print()

bst1 = BinarySearchTree(None, 12, 6, 18, 3, 9, 15, 21)
bst1.print_tree_top_to_bottom()
bst1.print_tree_left_to_right()
print([val.get_data() for val in bst1.get_path(bst1.search(3))])
bst1.add_by_value(14)
print([val.get_data() for val in bst1.get_path(bst1.search(14))])
bst1.add_by_value(13)
print([val.get_data() for val in bst1.get_path(bst1.search(13))])
bst1.print_tree_top_to_bottom()
bst1.add_by_value(16)
print([val.get_data() for val in bst1.get_path(bst1.search(16))])
bst1.print_tree_top_to_bottom()
bst1.add_by_value(19)
print([val.get_data() for val in bst1.get_path(bst1.search(19))])
bst1.print_tree_top_to_bottom()
