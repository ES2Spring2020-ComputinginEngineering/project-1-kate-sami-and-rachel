#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:19:33 2020

@author: samirothstein
"""
#import numpy as np
import matplotlib.pyplot as plt
length = [8.75,11,13,15,17]
period = [427.52,420.23,428.28,434.28,558.35]
plt.plot(length,period,'.')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('log (length) in.')
plt.ylabel('log (period) ms.')