# -*- coding: utf-8 -*-
"""
Created on 4/30/2019

Author: Joost Berkhout (VU, email: j2.berkhout@vu.nl)

Description: A simple discrete-event simulation (DES) of a single-server queue.
"""

import scipy.stats
import numpy as np

# init
serviceTimeDistr = scipy.stats.lognorm(s=1, scale=np.exp(1))
interArrivalDistr = scipy.stats.expon(scale=5)
maxTime = 3500
"""
Remark: via the scipy module in python, you can make objects correponding to 
a distribution. Using this object, you can generate a random number by calling
.rvs(). This can be done from any distribution object. Therefore, this makes
the code a bit more robust as I can change the required distribution in the 
code above and I do not have to change all random number generation inside the
code (which would be the case if I would use np.random).

As an example: serviceTimeDistr.rvs() gives the same random number as
np.random.lognormal(1, 1)
"""

# technical init for simulation
time = 0
state = 0  # number in queue
nextServiceTimeCompletion = np.inf  # infinity represents none in service
nextInterArrivalTime = interArrivalDistr.rvs()
totalInQueueOverTime = 0

while time < maxTime:
    # continue simulation

    oldTime = time
    oldState = state

    if nextInterArrivalTime <= nextServiceTimeCompletion:
        # next event: a new arrival
        time += nextInterArrivalTime
        if state == 0:
            # arrival to empty system
            nextServiceTimeCompletion = serviceTimeDistr.rvs()
        else:
            nextServiceTimeCompletion -= nextInterArrivalTime
        state += 1
        nextInterArrivalTime = interArrivalDistr.rvs()
    else:
        # next event: a service completion
        time += nextServiceTimeCompletion
        state -= 1
        nextInterArrivalTime -= nextServiceTimeCompletion
        if state == 0:
            # none in service
            nextServiceTimeCompletion = np.inf
        else:
            nextServiceTimeCompletion = serviceTimeDistr.rvs()

    totalInQueueOverTime += (time - oldTime)*oldState

averageQueueLength = totalInQueueOverTime/time

print('Average in queue is {}'.format(averageQueueLength))