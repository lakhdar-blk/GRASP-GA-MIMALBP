####################_____________________________________________________________________################################
################### |                    GENETIC____ALGORITHM                           |################################
####################|___________________________________________________________________|################################

import model2 as md2
import numpy as np
from random import randint
from random import shuffle
from random import sample

#initial population
pop = md2.ma_in()


"""
for i in range(len(Random_solutions)):
    print("Solution ",i+1," : ",Random_solutions[i]," has a cycle time = ", c_times[i])
"""
"""
print("first pop:")
print(Random_solutions)
"""


#the fitness function = 1 / cycle time
def fitnesse_function(array):

    tab_fit = [None]*md2.nb_solutions

    for i in range(len(array)):
        tab_fit[i] = 1/array[i]

    return tab_fit

#fitness_sol = fitnesse_function(c_times)

Ind = np.arange(5*md2.nb_tasks).reshape(5,md2.nb_tasks)


# Tournament Selection (the fittest individual is chosen and is passed on to the next generation)
def selection_function(array_2):
    
    #print(array_2)
   
    tab = [None]*(int(len(array_2)/2)) #si nombre de tache est impaire on ajoute 1
    

    for a in range(len(tab)):

        tab[a] = max(array_2)
        b = array_2.index(max(array_2))

        Ind[a] = pop[b]

        array_2[b] = 0

      
    
    return tab


def crossover_function(array_M):

    #print(array_M)
    tab = np.arange(md2.nb_solutions*md2.nb_tasks).reshape(md2.nb_solutions, md2.nb_tasks)
    #tab = array_M
    
    tab[0] = array_M[0]
    tab[1] = array_M[1]
    tab[2] = array_M[2]
    tab[3] = array_M[3]
    tab[4] = array_M[4]
    

    t3 = [None]*md2.nb_tasks
    t4 = [None]*md2.nb_tasks
    t5 = [None]*md2.nb_tasks
    t6 = [None]*md2.nb_tasks

    #one point crossover between the second and the third individuals
    t1 = array_M[1]
    t2 = array_M[2]

    for i in range(3): t3[i] = t1[i] #copy of the first three elements from t1 to t3
    for i in range(3): t4[i] = t2[i] #copy of the first three elements from t2 to t4

    for i in range(3, md2.nb_tasks): t5[i] = t2[i] #copy of the last seven elements from t2 to t5
    for i in range(3, md2.nb_tasks): t6[i] = t1[i] #copy of the last seven elements from t1 to t6

    for i in range(3):

        for j in range(3, md2.nb_tasks):

            if t3[i] == t5[j] : 
                t5[j] = 0
            t3[j] = t5[j]
            
            if t4[i] == t6[j] : 
                t6[j] = 0
            t4[j] = t6[j]
    
    tab[5] = t3
    tab[6] = t4
    #the end

    #one point crossover between the fourth and the fiveth individuals
    t1 = array_M[3]
    t2 = array_M[4]

    for i in range(3): t3[i] = t1[i] #copy of the first three elements from t1 to t3
    for i in range(3): t4[i] = t2[i] #copy of the first three elements from t2 to t4

    for i in range(3, md2.nb_tasks): t5[i] = t2[i] #copy of the last seven elements from t2 to t5
    for i in range(3, md2.nb_tasks): t6[i] = t1[i] #copy of the last seven elements from t1 to t6

    for i in range(3):

        for j in range(3, md2.nb_tasks):

            if t3[i] == t5[j] : 
                t5[j] = 0
            t3[j] = t5[j]
            
            if t4[i] == t6[j] : 
                t6[j] = 0
            t4[j] = t6[j]
    
    tab[7] = t3
    tab[8] = t4
    #the end

    
    #one point crossover between the first and the fourth individuals
    t1 = array_M[0]
    t2 = array_M[4]

    for i in range(3): t3[i] = t1[i] #copy of the first three elements from t1 to t3
    for i in range(3): t4[i] = t2[i] #copy of the first three elements from t2 to t4

    for i in range(3, md2.nb_tasks): t5[i] = t2[i] #copy of the last seven elements from t2 to t5
    for i in range(3, md2.nb_tasks): t6[i] = t1[i] #copy of the last seven elements from t1 to t6

    for i in range(3):

        for j in range(3, md2.nb_tasks):

            if t3[i] == t5[j] : 
                t5[j] = 0
            t3[j] = t5[j]
            
            if t4[i] == t6[j] : 
                t6[j] = 0
            t4[j] = t6[j]
    
    tab[9] = t3
    
    #the end
    
    #print("---------------------------------")
    #replacing 0 by another acceptable number
    for j in range(md2.nb_solutions):
        t = tab[j]
        
        for i in range(1,md2.nb_tasks+1):

                if i !=3 and i!=6 and not i in t :
                    for k in range(md2.nb_tasks):
                        if t[k] == 0 :
                            t[k] = i
                            break
    
    #print(tab)
    #tab = md2.precedence_relations(tab)
    #print(tab)

    """
    print("crossover")
    """

  
    
    return tab
    #print(t4)
    
   
def mutation_function(array):

    pm = 0.3
    a = int(pm * md2.nb_tasks)
    tab = [None]*a
    i=0
    #tm = np.arange(30).reshape(3,10)
    while a!= 0:
        n = randint(0, 9)
        if not n in tab:
            tab[i] = n
            a = a-1
            i=i+1

    #sample(tab, len(tab))
    #print(tab)

    ts = [None]*6
    for j in tab:

        tm = array[j]
       
        for i in range(2,8):
                ts[i-2] = tm[i]
            
        ts = sample(ts, len(ts))
        for i in range(2, 8):
                tm[i] = ts[i-2]

        array[j] = tm

    """
    print("after mutation")
    print(array)        
    """
    array = md2.precedence_relations(array)

    return array
    """
    print("after precedence relations verifiation:")
    print(array)  
    """

   
    #print(tm)
    




"""
for i in range(len(Random_solutions)):
    print("Solution ",i+1," : ",Random_solutions[i]," cycle time = ",c_times[i]," and fitness function = ", fitness_sol[i])


for j in range(len(Ind)):
    print("individual ",j+1," : ",Ind[j]," fit = ",selected_individuals_fitness[j])

crossover_function(Ind)
"""

#selected_individuals_fitness = selection_function(fitnesse_function(c_times))



print(pop)  #first population
c_times = md2.cycle_time(pop) #cycle times of first individuals
print(c_times)
print("-------------------------------")


for g in range(1000):
    selection_function(fitnesse_function(c_times)) #selection process based on cycle times
    pop = mutation_function(crossover_function(Ind)) #crossover and mutation
    c_times = md2.cycle_time(pop)
  




print(pop) #the final population after 2000 generation
print(c_times)


    #print(c_times)
"""
for j in range(len(selected_individuals_fitness)):
    print("individual ",j+1," : ",selected_individuals_fitness[j])
"""




#md2.ma_in()
#md2.show_graph()