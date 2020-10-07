# -*- coding: utf-8 -*-
"""
Created on 4/13/2020

Author: Joost Berkhout (VU, email: j2.berkhout@vu.nl)

Description: Knapsack Exercise 1 from the slides of Lecture 10.
"""

import pulp

# init linear optimization problem object
LO_problem = pulp.LpProblem("knapsack_ILO", pulp.LpMaximize)

# data (parameters)
sizes = [5, 10, 2, 3, 5]
weights = [4, 1, 2, 3, 4]
rewards = [5, 8, 3, 2, 7]
size_capacity = 20
weight_capacity = 10
n = len(sizes)  # number of items

# decision variables
x = [pulp.LpVariable(f'x_{i}', cat='Binary') for i in range(n)]

# objective function
LO_problem += pulp.lpDot(x, rewards), "total_reward"

# constraints
LO_problem += pulp.lpDot(x, sizes) <= size_capacity, "size_capacity_constraint"
LO_problem += pulp.lpDot(x, weights) <= weight_capacity, "weight_capacity_constraint"

print(LO_problem)
LO_problem.solve()
print("Status:", pulp.LpStatus[LO_problem.status])

# each of the variables is printed with it's resolved optimum value
for v in LO_problem.variables():
    print(v.name, "=", v.varValue)

# the optimised objective function value is printed to the screen
print("Total profit = ", pulp.value(LO_problem.objective))

# to find the second best solution, we are going to exclude the solution found
# by ensuring that the sum of those decision variables is smaller than before
x_values = [x[i].value() for i in range(n)]
LO_problem += sum([x[i] for i in range(n) if x_values[i] == 1]) <= sum(x_values) - 1, "exclude_previous_solution"

# solve updated problem
print('\n\nExercise 1c:\n')
print(LO_problem)
LO_problem.solve()
print("Status:", pulp.LpStatus[LO_problem.status])

# each of the variables is printed with it's resolved optimum value
for v in LO_problem.variables():
    print(v.name, "=", v.varValue)

# the optimised objective function value is printed to the screen
print("Total profit = ", pulp.value(LO_problem.objective))
print("The same profit is obtained as before!")