
	
	
swap_ends(X,Y):-
    append([F|M],[L],X),
    append([L|M],[F],Y).
	
swap_ends2([X1|X2],[Y1|Y2]):-
    append([X1],X2,X),
    append([Y1],Y2,Y),
    append([F|M],[L],X),
    append([L|M],[F],Y).