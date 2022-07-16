# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 18:51:39 2022
@author: Dvora Cohen
@ID: 015407190
"""
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm

#  Question 1A - Start #
#define the given data in np.array
x = np.array([-3.0,-2.0,0.0,1.0,3.0,4.0])
y = np.array([-1.5,2.0,0.7,5.0,3.5,7.5])
arrCost = []
arrIter = []
a_iterration = []
b_iterration = []
"""
function gradient_descent Iterator Finder
defind the iterations number, the len of the data array and the learning rate
Then each itteration wil find a line according to the cost, m-derived and b derived of the line
and calculate the cost.
The-model is 𝑓(𝑥)= 𝑎𝑥+𝑏
"""
def gradient_descent(x,y):
    #Define the default values randomly
    a_curr = b_curr = 0
    #define the number of itterations
    iterations = 110
    #define the learning rate
    learning_rate = 0.08
    n = len(x)
    #print the data in graph
    plt.scatter(x, y)
    
    for i in range(iterations):
        y_predicted = a_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        #print(cost)
        arrCost.append(cost)
        arrIter.append(i)
        a_iterration.append(a_curr)
        b_iterration.append(b_curr)
        ad = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        a_curr = a_curr - learning_rate * ad
        b_curr = b_curr - learning_rate * bd
        
        
    #print the line
    plt.plot(x,y_predicted,color='green')
    plt.show()
    #print the last found a,b and cost
    print ("a {}, b {}, cost {} iteration {}".format(a_curr,b_curr,cost, i))

    
    
def printCostvsIteration():
    plt.plot(arrIter,arrCost,color='red')
    plt.xlabel("Iterrations")
    plt.ylabel("E(sum)")

    
    
def d3dGraph():
    x = a_iterration
    y = b_iterration
    X,Y = np.meshgrid(x,y)
    print("X =",len(X), X.shape)
    print("X =",len(X), X.shape)
    #the b iterration on Y

    Z =  np.array(arrCost)
        
    print(Z)
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
        
    # Plot a 3D surface
    ax.plot_surface(X, Y, Z)
        
    plt.show()


gradient_descent(x,y)
printCostvsIteration()
d3dGraph()

#  Question 1A - End #



