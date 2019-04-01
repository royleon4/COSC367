fib(0, X).
fib(2, [0, 1]).
fib(N, T) :-
	Next is N - 2,
	fib(Next, [1, 1]),
	append([0, 1], [1], T),
	
	
fib(N, [A,B]):- 
	Sum is A + B,
	append([], [Sum], T),
	Next is N - 1,
	fib(Next, B|T).