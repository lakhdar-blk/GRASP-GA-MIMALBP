####################_____________________________________________________________________################################
################### |                    GENETIC____ALGORITHM                           |################################
####################|___________________________________________________________________|################################

import combined_gr_12 as mdcmb
import numpy as np
from random import randint
from random import shuffle
from random import sample
import matplotlib.pyplot as plt
import sys
import random
"""
from humanfriendly import format_timespan
import time
begin_time = time.time()
end_time = time.time() - begin_time
print("Total execution time: ", format_timespan(end_time))"""
sys.setrecursionlimit(5000)




#initial population
#pop = mdcmb.ma_in()


pop = [[2, 5, 1, 4, 3, 6, 8, 7, 9, 11, 10, 12],
    [2, 3, 1, 4, 5, 8, 7, 6, 9, 10, 11, 12],
    [3, 2, 1, 5, 4, 6, 8, 9, 7, 11, 10, 12],
    [3, 2, 1, 5, 6, 8, 9, 4, 7, 11, 10, 12],
    [2, 5, 1, 3, 4, 6, 7, 9, 8, 10, 11, 12],
    [2, 3, 1, 5, 6, 4, 8, 9, 7, 11, 10, 12],
    [3, 2, 1, 5, 4, 6, 9, 7, 8, 10, 11, 12],
    [2, 3, 1, 5, 4, 8, 7, 6, 9, 10, 11, 12],
    [3, 1, 6, 4, 2, 5, 8, 9, 7, 10, 11, 12],
    [2, 5, 1, 4, 3, 6, 9, 7, 8, 10, 11, 12],
    [2, 3, 1, 6, 4, 5, 9, 8, 7, 10, 11, 12],
    [3, 6, 1, 2, 4, 5, 8, 9, 7, 11, 10, 12],
    [3, 2, 1, 4, 6, 5, 8, 9, 7, 11, 10, 12],
    [2, 5, 1, 3, 4, 6, 9, 8, 7, 10, 11, 12],
    [2, 3, 1, 5, 4, 6, 9, 7, 8, 11, 10, 12],
    [3, 2, 1, 4, 5, 6, 9, 8, 7, 10, 11, 12],
    [2, 5, 1, 4, 3, 6, 7, 9, 8, 10, 11, 12],
    [2, 3, 1, 6, 5, 4, 9, 8, 7, 10, 11, 12],
    [2, 3, 1, 4, 6, 5, 9, 8, 7, 10, 11, 12],
    [2, 3, 1, 4, 5, 6, 8, 9, 7, 10, 11, 12]]


"""
pop = [[3, 6, 1, 2, 5, 9, 11, 12, 8, 4, 7, 10],
 [ 2 ,5 ,1 ,3 ,6 ,4 ,8 ,9 ,7, 11 ,12, 10],
 [ 2 ,1 ,5 ,4 ,3 ,6 ,9 ,7 ,8 ,10, 11, 12],
 [ 2 ,3 ,1 ,5 ,6 ,4 ,9, 11 ,7 ,12 ,8, 10],
 [ 2 ,5 ,8 ,3 ,1 ,6 ,9 ,4 ,7 ,11 ,10 ,12],
 [ 2 ,5 ,1 ,3 ,8 ,6 ,4 ,9 ,11 ,7 ,12 ,10],
 [ 2 ,5 ,3 ,8 ,1 ,6 ,9 ,4 ,11 ,7 ,10 ,12],
 [ 1 ,3 ,2 ,6 ,4 ,5 ,9 ,8 ,7 ,11 ,10 ,12],
 [ 2 ,3 ,1 ,5 ,8 ,4 ,7 ,6 ,9 ,11 ,12 ,10],
 [ 1 ,4 ,2 ,5 ,3 ,7 ,8 ,6 ,10 ,9 ,11 ,12],
 [ 3 ,2 ,6 ,1 ,4 ,5 ,7 ,9, 11, 12 ,8 ,10],
 [ 2 ,5 ,1 ,3 ,6 ,4 ,8 ,9 ,7 ,10 ,11 ,12],
 [ 3 ,2 ,1 ,6 ,5 ,9 ,4 ,7 ,8 ,11 ,10 ,12],
 [ 3 ,2 ,6 ,1 ,5 ,9 ,11 ,4 ,7 ,8 ,12 ,10],
 [ 2 ,5 ,3 ,6 ,1 ,9 ,8 ,11 ,4 ,7 ,10 ,12],
 [ 3 ,2 ,5 ,1 ,6 ,4 ,9 ,8 ,7, 11 ,12 ,10],
 [ 1 ,3 ,2 ,4 ,5 ,8 ,6 ,7 ,9 ,11 ,12 ,10],
 [ 1 ,2 ,3 ,5 ,4 ,7 ,6 ,8 ,9 ,10 ,11 ,12],
 [ 2 ,5 ,8 ,3 ,6 ,9 ,11 ,1 ,4 ,12 ,7 ,10],
 [ 3 ,6 ,2 ,5 ,1 ,8 ,4 ,7 ,9, 10 ,11 ,12]]"""


"""
pop = [[2, 1, 5, 3, 6, 9, 4, 11, 8, 7, 12, 10],
       [2, 1, 5, 3, 4, 6, 9, 11, 7, 8, 10, 12],
       [2, 5, 1, 3, 6, 9, 4, 11, 8, 7, 12, 10],
       [1, 2, 5, 3, 4, 6, 9, 11, 7, 12, 8, 10],
       [2, 5, 1, 3, 6, 9, 4, 11, 8, 12, 7, 10],
       [2, 3, 6, 1, 5, 4, 8,  9, 7, 11, 10, 12],
       [3, 6, 2, 5, 9, 8, 11, 12, 1, 4, 7, 10],
       [ 1,  4,  2,  3,  5,  7,  8,  6, 10,  9, 11, 12],
       [ 3,  2,  6,  1,  5,  8,  4,  9, 11,  7, 10, 12],
       [ 2,  5,  8,  1,  3,  6,  9, 11,  4,  7, 12, 10]]

"""
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

   
    tab_fit = [None]*mdcmb.nb_solutions

    for i in range(len(array)):
        tab_fit[i] = 1/array[i]

    return tab_fit

#fitness_sol = fitnesse_function(c_times)

mtp = np.arange(10*mdcmb.nb_tasks).reshape(10,mdcmb.nb_tasks)


# Tournament Selection (the fittest individual is chosen and is passed on to the next generation)
def selection_function(array_2):

    copiec = array_2.copy()
    templ = []
    j=0
    while(j<5):

        if(list(pop[copiec.index(max(copiec))]) not in templ):
            templ.append(list(pop[copiec.index(max(copiec))]))
            mtp[j] = templ[j]
            copiec[copiec.index(max(copiec))] = 0
            j=j+1
   
    #print(mtp[0])


    k = 2 
    candidate_list = []
    l = []
    l_index = []
    ri = 0
    j = 5

    while(j < 10):

        for i in range(k):

            while(True):

                ri = randint(5,19)
                if(ri not in l):
                    l.append(ri)
                    tup = [ri , array_2[ri]]
                    candidate_list.append(tup)
                    break

        #print(candidate_list)
        #input()
        """
            candidate_list_ind[i] = popu.index(random.choice(pop))
            candidate_list_c[i] = array_2(candidate_list_ind[i])
        """
        max_c = 0

        for i in range(2):

            if(max_c < candidate_list[i][1]):
                max_c = candidate_list[i][1]
                index = candidate_list[i][0]

        if(index not in l_index):
            
            mtp[j] = pop[index]
            l_index.append(index)
            j= j+1

        candidate_list = []
        l = []

    #print(mtp)
    #input()
    """
    tab = [None]*(int(len(array_2)/2)) #si nombre de tache est impaire on ajoute 1
   
    for a in range(len(tab)):
       
        
        tab[a] = max(array_2)
        
        b = array_2.index(max(array_2))

        Ind[a] = pop[b]

        array_2[b] = 0

    """
    

    #return tab


def crossover_function(array_M):
   
  

    tab = np.arange(mdcmb.nb_solutions*mdcmb.nb_tasks).reshape(mdcmb.nb_solutions, mdcmb.nb_tasks)
    #tab = array_M
    po = 3

    tab[0] = array_M[0]
    tab[1] = array_M[1]
    tab[2] = array_M[2]
    tab[3] = array_M[3]
    tab[4] = array_M[4]
    tab[5] = array_M[5]
    tab[6] = array_M[6]
    tab[7] = array_M[7]
    tab[8] = array_M[8]
    tab[9] = array_M[9]

    t3 = [None]*mdcmb.nb_tasks
    t4 = [None]*mdcmb.nb_tasks
    t5 = [None]*mdcmb.nb_tasks
    t6 = [None]*mdcmb.nb_tasks

    
    #one point crossover between the second and the third individuals
    t1 = array_M[0]
    t2 = array_M[1]

    for i in range(po): t3[i] = t1[i] #copy of the first three elements from t1 to t3
    for i in range(po): t4[i] = t2[i] #copy of the first three elements from t2 to t4

    for i in range(po, mdcmb.nb_tasks): t5[i] = t2[i] #copy of the last seven elements from t2 to t5
    for i in range(po, mdcmb.nb_tasks): t6[i] = t1[i] #copy of the last seven elements from t1 to t6

    for i in range(po):

        for j in range(po, mdcmb.nb_tasks):

            if t3[i] == t5[j] : 
                t5[j] = 0
            t3[j] = t5[j]
            
            if t4[i] == t6[j] : 
                t6[j] = 0
            t4[j] = t6[j]
    
    tab[10] = t3
    tab[11] = t4
    #the end

    t1 = array_M[1]
    t2 = array_M[2]

    for i in range(po): t3[i] = t1[i] #copy of the first three elements from t1 to t3
    for i in range(po): t4[i] = t2[i] #copy of the first three elements from t2 to t4

    for i in range(po, mdcmb.nb_tasks): t5[i] = t2[i] #copy of the last seven elements from t2 to t5
    for i in range(po, mdcmb.nb_tasks): t6[i] = t1[i] #copy of the last seven elements from t1 to t6

    for i in range(po):

        for j in range(po, mdcmb.nb_tasks):

            if t3[i] == t5[j] : 
                t5[j] = 0
            t3[j] = t5[j]
            
            if t4[i] == t6[j] : 
                t6[j] = 0
            t4[j] = t6[j]
    
    tab[12] = t3
    tab[13] = t4
    #the end

    #one point crossover between the first and the fiveth individuals
    t1 = array_M[2]
    t2 = array_M[3]

    for i in range(po): t3[i] = t1[i] #copy of the first three elements from t1 to t3
    for i in range(po): t4[i] = t2[i] #copy of the first three elements from t2 to t4

    for i in range(po, mdcmb.nb_tasks): t5[i] = t2[i] #copy of the last seven elements from t2 to t5
    for i in range(po, mdcmb.nb_tasks): t6[i] = t1[i] #copy of the last seven elements from t1 to t6

    for i in range(po):

        for j in range(po, mdcmb.nb_tasks):

            if t3[i] == t5[j] : 
                t5[j] = 0
            t3[j] = t5[j]
            
            if t4[i] == t6[j] : 
                t6[j] = 0
            t4[j] = t6[j]
    
    tab[14] = t3
    tab[15] = t4
    
    #the end
    #one point crossover between the first and the fiveth individuals
    t1 = array_M[3]
    t2 = array_M[4]

    for i in range(po): t3[i] = t1[i] #copy of the first three elements from t1 to t3
    for i in range(po): t4[i] = t2[i] #copy of the first three elements from t2 to t4

    for i in range(po, mdcmb.nb_tasks): t5[i] = t2[i] #copy of the last seven elements from t2 to t5
    for i in range(po, mdcmb.nb_tasks): t6[i] = t1[i] #copy of the last seven elements from t1 to t6

    for i in range(po):

        for j in range(po, mdcmb.nb_tasks):

            if t3[i] == t5[j] : 
                t5[j] = 0
            t3[j] = t5[j]
            
            if t4[i] == t6[j] : 
                t6[j] = 0
            t4[j] = t6[j]
    
    tab[16] = t3
    tab[17] = t4
    
    #the end
      #one point crossover between the first and the fiveth individuals
    t1 = array_M[4]
    t2 = array_M[5]

    for i in range(po): t3[i] = t1[i] #copy of the first three elements from t1 to t3
    for i in range(po): t4[i] = t2[i] #copy of the first three elements from t2 to t4

    for i in range(po, mdcmb.nb_tasks): t5[i] = t2[i] #copy of the last seven elements from t2 to t5
    for i in range(po, mdcmb.nb_tasks): t6[i] = t1[i] #copy of the last seven elements from t1 to t6

    for i in range(po):

        for j in range(po, mdcmb.nb_tasks):

            if t3[i] == t5[j] : 
                t5[j] = 0
            t3[j] = t5[j]
            
            if t4[i] == t6[j] : 
                t6[j] = 0
            t4[j] = t6[j]
    
    tab[18] = t3
    tab[19] = t4
    
    #the end
    
    #print("---------------------------------")
    #replacing 0 by another acceptable number
    for j in range(mdcmb.nb_solutions):
        t = tab[j]
        for i in range(1,mdcmb.nb_tasks+1):
            if not i in t :
                for k in range(mdcmb.nb_tasks):
                    if t[k] == 0 :
                        t[k] = i
                        break
    
    #print(tab)
    #tab = mdcmb.precedence_relations(tab)
    #print(tab)

    
    
    return tab
    #print(t4)
    
   
def mutation_function(array):

    
    pm = 0.15
    a = int(pm * mdcmb.nb_solutions)
    tab = [None]*a
    i=0
    #tm = np.arange(30).reshape(3,10)
    while a!= 0:
        n = randint(5, 19)
        if not n in tab:
            tab[i] = n
            a = a-1
            i=i+1

    #sample(tab, len(tab))
  

    #ts = [None]*8
    for j in tab:

          
        tm = list(array[j])
        a = random.choice(tm)
        id1 = tm.index(a)
        while(True):
            b = random.choice(tm)
            id2 = tm.index(b)
            if(b!=a):
                break
        
        tm[id1] = b
        tm[id2] = a

        array[j] = tm
       

        """
        tm = array[j]
        #print(tm)
        tfs = [0,1,2,3,4,5,6]
        tfe = [7,8,9,10,]
        s = random.choice()
        for i in range(0,8):
            #print(i)
            ts[i] = tm[i] #--------***ts[i-!] modifit
        #print(ts)    
        ts = sample(ts, len(ts))
        for i in range(0, 8):
            tm[i] = ts[i] #--------***ts[i-!] modifit
        #print(ts)
        #print(tm)
        #*
        # input()
        array[j] = tm
        """

    """
    print("after mutation")
    print(array)        
    """
    #print("mutation")
    #print(array)
    #input()
  
    """
    print("*************before****************")
    print(array)
    """
    array = mdcmb.precedence_relations(array)
  
    for i in range(mdcmb.nb_solutions):

        for j in range(mdcmb.nb_solutions):
            if((i != j)):
                
                tab = list(array[i])
                tab2 = list(array[j])
                if(tab == tab2):
                    #print("repedted")
                    #print(i)
                    #print(array)
                    #input()
                    array = mutation_function(array)
    """
    print("*************afetr****************")
    print(array)
    input()
    """
    print("mutation")
    print(array)
    input()
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


converg_c = []
print(pop)  #first population
c_times = mdcmb.cycle_time(pop) #cycle times of first individuals
print(c_times)
print("-------------------------------")
converg_c.append(min(c_times))

idx = c_times.index(min(c_times))
max_num_of_sol = []
max_num_of_sol.append(list(pop[idx]))

#if(list(pop[idx]) not in max_num_of_sol and min(c_times) <= 45.5):
"""
if(list(pop[idx]) not in max_num_of_sol and len(max_num_of_sol) > 0):

    #for simple GA
    l = mdcmb.cycle_time(max_num_of_sol)
    if(min(c_times) < min(max_num_of_sol)):
        max_num_of_sol = []
        max_num_of_sol.append(list(pop[idx]))
    else:
        max_num_of_sol.append(list(pop[idx]))
    #for GA
"""
""" for hybrid
    max_num_of_sol.append(list(pop[idx]))
"""

axe_y = c_times

"""
best_gen = pop
best_gen_c = c_times
min_c = min(c_times)
num_best_sol = 0
n_b_s = 0
ng = 0

for i in c_times:
    if(i == min_c):
        num_best_sol = num_best_sol  + 1

"""


for g in range(100):
    selection_function(fitnesse_function(c_times)) #selection process based on cycle times
    pop = mutation_function(crossover_function(mtp)) #crossover and mutation
    c_times = mdcmb.cycle_time(pop)
    converg_c.append(min(c_times))
    """
    idx = c_times.index(min(c_times))

    if(list(pop[idx]) not in max_num_of_sol and min(c_times) <= 45.5):
        max_num_of_sol.append(list(pop[idx]))
    """

    """
    idx = c_times.index(min(c_times))

    if(list(pop[idx]) not in max_num_of_sol):

        #for simple GA
        l = mdcmb.cycle_time(max_num_of_sol)

        if(min(c_times) < min(l)):
            max_num_of_sol = []
            max_num_of_sol.append(list(pop[idx]))

        elif(min(c_times) == min(l)):
            max_num_of_sol.append(list(pop[idx]))
    """


    """
    if(min_c > min(c_times)):
        
        min_c = min(c_times)
        num_best_sol = 0

        for i in c_times:
            if(i == min_c):
                num_best_sol = num_best_sol  + 1  

        best_gen = pop
        best_gen_c = c_times
        ng = g

    else:
       
        for i in c_times:
            if(i == min_c):
                n_b_s = n_b_s + 1

        if(n_b_s > num_best_sol):
            num_best_sol = n_b_s
            best_gen = pop
            best_gen_c = c_times
            ng = g
    n_b_s = 0
    """

print(pop) #the final population after 2000 generation
print(c_times)
print(converg_c)
"""
print("max_num:")
print(max_num_of_sol)
cc =  mdcmb.cycle_time(max_num_of_sol) 
print(cc)
"""
"""
print("best generation:")
print(best_gen)
print(best_gen_c)
print(ng)
"""

axe_y2 = c_times
#axe_y3 = best_gen_c

    #print(c_times)
"""
for j in range(len(selected_individuals_fitness)):
    print("individual ",j+1," : ",selected_individuals_fitness[j])
"""




#mdcmb.ma_in()
#mdcmb.show_graph()
#plt.style.use('fivethirtyeight')

axe_x = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20']


"""
plt.plot(axe_x, axe_y, color='b', linestyle='-',marker='o', linewidth ='3',label='The first population')

plt.plot(axe_x, axe_y2, color='r', linestyle='-', marker='o', linewidth ='3', label="The final population")

#plt.plot(axe_x, axe_y3, color='g', linestyle='-', marker='o', linewidth ='3', label="Best population")

plt.ylim(0, 70)
plt.xlabel('Solutions')
plt.ylabel('Cycle times')
plt.title('The Simple Genetique algorithme')

plt.legend()
#plt.grid()
plt.tight_layout()
plt.show()
"""
N = 20
first = axe_y
final = axe_y2
        
ind = np.arange(N) 
width = 0.35       
plt.bar(ind, first, width, label='Initial population (GRASP solutions)')
plt.bar(ind + width, final, width, label='Final population')

plt.ylabel('Cycle time')
plt.title('GRASP_Genetic_Algorithm')

plt.xticks(ind + width / 2, ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20'))
plt.legend(loc='best')
plt.show()