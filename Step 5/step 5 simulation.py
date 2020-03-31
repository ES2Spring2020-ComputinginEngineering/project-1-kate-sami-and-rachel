##################
# step 5 simulation.py
# Sami Rothstein, Kate Wujciak, Rachel Moore
# This script calculates and plots angular acceleration, velocity,
# and position as a function of time. It also calculates the period based
# on theta. The length vs. period is graphed.
#################

# Import Statements
import numpy as np
import matplotlib.pyplot as plt
import statistics
import scipy.signal as sig

#Initial Conditions
vel = np.array([0])
acc = np.array([0])
theta = [np.pi/2]
time = np.linspace(0,20,num=10000)
length = [8.75,11,13,15,17]
avgT=np.array([])

#Function Definitions

def update_system(acc,theta,vel,l):
# This function takes 4 parameters: acceleration, theta (angular position),
# velocity, and length of pendulum. This function takes initial conditions
# and determines the next position, velocity, and acceleration using
# Euler's Method. It returns the new position, velocity, and acceleration.
    accNext = -386.1*np.sin(theta)/l
#    gravity in in/s^2
    dt = .002 
#    time step in s
    velNext = vel+(accNext*dt)
#    in/s
    thetaNext = theta+(velNext*dt)
#    in.
    return thetaNext,velNext,accNext

def period(theta):
# This function takes one parameter: theta. It determines the period based
# on theta (its angular position). It returns the average period and a list
# of the periods.
    theta_pks, _ = sig.find_peaks(theta)
    time_val = time[theta_pks]
    period_L = []
    for i in range(len(time_val)-1):
        interval = time_val[i+1]-time_val[i]
        period_L.append(interval)
    avg_period = statistics.mean(period_L)
    return avg_period,period_L

def graph_time(acceleration,velocity,theta,time):
# This function takes four parameters: acceleration, velocity, theta,
# and time. It graphs Theta vs. Time, Velocity vs. Time, and Acceleration
# vs. Time. It is a void function.
    plt.subplot(4,1,1)
    plt.plot(time,theta)
    plt.xlabel('Time (s)')
    plt.ylabel('Theta (rad)')
    plt.title('Theta vs.Time')
    plt.show()

    plt.subplot(4,1,2)
    plt.plot(time,vel)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (in/s)')
    plt.title('Velocity vs.Time')
    plt.show()

    plt.subplot(4,1,3)
    plt.plot(time,acceleration)
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (in/s^2)')
    plt.title('Acceleration vs.Time')
    plt.show()

def graph_period(length,avgT):
# This function takes two parameters: length of pendulum and average period
# (array not single value). This function graphs period as a function of
# length. It is a void function.
    plt.plot(length,avgT,'.')
    plt.ylabel('Period (s)')
    plt.xlabel('Length (in.)')
    plt.title('Length vs. Period')
    plt.show()


#Main Script
for x in length:
    i = 1
    vel = np.array([0])
    acc = np.array([0])
    theta = [np.pi/2]
    while i < len(time):
        thetaNext,velNext, accNext = update_system(acc[i-1],theta[i-1],vel[i-1],x)
        theta = np.append(theta, thetaNext)
        vel = np.append(vel, velNext)
        acc = np.append(acc, accNext)
        i +=1

    avg_period,period_L = period(acc)
    avgT = np.append(avgT,avg_period)
    graph_time(acc,vel,theta,time)
    
graph_period(length,avgT)
