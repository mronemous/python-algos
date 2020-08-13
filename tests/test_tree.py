from pythonalgos.tree import Tree, TreeNode

"""

              A
             / \
            B   C
           / \   \
          D   E   F
         / \
        G   H

inorder ->G->D->H->B->E->A->C->F
preorder ->A->B->D->G->H->E->C->F
postorder ->G->H->D->E->B->F->C->A         
"""
def createTree():
    h = TreeNode(data="H")
    g = TreeNode(data="G")
    f = TreeNode(data="F")
    e = TreeNode(data="E")
    d = TreeNode(data="D", left=g, right=h)
    c = TreeNode(data="C", right=f)
    b = TreeNode(data="B", left=d, right=e)
    root = TreeNode(data="A", left=b, right=c)
    return Tree(root=root)

def test_traverse_inorder():
    t = createTree()
    assert t.traverse_inorder(t.root) == ['G', 'D', 'H', 'B', 'E', 'A', 'C', 'F']

def test_traverse_preorder():
    t = createTree()
    assert t.traverse_preorder(t.root) == ['A', 'B', 'D', 'G', 'H', 'E', 'C', 'F']

def test_traverse_postorder():
    t = createTree()
    assert t.traverse_postorder(t.root) == ['G', 'H', 'D', 'E', 'B', 'F', 'C', 'A']

def test_traverse_postorder_stack():
    t = createTree()
    assert t.traverse_postorder_stack(t.root) == ['G', 'H', 'D', 'E', 'B', 'F', 'C', 'A']

def test_traverse_preorder_stack():
    t = createTree()
    assert t.traverse_preorder_stack(t.root) == ['A', 'B', 'D', 'G', 'H', 'E', 'C', 'F']

def test_traverse_inorder_stack():
    t = createTree()
    assert t.traverse_inorder_stack(t.root) == ['G', 'D', 'H', 'B', 'E', 'A', 'C', 'F']


def test_to_string():
    t = createTree()
    assert t.to_string(t.root) == \
"""
A[B,C]
B[D,E]
D[G,H]
G[ , ]
H[ , ]
E[ , ]
C[ ,F]
F[ , ]"""

def traverse_levelorder():
    t = createTree()
    assert t.traverse_levelorder(t.root) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def test_traverse_levelorder_reverse():
    t = createTree()
    assert t.traverse_levelorder_reverse(t.root) == ['G', 'H', 'D', 'E', 'F', 'B', 'C', 'A']


def test_traverse_levelorder_split():
    t = createTree()
    assert t.traverse_levelorder_split(t.root) == [['A'], ['B', 'C'], ['D', 'E', 'F'], ['G', 'H']]

def test_tree_height():
    t = createTree()
    assert t.height(t.root) == 4

def test_tree_size():
    t = createTree()
    assert t.size(t.root) == 8

