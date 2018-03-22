#Another way to load and save data
#Create a file, one row to a line, columns separated by commas
#1,2,3
#4,5,6
#7,8,9


load ex8A.mat
load ex8B.mat
A = ex8A;
B = ex8B';

P = A * B;

save ex8P.mat P