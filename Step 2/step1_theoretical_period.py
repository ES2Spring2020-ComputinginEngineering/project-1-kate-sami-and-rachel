#step1_theoretical_period.py
#Kate Wujciak, Sami Rothstein, Rachel Moore
#Project 1 Step 2
#--------------------------------------------

#import statements
import numpy as np
import math
import matplotlib.pyplot as plt

#global variables
length = np.array([8.75,11,13,15,17])


#Function Defintions
def find_period(length):
#This function takes one parameter, length of the pendulum.
#It finds the theoretical period of the pendulum in seconds based
#on the length of each pendulum. The period is in seconds.
#It is a void function.
    period = 2*(math.pi)*(np.sqrt(length/386.09))
    print(period)

#Main Script

#Period Graph
y = 2*(math.pi)*(np.sqrt(length/386.09))
x = length
plt.scatter(x, y)
plt.show
plt.title('Length vs. Period')
plt.xlabel('Length (in.)')
plt.ylabel('Period (sec.)')

find_period(length)

# We are assuming gravity is constant and that there is 
# no air resistance. The friction of the pendulum will
# give a longer than theoretical time.
