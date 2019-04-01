import itertools, copy 
from csp import *

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x:v for x, v in zip(names, values)}
        if all(satisfies(assignment, c) for c in csp.constraints):
            yield assignment

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    tda = {(x, c) for c in csp.constraints for x in csp.var_domains}
    #print(tda)
    while tda:
        x, c = tda.pop()
        ys = list(scope(c) - {x})
        new_domain = set()
        for xval in csp.var_domains[x]: #COMPLETE:
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval)
                    break
        if csp.var_domains[x] != new_domain:
            csp.var_domains[x] = new_domain
            for cprime in set(csp.constraints) - {c}:
                if x in scope(c):
                    for z in scope(cprime):
                        if x != z:
                            tda.add((z, cprime))
    return csp


simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })

for i in generate_and_test(simple_csp):
    print(i)

csp = arc_consistent(simple_csp)
for var in sorted(csp.var_domains.keys()):
    print("{}: {}".format(var, sorted(csp.var_domains[var])))   
    
    
cryptic_puzzle = CSP(
    var_domains={x: set(range(0 if x != "f" else 1, 10)) for x in "twofur"},
    constraints={
        lambda t, w, o, f, u, r: len([t, w, o, f, u, r]) == len({t, w, o, f, u, r}),
        lambda o, r: (o + o) % 10 == r,
        lambda w, o, u: ((0 if o < 5 else 1) + w + w) % 10 == u,
        lambda t, w, o: ((0 if w < 5 else 1) + t + t) % 10 == o,
        lambda f: f == 1,
        lambda t: t + t >= 10
    }
)


new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['w']))