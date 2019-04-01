/*
append([],L,L). 
append([H|T],L2,[H|L3])  :-  append(T,L2,L3).
	
prefix(P, L):-
	append(P,_,L).
	
suffix(S,L):-
	append(_,S,L).

	
swap_ends([Last,Fisrt], [Fisrt,Last]).


swap_ends([Last|[H|L1]],[L|L2]):- 
	swap_ends(L1,L2),
	print(L1).
*/
/*
swapfl(L,[]) :- False.

swapfl([X|Xs],List2) :- 
    append(T,[H],Xs),
    append([H|T],[X],List2).
*/


swap_ends([First1|Tail1], [First2|Tail2]):-
	reverse(Tail1, [Last1|Rest1]),
	reverse(Tail2, [Last2|Rest2]),
	First1 = Last2,
	Last1 = First2,
	Rest1 = Rest2.

