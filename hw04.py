######################
# Required Questions #
######################

def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"

def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"

def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"

def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"


def higher_order_lambdas():
    """
    Return a lambda function that takes in a multiplier and returns a lambda function that given an input will 
    return the input multiplied by the multiplier
    >>> hol = higher_order_lambdas()
    >>> doubles = hol(2)
    >>> doubles(3)
    6
    >>> hol = higher_order_lambdas()
    >>> triples = hol(3)
    >>> triples(4)
    12
    """
    "*** YOUR CODE HERE ***"

def lambda_curry2(fn):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    "*** YOUR CODE HERE ***"
    


def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> e = replace_all(d, 3, 'poof')
    >>> e == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    


def merge_dict(d1, d2):
    """Returns a dictionary that is the result of two dictionaries being merged together. 
    Dictionaries are merged by adding up their values. You can assume that the same keys 
    appear in both dictionaries.
    >>> data8 = {"midterms":1, "projects":3}
    >>> data100 = {"midterms":2, "projects":3}
    >>> combined_exams = merge_dict(data8, data100)
    >>> combined_exams
    {'midterms': 3, 'projects': 6}
    >>> sunday_orders = {"pizza": 3, "hot dogs": 2, "fries": 5}
    >>> monday_orders = {"pizza": 1, "hot dogs": 1, "fries": 8}
    >>> combined_orders = merge_dict(sunday_orders, monday_orders)
    >>> combined_orders
    {'pizza': 4, 'hot dogs': 3, 'fries': 13}
    """
    "*** YOUR CODE HERE ***"
    



