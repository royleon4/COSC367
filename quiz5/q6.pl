addone([], []).
addone([I|L1], [Sum|L2]):-
	addone(L1, L2),
	Sum is 1 + I.
