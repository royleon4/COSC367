new_append([], L, L).
new_append([H|L1],L2,[H|L3]):-
    new_append(L1,L2,L3).
	
