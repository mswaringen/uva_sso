# -*- coding: utf-8 -*-
"""
Created on 3/17/2020

Author: Joost Berkhout (VU, email: j2.berkhout@vu.nl)

Description: Product mix example from the slides of Lecture 1.
"""

import pulp

# init linear optimization problem object
LO_problem = pulp.LpProblem("product_mix_LO", pulp.LpMaximize)

# decision variables
x_1 = pulp.LpVariable('x_1', lowBound=0)
x_2 = pulp.LpVariable('x_2', lowBound=0)

# Objective function
LO_problem += 2*x_1 + 3*x_2, "profit"

# Constraints
LO_problem += x_1 <= 5, "resource_1_constraint"
LO_problem += x_1 + 2*x_2 <= 10, "resource_2_constraint"

print(LO_problem)
LO_problem.solve()
print("Status:", pulp.LpStatus[LO_problem.status])

# Each of the variables is printed with it's resolved optimum value
for v in LO_problem.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total profit = ", pulp.value(LO_problem.objective))





