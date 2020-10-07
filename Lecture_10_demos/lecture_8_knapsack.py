# -*- coding: utf-8 -*-
"""
Created on 3/17/2020

Author: Joost Berkhout (VU, email: j2.berkhout@vu.nl)

Description: Knapsack example from the slides of Lecture 8.
"""

import pulp

# init linear optimization problem object
LO_problem = pulp.LpProblem("knapsack_ILO", pulp.LpMaximize)

# data (parameters)
sizes = [3, 5, 4, 1.4, 3, 3, 1]
rewards = [60, 60, 40, 10, 20, 10, 3]
capacity = 11
n = len(sizes)  # number of items

# modelling

# decision variables
x = [pulp.LpVariable(f'x_{i}', cat='Binary') for i in range(n)]

# objective function
LO_problem += pulp.lpDot(x, rewards), "total_reward"

# constraints
LO_problem += pulp.lpDot(x, sizes) <= capacity, "capacity_constraint"

print(LO_problem)
LO_problem.solve()
print("Status:", pulp.LpStatus[LO_problem.status])

# each of the variables is printed with its resolved optimum value
for v in LO_problem.variables():
    print(v.name, "=", v.varValue)

# the optimised objective function value is printed to the screen
print("Total profit = ", LO_problem.objective.value())
