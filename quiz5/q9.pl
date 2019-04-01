split_odd_even(List,Odd,Even):-odd(List,Odd,Even).

odd([H|T],[H|Odd],Even):-even(T,Odd,Even).
odd([],[],[]).

even([H|T],Odd,[H|Even]):-odd(T,Odd,Even).       
even([],[],[]).