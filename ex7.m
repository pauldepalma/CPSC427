#done the old fashion way

dataMatrix = csvread('ex6Data.mat');
paramMatrix = csvread('ex6Param.mat');

dimenDat = size(dataMatrix);
dimenPar = size(paramMatrix);
numRows = dimenDat(1);
pred = [];
for i = 1:numRows
  tmp = dataMatrix(i,2) * paramMatrix(1,2);
  tmp = tmp + dataMatrix(i,1) * paramMatrix(1,1);
  pred = [pred;tmp];
end

pred