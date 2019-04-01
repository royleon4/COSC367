from csp import *
import itertools

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    print(names, domains)
    for values in itertools.product(*domains):
        
        assignment = {x:v for x, v in zip(names, values)}
        print(assignment)
        if all(satisfies(assignment, c) for c in csp.constraints):
            yield assignment
            
            
simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })

solutions = sorted(str(sorted(solution.items())) for solution 
                   in generate_and_test(simple_csp))
print("\n".join(solutions))


crossword_puzzle = CSP( # from slide 14
    var_domains={
        # read across:
        'a1': set("ant,big,bus,car".split(',')),
        'a3': set("book,buys,hold,lane,year".split(',')),
        'a4': set("ant,big,bus,car,has".split(',')),
        # read down:
        'd1': set("book,buys,hold,lane,year".split(',')),
        'd2': set("ginger,search,symbol,syntax".split(',')),
        },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
        })

solution = next(iter(generate_and_test(crossword_puzzle)))

# printing the puzzle similar to the way it actually  looks 
pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
    solution['d1'], "", solution['d2'], fillvalue=" ")]
pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
print("\n".join(pretty_puzzle))

print()

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': set("bus has".split()),
        'a3': set("lane year".split()),
        'a4': set("ant car".split()),
        # read down:
        'd1': set("buys hold".split()),
        'd2': set("search syntax".split()),
        },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
        })

solution = next(iter(generate_and_test(crossword_puzzle)))
print(solution)

# printing the puzzle similar to the way it actually  looks 
pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
    solution['d1'], "", solution['d2'], fillvalue=" ")]
pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
print("\n".join(pretty_puzzle))

print(sorted(crossword_puzzle.var_domains['a1']))


print()

from csp import CSP
canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })

solution = next(iter(generate_and_test(canterbury_colouring)))
print(solution)