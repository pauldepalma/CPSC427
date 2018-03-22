#Vectorized loop
#Htheta = theta + theta_one * x

dataMatrix = csvread('ex6Data.mat');
paramMatrix = csvread('ex6Param.mat');

predMatrix = dataMatrix * paramMatrix'
