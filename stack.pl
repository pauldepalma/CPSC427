empty([]).
push(Top,Stack,[Top|Stack]).
pop(Top,Stack,[Top|Stack]).
isIn(Elt,Stack) :- mem(Elt,Stack).

write_s(Stack):- empty(Stack).
write_s(Stack):- pop(Top,Rest,Stack), write_s(Rest), write(Top), nl.
