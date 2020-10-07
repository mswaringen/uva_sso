"""
Created on 4/11/2020

Author: Joost Berkhout (VU, email: j2.berkhout@vu.nl)

Description: This is the elaboration of the TSP example from Lecture 10 slides.

The notation from the slides is used.
"""

import pulp
import itertools

# load data
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
undirected_edge_lengths = [('A', 'B', 2),
                           ('A', 'C', 1),
                           ('B', 'C', 2),
                           ('B', 'D', 3),
                           ('B', 'E', 2),
                           ('C', 'D', 3),
                           ('C', 'E', 6),
                           ('D', 'E', 1),
                           ('D', 'F', 5),
                           ('E', 'F', 2)]
big_constant = 10000  # distance for non-existing edges
n = len(nodes)  # number of nodes

# preprocess data in two steps:

# 1. add reversed (directed) edges
edge_lengths = undirected_edge_lengths.copy()
for i, j, distance in undirected_edge_lengths:
    edge_lengths.append((j, i, distance))  # also add reversed edge

# 2. create a distance matrix with c[i][j] the distance from i to j
c = {i: {j: big_constant for j in nodes} for i in nodes}
for i, j, length in edge_lengths:
    c[i][j] = length

# Start modeling
# ==============

# init model
ILO_TSP = pulp.LpProblem("TSP_ILO", pulp.LpMinimize)

# decision variables
x = pulp.LpVariable.dicts("edge", (nodes, nodes), cat=pulp.LpBinary)  # x[i][j] = 1 if edge (i, j) is used, 0 else

# objective
ILO_TSP += sum([c[i][j] * x[i][j] for i in nodes for j in nodes]), "min_tour_length"

# constraints
for j in nodes:
    ILO_TSP += sum([x[i][j] for i in nodes]) == 1, f'visit_{j}'
    ILO_TSP += sum([x[j][i] for i in nodes]) == 1, f'leave_{j}'

for subset_size in range(1, n):
    # add restrictions for all subsets of this size
    for subset in itertools.combinations(nodes, subset_size):
        ILO_TSP += sum([x[i][j] for i in subset for j in subset]) <= subset_size - 1, f'subtour_elimination_for_subset_{subset}'

# solve problem and present results
ILO_TSP.solve()
print("Optimization status:", pulp.LpStatus[ILO_TSP.status])
print('The optimal route from source to destination is:')
for i in nodes:
    for j in nodes:
        if pulp.value(x[i][j]) == 1:
            print(f'From {i} to {j}')
print(f'with a minimum tour length of {ILO_TSP.objective.value()}')