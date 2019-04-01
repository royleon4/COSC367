from math import *
def max_value(tree):
    """"""
    if isinstance(tree, int):
        return tree
    v = -inf
    for item in tree:
        v = max(v, min_value(item))
    return v

def min_value(tree):
    """"""
    if isinstance(tree, int):
        return tree
    v = inf
    for item in tree:
        v = min(v, max_value(item))
    return v







tree = 3
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [1, 2, 3]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [1, 2, [3]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[1, 2], [3]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[1, 2], [3, 4]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[2, 3, 4], [1, 100, -100]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

# From the lecture notes
tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))


tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[1, 4], [3, 5], [2]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))