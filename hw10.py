
######################
#### Trees ####
######################

class Tree:
    def __init__(self, value, branches=()):
        self.value = value
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.value, branches_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.value) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def is_leaf(self):
        return not self.branches



def leaves(t):
    """Returns a list of all the entries of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"


def path(t, item):
    """
    >>> t = Tree(9, [Tree(7, [Tree(3), Tree(2)]), Tree(5)])
    >>> path(t, 2)
    [9, 7, 2]
    >>> path(t, 5)
    [9, 5]
    >>> path(t, 8)
    []
    """
    "*** YOUR CODE HERE ***"


def find_level(t, level):
    """
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> find_level(t, 2)
    [4, 5, 7]
    >>> find_level(t, 1)
    [2, 6]
    >>> find_level(t, 5)
    []
    """
    "*** YOUR CODE HERE ***"



