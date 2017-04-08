%farmer, dog, goat, cabbage
%moving from west to east 
go :- path(st(w,w,w,w),st(e,e,e,e)).

path(Start, Goal) :- empty(EmptyBeen), 
		     push(Start,EmptyBeen,Been),
                     path1(Start, Goal, Been).

path1(Goal, Goal, Been) :- 
    write('Solution is: '), nl, 
    writeR(Been).
path1(Start, Goal, Been) :- 
    mv(Start, Next),
    not(memberSt(Next, Been)),
    push(Next, Been, Newbeen),
    path1(Next, Goal, Newbeen).

%move predicates

%take the dog 				
mv(st(X,X,G,C), st(Y,Y,G,C)) :- opp(X,Y), not(unsafe(st(Y,Y,G,C))).
%take the goat
mv(st(X,D,X,C), st(Y,D,Y,C)) :- opp(X,Y), not(unsafe(st(Y,D,Y,C))).
%take the cabbage
mv(st(X,D,G,X), st(Y,D,G,Y)) :- opp(X,Y), not(unsafe(st(Y,D,G,Y))).
%return alone
mv(st(X,D,G,C), st(Y,D,G,C)) :- opp(X,Y), not(unsafe(st(Y,D,G,C))).

%unsafe if the dog and the goat are together without the farmer
unsafe(st(X,Y,Y,C)) :-opp(X,Y), writelist(['dog & goat, no farmer: ',X,Y,Y,C]),nl.

%unsafe if the goat and the cabbage are together without the farmer
unsafe(st(X,W,Y,Y)):-opp(X,Y),writelist(['goat & cabbage,no farmer: ',X,W,Y,Y]),nl.

opp(e,w).
opp(w,e).


%stack
empty([]).
push(Top, Stack, [Top|Stack]).
pop(Top, Stack, [Top|Stack]).
memberSt(Elt, Stack) :- mem(Elt,Stack).
writeR(Stack) :- empty(Stack).
writeR(Stack) :- pop(Top, Rest, Stack),
                 writeR(Rest),
                    write(Top),
                    nl.

%membership in a list that is used by stack
mem(Elt,[Elt|_]).
mem(Elt,[_|Tail]) :- mem(Elt,Tail).

%write out a list
writelist([]).
writelist([H|T]) :- write(H), writelist(T).

