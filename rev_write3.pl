rev_w3([]).
rev_w3([H|T]) :- rev_w3(T), write(H). 
