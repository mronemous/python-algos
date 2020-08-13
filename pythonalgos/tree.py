from __future__ import annotations
from dataclasses import dataclass
from collections import deque


@dataclass
class TreeNode:
    data: str
    left: TreeNode = None
    right: TreeNode = None

    def to_string(self):
        result = "\n" + self.data + "["
        if self.left:
            result += self.left.data
        else:
            result += " "

        result += ","

        if self.right:
            result += self.right.data
        else:
            result += " "

        return result + "]"

@dataclass
class Tree:
    root: TreeNode

    def to_string(self, node: TreeNode) -> str:
        result = ""
        if node:
            result += node.to_string()
            result += self.to_string(node.left)
            result += self.to_string(node.right)

        return result

    """
    Depth first search methods
    """

    def traverse_inorder(self, node: TreeNode) -> [str]:
        result = []
        if node:
            result += self.traverse_inorder(node.left)
            result += node.data
            result += self.traverse_inorder(node.right)

        return result

    def traverse_preorder(self, node: TreeNode) -> [str]:
        result = []
        if node:
            result += node.data
            result += self.traverse_preorder(node.left)
            result += self.traverse_preorder(node.right)

        return result

    def traverse_postorder(self, node: TreeNode) -> [str]:
        result = []
        if node:
            result += self.traverse_postorder(node.left)
            result += self.traverse_postorder(node.right)
            result += node.data

        return result

    # Stack based versions
    def traverse_postorder_stack(self, root: TreeNode) -> [str]:
        result = []
        if root is None:
            return result
        s1 = [root]
        while s1:
            n = s1.pop()
            result.append(n.data)
            if n.left:
                s1.append(n.left)
            if n.right:
                s1.append(n.right)

        return result[::-1]

    def traverse_preorder_stack(self, root: TreeNode) -> [str]:
        result = []
        if root is None:
            return result
        s1 = [root]
        while s1:
            n = s1.pop()
            result.append(n.data)
            if n.right:
                s1.append(n.right)
            if n.left:
                s1.append(n.left)

        return result

    def traverse_inorder_stack(self, root: TreeNode) -> [str]:
        result = []
        if root is None:
            return result

        s = []
        current = root

        while current or s:

            if current:
                s.append(current)
                current = current.left
            else:
                current = s.pop()
                result.append(current.data)
                current = current.right

        return result

    """
    Breadth first traverses
    """
    def traverse_levelorder(self, root: TreeNode) -> [str]:
        result = []
        if root is None:
            return result

        queue = deque([root])
        while queue:
            n = queue.popleft()
            result.append(n.data)

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        return result

    def traverse_levelorder_reverse(self, root: TreeNode) -> [str]:
        result = []
        if root is None:
            return result

        queue = deque([root])
        while queue:
            n = queue.popleft()
            result.append(n.data)

            if n.right:
                queue.append(n.right)
            if n.left:
                queue.append(n.left)

        #could also append to a stack to provide this reversed output

        return result[::-1]

    def traverse_levelorder_split(self, root: TreeNode) -> [str]:
        result = []
        if root is None:
            return result

        queue = deque([root])
        while queue:

            level = []
            for i in range(0, len(queue)):
                n = queue.popleft()
                level.append(n.data)

                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            if len(level) > 0:
                result.append(level[:])
                level.clear()

        return result

    def height(self, root: TreeNode) -> int:
        result: int = 0
        left: int = 0
        right: int = 0

        if root is None:
            return result

        if root.left:
            left = self.height(root.left)

        if root.right:
            right = self.height(root.right)

        result = 1 + max(left, right)

        return result

    def size(self, root: TreeNode) -> int:
        result: int = 0

        if root is None:
            return result

        result += 1
        if root.left:
            result += self.size(root.left)

        if root.right:
            result += self.size(root.right)

        return result



