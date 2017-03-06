len([],0).
len([_|T],L) :- len(T,l), L is l + 1.
