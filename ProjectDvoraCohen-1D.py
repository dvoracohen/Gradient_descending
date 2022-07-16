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
from scipy.optimize import curve_fit


#  Question 1D - Start #
#define the given data in np.array
x = np.array([-5.,-4.5,-4.,-3.5,-3.,-2.5,-2.,-1.5,-1.,-0.5,0.,0.5,1.,1.5,2.,2.5,3.,3.5,4.,4.5,5.]) 
y = np.array([-2.16498306,-1.53726731,1.67075645,2.47647932,4.49579917,1.14600963,0.15938811,-3.09848048,-3.67902427,-1.84892687,-0.11705947,3.14778203,4.26365256,2.49120585,0.55300516,-2.105836,-2.68898773,-2.39982575,-0.50261972,1.40235643,2.15371399])

"""
function curvefit 
will run the previous model using the curve fit instead of the 
gradient descending 
The-model is 𝑓(𝑥)= 𝑎𝑥+𝑏
"""
def curvefit(x,y):
    
    #print the data in graph
    plt.scatter(x, y)
          

    constants = curve_fit(logarithmic, x, y)
    a_fit = constants[0][0]
    b_fit = constants[0][1]

    fit = []
    for i in x:
        fit.append(logarithmic(i, a_fit, b_fit))

    plt.plot(x, fit) 
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Python Curve Fit")
    plt.show()       
    print ("a {}, b {}".format(a_fit,b_fit))
   

# Linear equation: y = a*sin(x*b)
def logarithmic(x, a, b):
	return a * np.sin(b*x) 
   
  

curvefit(x,y)

#  Question 1D - End #



