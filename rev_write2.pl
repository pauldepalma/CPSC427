rev_w2(L) :- rev(L,R).
rev(L,R) :- rev1(L, [], R).
rev1([], Temp, Temp).
rev1([H|T], Temp, R) :- rev1(T, [H|Temp],R), write(H). 
