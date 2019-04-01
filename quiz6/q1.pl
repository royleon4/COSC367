


max_value(Tree):-
	min_value(Tree).

min_value(Tree):-
	max_value(Tree).

	
	
test([T]) :- writeln(T), writeln('one').
test([T|M]) :- 
	writeln(T),
	test(M).