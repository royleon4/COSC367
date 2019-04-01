rle([],[]).
rle([A|T],[(A, N)]):-
	N is N+1,
	rle(T, [(A, N)]).