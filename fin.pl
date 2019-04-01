mirror(leaf(X),leaf(X)).
mirror(tree(X1,Y1),tree(Y2,X2)) :- mirror(X1,X2), mirror(Y1,Y2).
