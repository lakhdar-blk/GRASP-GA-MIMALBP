import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G= nx.DiGraph()


G.add_nodes_from([1,2,3,4,5,6,7,8,9])
G.add_edges_from([(1, 3),(2, 3), (3, 5), (5, 7), (4 , 6), (6, 8), (7, 9), (8, 7)])
attrs = {1: {'task1': 6}, 2: {'task2': 4}, 3: {'task3': 6}, 4: {'task4': 4}, 5: {'task5': 2}, 6: {'task6': 5}, 7: {'task7': 5}, 8: {'task8': 8}, 9: {'task9': 4}}
nx.set_node_attributes(G,attrs)

"""
a = "3"
i= 3
print(G.nodes[i]["task"+a])
"""
nb_tasks =  9
nb_solutions =  10 

def creating_random_solutions():
    
    tab =[None]*nb_tasks
    tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    A = np.arange(nb_solutions*nb_tasks).reshape(nb_solutions, nb_tasks)

    for j in range(nb_solutions):    
       

        for i in range(nb_tasks):  
            tab[i] = random.choice(tab2)
            tab2.remove(tab[i])

        A[j] = tab
        tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    return A

def fun(tabb, i):

    tab = tabb

    for e in range(0, nb_tasks):     

                    if tab[e] in list(G.predecessors(tab[i])) and e>i:
                        a = tab[e]
                        tab[e] = tab[i]
                        tab[i] = a
                        tab  = fun(tab, i)  #recursive call

    return tab

def precedence_relations(Array):

    AV = np.arange(nb_solutions*nb_tasks).reshape(nb_solutions, nb_tasks)
   

    for j in range(nb_solutions):
        tab = Array[j]

        for i in range(nb_tasks):
           
            tab = fun(tab, i)
                    

        AV[j] = tab

    return AV

def cycle_time(Array):

  
    cycle_times = [None]*nb_tasks
    work_s = 4
    c_init = 8
    nbw = 1
    

    
    """
    M_stations[0] = [0, 0]
    M_stations[1] = [0, 0]
    M_stations[2] = [0, 0]
    M_stations[3] = [0, 0]
    temp_tab = [0,0]
    """


    for i in range(nb_tasks):

        tab = Array[i]
    
        while nbw != work_s :

            c = c_init
            
            for j in range(nb_tasks):

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
                for k in range(nb_tasks):

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

                """
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
                """


                c_init = 8
                
        nbw = 1    

    return cycle_times    

def ma_in():
    M = creating_random_solutions()
    #print(M)
    M2 = precedence_relations(M)
    #print(M2)
    #cycle_time(M2)

    return M2

def show_graph():
    nx.draw(G, with_labels=True, node_color='green')
    #plt.savefig("path_graph1.png")
    plt.show()

#print(G.nodes())
#print(G.edges())
nx.draw(G, with_labels=True, node_color='green')
#plt.savefig("path_graph1.png")
plt.show()