%Knight's Tour, keeping visited squares in a list 

mem(X,[X|_]).
mem(X,[_|T]) :- mem(X, T).



path(Start,Goal) :- path1(Start,Goal,[Start|[]]).
path1(Z,Z,[_|_]).  %final argument is not used
path1(Start,Goal,List) :- 
		  move(Start,W),
                  not(mem(W,List)),
                  path1(W, Goal, [W|List]), !.  %push W on visited list
                                                %quit when path1 succeeds


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
