mem(Elt,[Elt|_]).
mem(Elt,[_|Tail]) :- mem(Elt,Tail).
