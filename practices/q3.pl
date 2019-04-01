pair(c, g).
pair(a, t).
pair(g, c).
pair(t, a).

dna([],[]).
dna([A|B], [C|D]):-
	pair(A,C),
	dna(B,D).