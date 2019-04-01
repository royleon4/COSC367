
preorder(leaf(A), [A]).
preorder(tree(A, leaf(B), leaf(C)), [A,B,C]).

preorder(tree(T1, Left, Right), [T1|T]):-
	append(T2, T3, T),
	preorder(Left, T2),
	preorder(Right, T3).