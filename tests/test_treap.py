from src.treap import Node, Treap
from src.treap_ops import search


def test_init_node():
    key, prio = "abc", 0.1
    n = Node(key, prio)
    assert (key, prio) == (n.key, n.priority)
    assert n.parent is None
    assert n.left is None
    assert n.right is None


def test_search_successful():
    node = search(build_treap().root, "guava")
    assert node.key == "guava:q"
    assert node.priority == .6


def test_search_unsuccessful():
    node = search(build_treap().root, "bla bla")
    assert node is None


def build_treap() -> Treap:
    apple = Node("apple", .7)
    guava = Node("guava", .6)
    cherry = Node("cherry", .75)
    cherry.set_left(apple)
    cherry.set_right(guava)
    orange = Node("orange", .5)
    pineapple = Node("pineapple", .6)
    pineapple.set_left(orange)
    mango = Node("mango", .8)
    mango.set_left(cherry)
    mango.set_right(pineapple)
    return Treap(mango)
