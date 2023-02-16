import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


G= nx.DiGraph()                                                 #creation of a dircted graph

G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12])
G.add_edges_from([(1, 4),(2, 5), (3, 6), (4, 7), (5 , 7), (5, 8), (5, 9), (6, 9), (7, 10), (8, 10), (9, 11), (11, 12)])
attrs = {1: {'task1': 6}, 2: {'task2': 23}, 3: {'task3': 25}, 4: {'task4': 16.5}, 
5: {'task5': 20}, 6: {'task6': 12}, 7: {'task7': 9}, 8: {'task8': 11}, 
9: {'task9': 14}, 10: {'task10': 8.5}, 11: {'task11': 17}, 12: {'task12': 13}}
nx.set_node_attributes(G,attrs)


"""
a=2
l = [1,2,3,4]

#l2[0:a-1] = l[0:a-1]

print(l[0:a])"""