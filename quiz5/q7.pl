element([E|_], 0, E).

element([_|L], I, V):-
	element(L, I1, V),
	I is I1 + 1.
	
	
	
