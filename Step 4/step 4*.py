#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:51:32 2020

@author: samirothstein
"""
import numpy as np
import matplotlib.pyplot as plt
import math


array = np.loadtxt('8-75in.csv', delimiter=',')
array1 = np.loadtxt('11in.csv', delimiter=',')
array2 = np.loadtxt('13in.csv', delimiter=',')
array3 = np.loadtxt('15in.csv', delimiter=',')
array4 = np.loadtxt('17in.csv', delimiter=',')

fig, axs = plt.subplots(2)

#**********************************************

#acc_x 8-75in graph *
x1 = array[:,0]
y1 = array[0:,1]
plt.figure()
axs[0].plot(x1,y1)
axs[0].set_title('X Acceleration vs. Time (8.75 in)')
axs[0].set_xlabel('Time (msec.)')
axs[0].set_ylabel('Acceleration (m/s^2.)')
axs[0].set_xlim(0, 8000)


#acc_y 8-75in graph *
x2 = array[:,0]
y2 = array[:,2]
plt.figure()
axs[1].plot(x2,y2)
axs[1].set_title('Y Acceleration vs. Time (8.75 in)')
axs[1].set_xlabel('Time (msec.)')
axs[1].set_ylabel('Acceleration (m/s^2.)')
axs[1].set_xlim(0, 8000)

fig.tight_layout()
fig1, axs1 = plt.subplots(2)

#acc_x 11in graph *
x1 = array1[:,0]
y1 = array1[0:,1]
plt.figure()
axs1[0].plot(x1,y1)
axs1[0].set_title('X Acceleration vs. Time (11 in)')
axs1[0].set_xlabel('Time (msec.)')
axs1[0].set_ylabel('Acceleration (m/s^2.)')
axs1[0].set_xlim(0, 8000)


#acc_y 11in graph *
x2 = array1[:,0]
y2 = array1[:,2]
plt.figure()
axs1[1].plot(x2,y2)
axs1[1].set_title('Y Acceleration vs. Time (11 in)')
axs1[1].set_xlabel('Time (msec.)')
axs1[1].set_ylabel('Acceleration (m/s^2.)')
axs1[1].set_xlim(0, 8000)

fig1.tight_layout()
fig2, axs1 = plt.subplots(2)

#acc_x 13in graph *
x1 = array2[:,0]
y1 = array2[0:,1]
plt.figure()
axs1[0].plot(x1,y1)
axs1[0].set_title('X Acceleration vs. Time (13 in)')
axs1[0].set_xlabel('Time (msec.)')
axs1[0].set_ylabel('Acceleration (m/s^2.)')
axs1[0].set_xlim(0, 8000)


#acc_y 13in graph *
x2 = array2[:,0]
y2 = array2[:,2]
plt.figure()
axs1[1].plot(x2,y2)
axs1[1].set_title('Y Acceleration vs. Time (13 in)')
axs1[1].set_xlabel('Time (msec.)')
axs1[1].set_ylabel('Acceleration (m/s^2.)')
axs1[1].set_xlim(0, 8000)

fig2.tight_layout()
fig3, axs1 = plt.subplots(2)

#acc_x 15in graph *
x1 = array3[:,0]
y1 = array3[0:,1]
plt.figure()
axs1[0].plot(x1,y1)
axs1[0].set_title('X Acceleration vs. Time (15 in)')
axs1[0].set_xlabel('Time (msec.)')
axs1[0].set_ylabel('Acceleration (m/s^2.)')
axs1[0].set_xlim(0, 8000)


#acc_y 15in graph *
x2 = array3[:,0]
y2 = array3[:,2]
plt.figure()
axs1[1].plot(x2,y2)
axs1[1].set_title('Y Acceleration vs. Time (15 in)')
axs1[1].set_xlabel('Time (msec.)')
axs1[1].set_ylabel('Acceleration (m/s^2.)')
axs1[1].set_xlim(0, 8000)

fig3.tight_layout()
fig4, axs1 = plt.subplots(2)

#acc_x 17in graph *
x1 = array4[:,0]
y1 = array4[0:,1]
plt.figure()
axs1[0].plot(x1,y1)
axs1[0].set_title('X Acceleration vs. Time (17in)')
axs1[0].set_xlabel('Time (msec.)')
axs1[0].set_ylabel('Acceleration (m/s^2.)')
axs1[0].set_xlim(0, 8000)


#acc_y 17in graph *
x2 = array4[:,0]
y2 = array4[:,2]
plt.figure()
axs1[1].plot(x2,y2)
axs1[1].set_title('Y Acceleration vs. Time (17 in)')
axs1[1].set_xlabel('Time (msec.)')
axs1[1].set_ylabel('Acceleration (m/s^2.)')
axs1[1].set_xlim(0, 8000)

fig4.tight_layout()
axs1.title.set_text('First Plot')

#*************************************************

acc_x = array[:,1]
acc_y = array[:,2]
acc_z = array[:,3]

def find_tilt_z(acc_x, acc_y, acc_z):
    tiltZ=((math.atan2(acc_z,(math.sqrt((acc_y**2)+(acc_x**2)))))*180)/(math.pi)
    return tiltZ























