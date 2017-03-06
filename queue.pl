empty([]).
isin(Elt,Queue) :- mem(Elt,Queue).
dequeue(Top,Queue,[Top|Queue]).
enqueue(Elt,[],[Elt]).
enqueue(Elt,[H|T],[H|Tnew]) :- enqueue(Elt,T,Tnew).
