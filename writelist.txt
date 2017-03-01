writelist([]).
writelist([H|T]) :- write(H), nl, writelist(T).

