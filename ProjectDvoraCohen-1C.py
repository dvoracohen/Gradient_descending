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
import math

#  Question 1C - Start #
#define the given data in np.array
x = np.array([-5.,-4.5,-4.,-3.5,-3.,-2.5,-2.,-1.5,-1.,-0.5,0.,0.5,1.,1.5,2.,2.5,3.,3.5,4.,4.5,5.]) 
y = np.array([-2.16498306,-1.53726731,1.67075645,2.47647932,4.49579917,1.14600963,0.15938811,-3.09848048,-3.67902427,-1.84892687,-0.11705947,3.14778203,4.26365256,2.49120585,0.55300516,-2.105836,-2.68898773,-2.39982575,-0.50261972,1.40235643,2.15371399])
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
    iterations = 376
    #define the learning rate
    learning_rate = 0.08
    n = len(x)
    #print the data in graph
    plt.scatter(x, y)
    
    for i in range(iterations):
        y_predicted = a_curr * np.sin(b_curr*x)
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
    #print("X =",len(X), X.shape)
    #print("X =",len(X), X.shape)
    #the b iterration on Y

    Z =  np.array(arrCost)
        
    #print(Z)
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
        
    # Plot a 3D surface
    ax.plot_surface(X, Y, Z)
        
    plt.show()


gradient_descent(x,y)
printCostvsIteration()
d3dGraph()

#  Question 1C - End #



