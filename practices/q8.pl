

postorder(leaf(A), [A]).

postorder(tree(T1, Left, Right), Ans):-
	
	postorder(Left, T2),
	postorder(Right, T3),
	append(T2, T3, T),
	append(T, [T1], Ans).