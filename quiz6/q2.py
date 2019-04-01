from math import *

def max_value(tree, alpha=float('-inf'), beta=float('inf')):
    """ """
    if isinstance(tree, int):
        return tree
    v = -inf
    for i, item in enumerate(tree):
        v = max(v, min_value(item, alpha, beta))
        if v >= beta:
            if tree[i+1:]:
                print("Pruning:", ", ".join(map(str, tree[i+1:])))            
            return v
        alpha = max(alpha, v)
    return v    


def min_value(tree, alpha=float('-inf'), beta=float('inf')):
    """ """
    if isinstance(tree, int):
        return tree
    v = inf
    for i, item in enumerate(tree):
        v = min(v, max_value(item, alpha, beta))
        if v <= alpha:
            if tree[i+1:]:
                print("Pruning:", ", ".join(map(str, tree[i+1:])))            
            return v
        beta = min(beta, v)
    return v    

tree = [[1, 2], [3, 4]]
print("Game tree:", tree)
print("Computing the utility of the root as a max node...")
print("Root utility for maximiser:", max_value(tree))
print("Computing the utility of the root as a min node....")
print("Root utility for minimiser:", min_value(tree))
print("\n")
# changing the order of children affects
# what is being pruned.
tree = [[3, 4], [1, 2]]
print("Game tree:", tree)
print("Computing the utility of the root as a max node...")
print("Root utility for maximiser:", max_value(tree))
print("Computing the utility of the root as a min node....")
print("Root utility for minimiser:", min_value(tree))

tree = [[2, 3, 4], [1, 100, -100]]
print("Game tree:", tree)
print("Computing the utility of the root as a max node...")
print("Root utility for maximiser:", max_value(tree))
print("Computing the utility of the root as a min node....")
print("Root utility for minimiser:", min_value(tree))

# From the lecture notes
tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
print("Game tree:", tree)
print("Computing the utility of the root as a max node...")
print("Root utility for maximiser:", max_value(tree))
print("Computing the utility of the root as a min node....")
print("Root utility for minimiser:", min_value(tree))

tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]
print("Game tree:", tree)
print("Computing the utility of the root as a max node...")
print("Root utility for maximiser:", max_value(tree))
print("Computing the utility of the root as a min node....")
print("Root utility for minimiser:", min_value(tree))

tree = [3, [[1, 2], [[4, 5], [6, 7]]], 8]
print("Game tree:", tree)
print("Computing the utility of the root as a max node...")
print("Root utility for maximiser:", max_value(tree))
print("Computing the utility of the root as a min node....")
print("Root utility for minimiser:", min_value(tree))