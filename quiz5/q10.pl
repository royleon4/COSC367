merge([], [], []).
merge(T, [], T).
merge([], T, T).
merge([X|L1], [Y|L2], [X|L3]):-
	X =< Y,
	merge(L1, [Y|L2], L3).

merge([X|L1], [Y|L2], [Y|L3]):-
	merge([X|L1], L2, L3).