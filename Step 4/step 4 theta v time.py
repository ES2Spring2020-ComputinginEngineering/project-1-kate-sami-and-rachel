##################
# step 4 theta v time.py
# Sami Rothstein, Kate Wujciak, Rachel Moore
# This script plots theta as a function of time. The angular position
# (theta) is calculated from the accelerations for each length.
# The average period of each length is calculated from the accelerations
# then plotted over length.
#################

# Import Statements
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import statistics

# Global Variables
array = np.loadtxt('8-75in.csv', delimiter=',')
array1 = np.loadtxt('11in.csv', delimiter=',')
array2 = np.loadtxt('13in.csv', delimiter=',')
array3 = np.loadtxt('15in.csv', delimiter=',')
array4 = np.loadtxt('17in.csv', delimiter=',')

acc_x = array[:,1]
acc_y = array[:,2]
acc_z = array[:,3]


# Function Definitions

def find_tilt_z(acc_x, acc_y, acc_z):
# This function takes three parameters: x-acceleration, y-acceleration, and
# z-acceleration. This function finds theta (tiltZ) in the z-direction based
# on the x and y accelerations. It returns tiltZ (theta).
    tiltZ=((np.arctan2(acc_z,(np.sqrt((acc_x**2)+(acc_y**2)))))*180)/(np.pi)
    return tiltZ

def period(array_L):
# This function takes one parameter: array_L. This is the file for the
# times and accelerations for each length. It is an array that has the
# times associated with the accelerations for each axis. This function
# finds the peaks on the acceleration vs. time graphs and finds the
# time difference between them (period). It then determines the average
# period for the given length (based on accelerations). It returns the
# average period.
    y = array_L[:,1]
    time_pks = array_L[:,0]
    y_filt = sig.medfilt(y)
    y_filt_pks, _ = sig.find_peaks(y_filt)
    time_val = time_pks[y_filt_pks]
    period_L = []
    for i in range(len(time_val)-1):
        interval = time_val[i+1]-time_val[i]
        period_L.append(interval)
    avg_period = statistics.mean(period_L)
    return avg_period


# Main Script

#8.75 in theta v time
fig, (ax4) = plt.subplots(1, figsize=[10,8], sharex=True)
x1 = array[:,0]
y1 = find_tilt_z(acc_x, acc_y,acc_z)
ax4.plot(x1, y1, "#ff7f0e")
ax4.set_title('Theta vs Time (8.75 in)')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()




#11 in theta v time
fig1, (ax4) = plt.subplots(1, figsize=[10,8], sharex=True)
acc_x = array1[:,1]
acc_y = array1[:,2]
acc_z = array1[:,3]
x2 = array1[:,0]
y2 = find_tilt_z(acc_x, acc_y,acc_z)
ax4.plot(x2, y2, "#ff7f0e")
ax4.set_title('Theta vs Time (11 in)')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

#13 in theta v time
fig2, (ax4) = plt.subplots(1, figsize=[10,8], sharex=True)
acc_x = array2[:,1]
acc_y = array2[:,2]
acc_z = array2[:,3]
x3 = array2[:,0]
y3 = find_tilt_z(acc_x, acc_y,acc_z)
ax4.plot(x3, y3, "#ff7f0e")
ax4.set_title('Theta vs Time (13 in)')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

#15 in theta v time
fig3, (ax4) = plt.subplots(1, figsize=[10,8], sharex=True)
acc_x = array3[:,1]
acc_y = array3[:,2]
acc_z = array3[:,3]
x4 = array2[:,0]
y4 = find_tilt_z(acc_x, acc_y,acc_z)
ax4.plot(x3, y3, "#ff7f0e")
ax4.set_title('Theta vs Time (15 in)')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

#17in theta v time
fig4, (ax4) = plt.subplots(1, figsize=[10,8], sharex=True)
acc_x = array4[:,1]
acc_y = array4[:,2]
acc_z = array4[:,3]
x5 = array2[:,0]
y5 = find_tilt_z(acc_x, acc_y,acc_z)
ax4.plot(x3, y3, "#ff7f0e")
ax4.set_title('Theta vs Time (17 in)')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

##################################


#8.75in with peaks
fig, (ax4) = plt.subplots(1, figsize=[10,8], sharex=True)
time = array[:,0]
y = array[:,1]
y_filt = sig.medfilt(y)
y_filt_pks, _ = sig.find_peaks(y_filt[:-50])
plt.plot(time[:-50], y[:-50], 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
plt.title('8.75 with peaks')
plt.xlabel('Time (s)')
plt.ylabel('X Acc (m/s^2)')
plt.show()


# Length vs. Period Graph
length = [8.75,11,13,15,17]
period = [period(array),period(array1),period(array2),period(array3),period(array4)]
plt.plot(length,period,'o')
plt.title('Length vs Period')
plt.xlabel('Length (in)')
plt.ylabel('Period (ms)')

#
#print(period(array))
#print(period(array1))
#print(period(array2))
#print(period(array3))
#print(period(array4))








