from typing import Optional
from src.treap import Node


def search(node: Node, key: str) -> Optional[Node]:
    if key is None or node is None:
        return None
    if key == node.key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


