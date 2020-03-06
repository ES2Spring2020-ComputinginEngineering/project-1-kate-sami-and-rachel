import numpy as np
import math


length = np.array([8.75,11,13,15,17])

def find_period(length):
    period = 2*(math.pi)*(np.sqrt(length/386.09))
    #period in seconds
    print(period)
find_period(length)
