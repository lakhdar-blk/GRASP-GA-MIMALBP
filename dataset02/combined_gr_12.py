import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G= nx.DiGraph()

G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12])
G.add_edges_from([(1, 4),(2, 5), (3, 6), (4, 7), (5 , 7), (5, 8), (5, 9), (6, 9), (7, 10), (8, 10), (9, 11), (11, 12)])
attrs = {1: {'task1': 6}, 2: {'task2': 23}, 3: {'task3': 25}, 4: {'task4': 16.5}, 
5: {'task5': 20}, 6: {'task6': 12}, 7: {'task7': 9}, 8: {'task8': 11}, 
9: {'task9': 14}, 10: {'task10': 8.5}, 11: {'task11': 17}, 12: {'task12': 13}}
nx.set_node_attributes(G,attrs)


nb_tasks =  12
nb_solutions = 20

def creating_random_solutions():
    
    tab =[None]*nb_tasks
    #tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    #tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    A = np.arange(nb_solutions*nb_tasks).reshape(nb_solutions, nb_tasks)

    for i in range(nb_solutions):
        for j in range(nb_tasks):
            A[i][j] = 0

    for j in range(nb_solutions):    
       

        for i in range(nb_tasks):  
            tab[i] = random.choice(tab2)
            tab2.remove(tab[i])

        #tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        #tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
        tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        A[j] = tab
              
            
            
        
        
          
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

  
    #cycle_times = [None]*nb_solutions
    cycle_times = [None]*len(Array)
    work_s = 4
    c_init = 25
    nbw = 1
    
    
    
    """
    M_stations[0] = [0, 0]
    M_stations[1] = [0, 0]
    M_stations[2] = [0, 0]
    M_stations[3] = [0, 0]
    temp_tab = [0,0]
    """


    #for i in range(nb_solutions):
    for i in range(len(Array)):   
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
                c_init = c_init + 0.5
                c = c_init 
                nbw = 1                                                                                                   
            
            else :
                cycle_times [i]  = c_init
                c_init = 25
                
                 
                
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
#nx.draw(G, with_labels=True, node_color='green')
#plt.savefig("path_graph1.png")
#plt.show()