py_triple(A, B, C) :- 
	A =\= 0,
	B =\= 0,
	C =\= 0,
	B > A,
	C > B,
	Sum is (A*A + B*B),
	C*C =:= Sum.