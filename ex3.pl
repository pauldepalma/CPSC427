/*
ex3.pl
A more complex backtracking program with a recursive call 
*/
parent(marguerite,paul).
parent(eleanora,marguerite).
parent(anna,eleanora).
parent(ralph,paul).
parent(antonio,ralph).
parent(fabio,antonio).
parent(paul,katie).
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(Z,Y), ancestor(X,Z).

