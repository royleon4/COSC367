twice([],[]).
twice([A|B],[A|[A|C]]) :- twice(B,C).
