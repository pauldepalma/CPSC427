/*
ex2.pl
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
ancestor(X,Z) :- parent(X,Y), ancestor(Y,Z).
