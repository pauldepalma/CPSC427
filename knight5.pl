%stops after first goal.  


path(Start, Goal) :- empty(EmptyBeen), 
		     push(Start,EmptyBeen,Been),
                     path1(Start, Goal, Been).

path1(Goal, Goal, Been) :- 
    nl,
    nl,
    write('Solution is: '),
    nl,
    display_r(Been).
path1(Start, Goal, Been) :- 
    move(Start, Next),
    not(member_st(Next, Been)),
    push(Next, Been, Newbeen),
    path1(Next, Goal, Newbeen), !.


move(1,6).
move(1,8).
move(2,7).
move(2,9).
move(3,4).
move(3,8).
move(4,3).
move(4,9).
move(6,1).
move(6,7).
move(7,2).
move(7,6).
move(8,1).
move(8,3).
move(9,2).
move(9,4).

not(P) :-
 P,!,fail
 ;
 true.

mem(Elt,[Elt|_]).
mem(Elt,[_|Tail]) :- mem(Elt,Tail).


empty([]).
push(Top, Stack, [Top|Stack]).
pop(Top, Stack, [Top|Stack]).
member_st(Elt, Stack) :- mem(Elt,Stack).
display_r(Stack) :- empty(Stack).
display_r(Stack) :- pop(Top, Rest, Stack),
                    display_r(Rest),
                    write(Top),
                    nl.
                    
