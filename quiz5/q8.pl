remove(_, [], []).
remove(X, [X|T], L):-
	remove(X, T, L), !.
remove(X, [H|T], [H|L]) :-
	remove(X, T, L).