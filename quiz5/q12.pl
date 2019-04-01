inside(Min,Max,X):-
	Min =< Max,
	X = Min.
inside(Min, Max, X):-
	Min < Max,
	Next is Min + 1,
	inside(Next, Max, X).