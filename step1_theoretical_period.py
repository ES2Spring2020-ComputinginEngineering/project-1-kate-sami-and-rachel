#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:39:04 2020

@author: samirothstein
"""
#import statements
import numpy as np
import math
import matplotlib.pyplot as plt

#global variables
length = np.array([8.75,11,13,15,17])


#custom functions
def find_period(length):
#this function finds the period of the accelerations for each length
#takes one parameter length
#finds period by using the formula, and does this for each length
    period = 2*(math.pi)*(np.sqrt(length/386.09))
    #period in seconds
    print(period)


#period
y = 2*(math.pi)*(np.sqrt(length/386.09))
x = length
plt.scatter(x, y)
plt.show
plt.title('Length vs. Period')
plt.xlabel('Length (in.)')
plt.ylabel('Period (sec.)')

# We are assuming gravity is constant and that there is 
# no air resistance. The friction of the pendulum will
# give a longer than theoretical time.

find_period(length)