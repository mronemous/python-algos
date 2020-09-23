from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SearchTreeNode:
    data: int
    left: SearchTreeNode = None
    right: SearchTreeNode = None

    def to_string(self):
        result = "\n" + str(self.data) + "["
        if self.left:
            result += str(self.left.data)
        else:
            result += " "

        result += ","

        if self.right:
            result += str(self.right.data)
        else:
            result += " "

        return str(result) + "]"


@dataclass
class SearchTree:
    root: SearchTreeNode

    def to_string(self, node: SearchTreeNode) -> str:
        result = ""
        if node:
            result += node.to_string()
            result += self.to_string(node.left)
            result += self.to_string(node.right)

        return result

    def search(self, root: SearchTreeNode, data: int) -> SearchTreeNode:
        found = None
        if root is None:
            return found

        if root.data == data:
            found = root
        elif data < root.data:
            if root.left:
                found = self.search(root.left, data)
        elif data > root.data:
            if root.right:
                found = self.search(root.right, data)

        return found

    def insert(self, data: int):
        if self.root is None:
            self.root = SearchTreeNode(data=data)
        else:
            self._insert(data, self.root)

    def _insert(self, data: int, node: SearchTreeNode):

        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = SearchTreeNode(data=data)
        elif data > node.data:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = SearchTreeNode(data=data)
        else:
            print("value already exists in tree")

    def is_valid(self, node: SearchTreeNode) -> bool:

        if node is None:
            return True

        is_left_valid = True
        is_right_valid = True
        if node.left:

            if node.data > node.left.data:
                is_left_valid = self.is_valid(node.left)
            else:
                is_left_valid = False

        if node.right:
            if node.data < node.right.data:
                is_right_valid = self.is_valid(node.right)
            else:
                is_right_valid = False

        return is_left_valid and is_right_valid
