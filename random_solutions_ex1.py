import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
G= nx.DiGraph()


G.add_nodes_from([1,2,3,4,5,6])
G.add_edges_from([(1, 3),(2, 4), (2, 5), (3, 6), (4 , 6), (5, 6)])
attrs = {1: {'task1': 5}, 2: {'task2': 3}, 3: {'task3': 4}, 4: {'task4': 5}, 5: {'task5': 6}, 6: {'task6': 3}}
nx.set_node_attributes(G,attrs)

"""
a = "3"
i= 3
print(G.nodes[i]["task"+a])
"""

def creating_random_solutions():
    
    tab =[None]*6
    tab2 = [1, 2, 3, 4, 5, 6]
    
    A = np.arange(36).reshape(6,6)

    for j in range(6):    
       

        for i in range(6):  
            tab[i] = random.choice(tab2)
            tab2.remove(tab[i])

        A[j] = tab
        tab2 = [1, 2, 3, 4, 5, 6]
    
    return A

def fun(tabb, i):

    tab = tabb

    for e in range(0, 6):     

                    if tab[e] in list(G.predecessors(tab[i])) and e>i:
                        a = tab[e]
                        tab[e] = tab[i]
                        tab[i] = a
                        tab  = fun(tab, i)

    return tab

def precedence_relations(Array):

    AV = np.arange(36).reshape(6,6)

    for j in range(6):
        tab = Array[j]
        s = 0

        for i in range(6):
           
            tab = fun(tab, i)
          
        AV[j] = tab

    return AV

def cycle_time(Array):

    cycle_times = [None]*8
    work_s = 3
    c_init = 6
    nbw = 1
    

    
    """
    M_stations[0] = [0, 0]
    M_stations[1] = [0, 0]
    M_stations[2] = [0, 0]
    M_stations[3] = [0, 0]
    temp_tab = [0,0]
    """
  
   

    for i in range(6):

        tab = Array[i]
    
        while nbw != work_s :

            c = c_init
            
            for j in range(6):

                a = tab[j]

                if(c >= G.nodes[a]["task"+str(a)]):
                    c = c - G.nodes[a]["task"+str(a)] 
                  
                                                                                                                                                    
                    #print("task:",a," Opt : ",G.nodes[a]["task"+str(a)])

                else :
                    nbw = nbw + 1
                    c = c_init
                    c = c - G.nodes[a]["task"+str(a)]
                 

            if (nbw != work_s):
                c_init = c_init + 1
                c = c_init 
                nbw = 1                                                                                                   
            
            else :
                cycle_times [i]  = c_init
                l = 1
                ct = cycle_times[i]
                station_1 = [None]*10
                station_2 = [None]*10
                station_3 = [None]*10
                p=0
                for k in range(6):

                    if(G.nodes[tab[k]]["task"+str(tab[k])] <= ct):
                        #print("station ",l," : ",tab[k],"| ", end=" ")
                        if(l == 1):
                            station_1[p] = tab[k]
                            p = p + 1
                        if(l == 2):
                            station_2[p] = tab[k]
                            p = p + 1
                        if(l == 3):
                            station_3[p] = tab[k]
                            p = p + 1

                        ct = ct - G.nodes[tab[k]]["task"+str(tab[k])]

                    else:
                        l = l + 1 
                        ct = cycle_times[i]
                        p = 0

                        if(l == 1):
                            station_1[p] = tab[k]
                            p = p + 1
                        if(l == 2):
                            station_2[p] = tab[k]
                            p = p + 1
                        if(l == 3):
                            station_3[p] = tab[k]
                            p = p + 1
                        
                        #print("station ",l," : ",tab[k],"| ", end=" ")
                        ct = ct - G.nodes[tab[k]]["task"+str(tab[k])]

                print("station 1 : ", end=" ")
                for t in range(0,len(station_1)):
                    if(station_1[t] != None):
                        print(station_1[t]," | ", end=" ")
                print("")

                print("station 2 : ", end=" ")
                for t in range(0,len(station_2)):
                    if(station_2[t] != None):
                        print(station_2[t]," | ", end=" ")
                print("")

                print("station 3 : ", end=" ")
                for t in range(0,len(station_3)):
                    if(station_3[t] != None):
                        print(station_3[t]," | ", end=" ")
                print("")

                print("success for c = ", cycle_times[i])
                print("--------------------------------")
            
                c_init = 6

        nbw = 1    

M = creating_random_solutions()
#print(M)
M2 = precedence_relations(M)
print(M2)
cycle_time(M2)

#print(G.nodes())
#print(G.edges())
nx.draw(G, with_labels=True, node_color='green')
#plt.savefig("path_graph1.png")
plt.show()