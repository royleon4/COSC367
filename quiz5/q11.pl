split_odd_even(List,Odd,Even):-odd(List,Odd,Even).

odd([H|T],[H|Odd],Even):-even(T,Odd,Even).
odd([],[],[]).

even([H|T],Odd,[H|Even]):-odd(T,Odd,Even).       
even([],[],[]).

merge([], [], []).
merge(T, [], T).
merge([], T, T).
merge([X|L1], [Y|L2], [X|L3]):-
	X =< Y,!,
	merge(L1, [Y|L2], L3).

merge([X|L1], [Y|L2], [Y|L3]):-
	merge([X|L1], L2, L3).

merge_sort([], []).
merge_sort([A], [A]).
merge_sort(L1, L2):-
	split_odd_even(L1,A,B),
	merge(A,B,L2),!.
	
	
	
