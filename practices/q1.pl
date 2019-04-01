product([], 1).
product([A|B], X) :- product(B, X1), X is A * X1 .