from itertools import *
from math import *

def conflict_count(array):
    conflict = 0
    for col, row in enumerate(array):
        for rcol, rrow in enumerate(array[col+1:]):
            if abs(rcol+col+1 - col) == abs(rrow - row):
                conflict += 1
        
    return conflict
    
#print(conflict_count((1, 2, 3)))
#print(conflict_count((1, 2, 3, 4, 5, 6, 7, 8)))
#print(conflict_count((2, 3, 1, 4)))


def neighbours(array):
    neighbours = []
    for change in combinations(array, 2):
        neighbour = list(array)
        x = neighbour.index(change[0])
        y = neighbour.index(change[1])

        neighbour[x], neighbour[y] = array[y], array[x]
        neighbours.append(tuple(neighbour))

    return neighbours
    
    
#print(sorted(neighbours((1, 3, 2))))

def greedy_descent(assignment):
    while True:
        conflicts = conflict_count(assignment)
        print("Assignment:", assignment, "Number of conflicts:", conflicts)

        if conflicts == 0:
            print("A solution is found.")
            return 0

        n = sorted(neighbours(assignment))
        assignment = min(n, key=lambda neighbour: conflict_count(neighbour))
        new_conflicts = conflict_count(assignment)

        if new_conflicts >= conflicts:
            print("A local minimum is reached.")
            return 1

#greedy_descent((1, 2, 3, 4, 5, 6))
#greedy_descent((6, 5, 3, 4, 2, 1))
#greedy_descent((2, 1, 3, 4, 6, 5))
#greedy_descent((1,))

#greedy_descent(tuple(range(1, 11)))

import random

def random_restart(n):
    random.seed(0) # seeding so that the results can be replicated.
    assignment = list(range(1, n+1))
    while not greedy_descent(tuple(assignment)):
        random.shuffle(assignment)

#random_restart(13)

def learn_perceptron(weights, bias, training_examples, learning_rate, 
                     max_epochs):
    for epoch in range(1, max_epochs + 1):
        #print("-" * 20, "epoch:", epoch, 20 * "-")
        #print("weights: ", weights)
        #print("bias: ", bias)
        seen_error = False
        for input, target in training_examples:
            a = sum(map(lambda x, y: x*y, input, weights)) + bias
            
            output = 1 if a >= 0 else 0
            #print("input: {} output: {} target: {}".format(
               #input, output, target))
            if output != target:
                seen_error = True
                # Now update the weights and bias
                weights = list(map(lambda x, y: x + learning_rate * y * (target - output), weights, input))
                bias += learning_rate * (target - output)
                #print("updating the weights and bias to: ", weights, bias)

        if not seen_error:
            def perceptron(input_vector):
                a = sum(map(lambda x, y: x*y, input_vector, weights)) + bias
                output = 1 if a >= 0 else 0
                return output
            return perceptron

# From the lecture notes
weights = [1, 1]
bias = -2
learning_rate = 0.5
examples = [
    ((0, 4), 0),
  ((-2, 1), 1),
  ((3, 5), 0),
  ((1, 1), 1),
]
max_epochs = 50

classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
if not classifier:
    print("No model could be learnt.")
else:
    print(classifier((0,4)))
    print(classifier((-2,1)))
    print(classifier((3,5)))
    print(classifier((1,1)))
    print(classifier((4,4)))
    print(classifier((-3,6)))
    print(classifier((3,-1)))
    
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
        ((0, 0), 0),
      ((0, 1), 1),
      ((1, 0), 1),
      ((1, 1), 0),
    ]
    max_epochs = 50
    
    classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
    if not classifier:
        print("No model could be learnt.")
    else:
        print(classifier((0,0)))
        print(classifier((0,1)))
        print(classifier((1,0)))
        print(classifier((1,1)))
        print(classifier((2,2)))
        print(classifier((-3,-3)))
        print(classifier((3,-1)))