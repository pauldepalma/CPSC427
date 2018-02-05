/*
ex2.pl
Illustrates backtracking
*/

par(mateo,margarita).
par(mateo,livia).
par(mateo,lena).
sibling(Y,Z) :- par(X,Y), par(X,Z), Y \= Z. /* not (Y=Z)*/
