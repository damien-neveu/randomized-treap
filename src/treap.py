from __future__ import annotations


class Node:
    def __init__(self, key: str, priority: float):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self, n: Node) -> None:
        self.left = n
        if n is not None:
            n.parent = self

    def set_right(self, n: Node) -> None:
        self.right = n
        if n is not None:
            n.parent = self


class Treap:
    def __init__(self, root: Node = None):
        self.root = root

    def insert(self, key: str, priority: float) -> None:
        pass
