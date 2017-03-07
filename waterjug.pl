/*
Water Jug
buckets(X,Y) where X is 4 gallon jug, Y is three gallon jug
to run: go(X,Y) 
X is the goal amount in the 4 gallon jug
Y is the goal amount in the 3 gallon jug
*/

go(X,Y) :- path(buckets(0,0),buckets(X,Y)).

path(Start,Goal) :- empty(Empty_been),
                    stack(Start,Empty_been,Been),
                    path1(Start,Goal,Been).

path1(Goal,Goal,Been) :- write('Solution is: '),
                         nl,
                         rev_pr_stack(Been).

path1(Start,Goal,Been) :-  mv(Start,Next),
                           not(memberSt(Next,Been)),
                           stack(Next,Been,New_been),
                           path1(Next,Goal,New_been).


/*If the four gallon jug is not full, fill it. */
mv(buckets(X,Y),buckets(4,Y)) :- X < 4.

/*If the three gallon jug is not full, fill it. */
mv(buckets(X,Y),buckets(X,3)) :- Y < 3.

/*If the four gallon jug is not empty, empty it. */
mv(buckets(X,Y),buckets(0,Y)) :- X > 0.

/*If the three gallon jug is not empty, empty it.*/
mv(buckets(X,Y),buckets(X,0)) :- Y > 0.

/*If the sum of the two jugs >= 4 and the three gallon jug is*/
/*not empty, fill the four gallon jug from the three gallon jug.*/
mv(buckets(X,Y),buckets(4,Y1)) :- (X + Y) >= 4, Y > 0, (Y1 is Y - (4 - X)).

/*if the sum of the two jugs >= 3 and the four gallon jug is not empty,*/
/*fill the three gallon jug from the four gallon jug.*/
mv(buckets(X,Y),buckets(X1,3)) :- (X + Y) >=3, X > 0, (X1 is X - (3 - Y)).

/*if the sum of the two jugs is <= 4 and the three gallon jug is not empty,*/
/*pour the three gallon jug into the four gallon jug.*/
mv(buckets(X,Y),buckets(X1,0)) :- (X + Y) =< 4, Y > 0, (X1 is X + Y).

/*If the sum of the two jugs is <= 3 and the four gallon jug is not empty,*/
/*pour the four gallon jug into the three gallon jug.*/
mv(buckets(X,Y),buckets(0,Y1)) :- (X + Y) =< 3, X > 0, (Y1 is X + Y).


/*stack operations*/
empty([]).
stack(Top,Stack,[Top|Stack]).
memberSt(Elt,Stack) :- mem(Elt,Stack).
rev_pr_stack(S) :- empty(S).
rev_pr_stack(S) :- stack(E,Rest,S),
                   rev_pr_stack(Rest),
                   write(E), nl.

/*member checking*/
mem(Elt,[Elt|_]).
mem(Elt,[_|Tail]) :- mem(Elt,Tail).


/*writing out a list*/

writelist([]).
writelist([H|T]) :- write(H), nl, writelist(T).


/* Backtrack
mv(buckets(X,Y),buckets(X,Y)) :- write('  backtrack from: '), 
                       nl,
                       write('Four Gallon (X) = '),
                       write(X),
                       nl,
                       write('Three Gallon (Y) = '),
                       write(Y),
                       nl,
                       fail.

*/
