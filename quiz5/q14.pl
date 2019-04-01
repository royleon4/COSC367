inside(Min,Max,X):-
	Min =< Max,
	X = Min.
inside(Min, Max, X):-
	Min < Max,
	Next is Min + 1,
	inside(Next, Max, X).
	
	
py_triple(A, B, C) :- 
	A =\= 0,
	B =\= 0,
	C =\= 0,
	B > A,
	C > B,
	Sum is (A*A + B*B),
	C*C =:= Sum.
	
py_triple(A, B, C, Min, Max) :-
	inside(Min,Max,A),
	inside(Min,Max,B),
	inside(Min,Max,C),
	py_triple(A,B,C).
	
	
	
