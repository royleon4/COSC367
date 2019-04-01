acclen([],Acc,Acc).

acclen([_|L],OldAcc,Length):-
	NewAcc is OldAcc+1,
	acclen(L,NewAcc,Length).
	
length(List,Length):-
	acclen(List,0,Length).