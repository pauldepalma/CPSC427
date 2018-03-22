matrixOut = rand(3,3);
csvwrite('ex5.mat',matrixOut);  #write out in CSV format

matrixIn = csvread('ex5.mat');  #read into matrix
disp(matrixIn) #display