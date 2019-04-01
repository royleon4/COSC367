binary_number([0, b, 0]).
binary_number([0, b, 1]).
binary_number([0, b, 1, A|B]) :- is_binary(A), binary_number([0, b, 1|B]).
is_binary(A):- A is 1; A is 0.
