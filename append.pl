%app([a,b,c],[d,e,f],R).
app([],L2,L2).
app([H|T],L2,[H|Result]) :- app(T,L2, Result).
