%Knight's Tour, keeping a global record of squares visited
path(Z,Z).
path(X,Y) :-
       assertz(been(X)),
       move(X,W),
       not(been(W)),
       assertz(been(W)),
       path(W,Y).
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
