from pythonalgos.search_tree import SearchTree, SearchTreeNode

"""
              6
             / \
            4   7
           / \   \
          2   5   8
         / \
        1   3
"""
def createSearchTree():
    h = SearchTreeNode(data=3)
    g = SearchTreeNode(data=1)
    f = SearchTreeNode(data=8)
    e = SearchTreeNode(data=5)
    d = SearchTreeNode(data=2, left=g, right=h)
    c = SearchTreeNode(data=7, right=f)
    b = SearchTreeNode(data=4, left=d, right=e)
    root = SearchTreeNode(data=6, left=b, right=c)
    return [SearchTree(root=root), e]

"""
              6
             / \
            4   7
           / \   \
          3   5   8
         / \
        1   2
"""
def createBadSearchTree():
    h = SearchTreeNode(data=2)
    g = SearchTreeNode(data=1)
    f = SearchTreeNode(data=8)
    e = SearchTreeNode(data=5)
    d = SearchTreeNode(data=3, left=g, right=h)
    c = SearchTreeNode(data=7, right=f)
    b = SearchTreeNode(data=4, left=d, right=e)
    root = SearchTreeNode(data=6, left=b, right=c)
    return [SearchTree(root=root), e]

def test_search_found():
    t, node5 = createSearchTree()
    assert t.search(t.root, 5) == node5

def test_search_notfound():
    t, node5 = createSearchTree()
    assert t.search(t.root, 20) is None

def test_insert_basic():
    t, _ = createSearchTree()
    t.insert(11)
    assert t.to_string(t.root) == \
"""
6[4,7]
4[2,5]
2[1,3]
1[ , ]
3[ , ]
5[ , ]
7[ ,8]
8[ ,11]
11[ , ]"""

def test_valid():
    t, _ = createSearchTree()
    assert t.is_valid(t.root) is True

def test_not_valid():
    t, _ = createBadSearchTree()
    assert t.is_valid(t.root) is False


