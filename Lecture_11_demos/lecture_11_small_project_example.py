# -*- coding: utf-8 -*-
"""
Created on 4/21/2020

Author: Joost Berkhout (VU, email: j2.berkhout@vu.nl)

Description: Simulation of the small project planning example from slides with
precedence constraints A -> C <- B, i.e., activity C can only start once
activities A & B are finished. The goal is to find an approximation of the
expected project finish time.
"""

import numpy as np

# init
mean = 1  # mean of underlying normal distribution
sigma = 1  # standard deviation of underlying normal distribution
N = 1000  # number of simulations

# each of the 3 columns in the following corresponds to the activities, resp.

# simulate (sim) activity durations (dur)
durSim = np.random.lognormal(mean=mean, sigma=sigma, size=(N, 3))
# print(durSim)

# # determine the finish times of the activities
finishTimes = np.empty((N, 3))
finishTimes[:, [0, 1]] = durSim[:, [0, 1]]  # act. A & B can start directly
finishTimes[:, 2] = np.max(durSim[:, [0, 1]], axis=1) + durSim[:, 2]

# # determine mean project finish time (equal to finish time activity C)
print(np.mean(finishTimes[:, 2]))
