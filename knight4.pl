%Knight's Tour using queue to display path from start to goal

path(Start,Goal) :-
    empty(Empty_been),
    enqueue(Start,Empty_been,Been),
    path1(Start,Goal,Been).
path1(Goal, Goal, Been) :- 
    write('Solution is: '),
    nl,
    writeQ(Been).
path1(Start, Goal, Been) :- 
    move(Start, Next),
    not(memberQ(Next, Been)),
    enqueue(Next, Been, New_been),
    path1(Next, Goal, New_been).


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


empty([]).
enqueue(Elt,[],[Elt]).
enqueue(Elt,[H|T],[H|Tnew]) :- enqueue(Elt,T,Tnew).
serve(Elt,Queue,[Elt|Queue]).
memberQ(Elt, Queue) :- mem(Elt, Queue).
writeQ(Queue) :- empty(Queue).
writeQ(Queue) :- serve(Top, Rest, Queue),
		 write(Top),
		 nl,
		 writeQ(Rest).
		 

mem(Elt,[Elt|_]).
mem(Elt,[_|Tail]) :- mem(Elt,Tail).
