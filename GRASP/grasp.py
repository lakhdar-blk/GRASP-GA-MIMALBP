import  graph   as gr
import random



#HEURISTICS
class Heuristics:

    #list    =   []


    #task time priority rule
    def priority_rule_01(l):

        or_l    = []
        max_t   = gr.G.nodes[l[0]]["task"+str(l[0])]
        t       = l[0]


        while(l):

            for i in l :

                if (gr.G.nodes[i]["task"+str(i)] > max_t):
                    
                    max_t = gr.G.nodes[i]["task"+str(i)]
                    t = i

            or_l.append(t)
            l.remove(t)   
            max_t = 0 

        return or_l

    #ranked positiona  weight:
    def priority_rule_02(l):

        or_l    =  []
        #sum_t   =   gr.G.nodes[l[0]]["task"+str(l[0])] #initialise sum_t with the task time
        sum_t = 0
    
        #ls = list(gr.G.successors(l[0])) #ls : list of successors of the first element of RCL
        ls =  gr.nx.nodes(gr.nx.dfs_tree(gr.G, l[0]))
        #print(ls)
        for j in ls:

                sum_t   = sum_t + gr.G.nodes[j]["task"+str(j)] #calcule of the positional weight of the fisrt element            

        max_w   =   sum_t #initialise the max_w with sum_t
        sum_t   = 0
        t       =  l[0]
        
        while(l):


            for i in l:

                #ls = list(gr.G.successors(i))
                ls =  gr.nx.nodes(gr.nx.dfs_tree(gr.G, i))
                print("ls",ls)
                #sum_t   =   gr.G.nodes[i]["task"+str(i)]

                for j in ls:
                    sum_t   = sum_t + gr.G.nodes[j]["task"+str(j)]

                print("sum_t:",sum_t,"max_w:",max_w) 

                if(sum_t > max_w):

                    max_w = sum_t
                    t = i

                sum_t = 0

           
            or_l.append(t)
            l.remove(t)   
            sum_t = 0 
            max_w = 0
            

        
        return or_l
    

    #def priority_rule():

    #def priority_rule():

    #def priority_rule():

#GRASP
class Grasp:

    iterations  =   0 #no detrmined
    alpha       =   0 #used to determine the number of elements in the RCL

    """
    def __init__(self, i, a):

        self.iterations =   i
        self.alpha      =   a
    """

    def construction_phase(self, c, n, l_tasks, a):

        
        CL              =   l_tasks                             #Candiate list
        #OR_CL           =   [1, 3, 2, 4]                       #Applaying the priority rule 
        no_sol          =   True
        alpha           =   a
        init_c_time     =   c                                   #initialisation of the cycle time (max task time)
        liste   =   []

        while(no_sol):
                                     
            RCL             =   []                              #Retricted candidate list
            solution        =   []
            wr_time         =   init_c_time                     #workstation time
            num_wr          =   1                               #number of workstation
        
            while(True):

                i   =   0                                       #counter used to check the number of chosen elements for RCL

                    #task (succesors already assigned, and time task doesn't exceed the time of the current workstation):
                for a in CL:   

                    check   =   any(item in list(gr.G.predecessors(a)) for item in CL)

                    if((not check) and (gr.G.nodes[a]["task"+str(a)] <= wr_time)):

                            liste.append(a)

                if(liste):           
                    print("liste:", liste)
                    liste = Heuristics.priority_rule_02(liste)
                    #liste = Heuristics.priority_rule_01(liste)
                    RCL = liste[0:alpha]
                    liste = []    
                """            
                        if(i<alpha):

                            #print(list(gr.G.predecessors(a)))            
                            check   =   any(item in list(gr.G.predecessors(a)) for item in CL)
                        
                            if((not check) and (gr.G.nodes[a]["task"+str(a)] <= wr_time)):  

                                
                                RCL.append(a)
                                i   =   i   +   1 
                                print("i:",i)   
                                
                        else:

                            break

                i   =   0
                """
                print("RCL:",RCL)
                
                if(RCL):

                        while(RCL):

                                #RCL = Heuristics.priority_rule_01(RCL)
                                #RCL = Heuristics.priority_rule_02(RCL)
                                #print("ORCL:",RCL)
                                s           =   random.choice(RCL)                          #randome choice
                                #s = RCL[0]
                                if(gr.G.nodes[s]["task"+str(s)] <= wr_time):
                                    print("choice:", s)
                                    solution.append(s)                                          #add s to solution
                                    CL.remove(s)        #remove s from CL
                                    RCL.remove(s)                                                
                                    print("CL:",CL)   
                                    print(s)
                                    print(wr_time)                                       
                                    wr_time     =   wr_time - gr.G.nodes[s]["task"+str(s)]      #update workstation time
                                    print(wr_time)
                                    #input()
                                                                             #clean RCL
                                
                                #if there no availabe time in the current workstation we pass to the next one
                                elif( gr.G.nodes[s]["task"+str(s)] >  wr_time or wr_time == 0):                                           
                                            
                                    num_wr  =   num_wr + 1
                                    wr_time = init_c_time
                                    solution.append(s)                                          #add s to solution
                                    CL.remove(s)        #remove s from CL
                                    RCL.remove(s)                                                
                                    print("CL:",CL)   
                                    print(s)
                                    print(wr_time)                                       
                                    wr_time     =   wr_time - gr.G.nodes[s]["task"+str(s)]  

                                    #RCL         =   [] 
                                #verify if OR_CL is empty
                                if (not CL):
                                
                                    print("final c:",init_c_time)
                                
                                    return solution, init_c_time


                              

                                #next workstation
                else:
                            print("station: ", solution )  
                            wr_time     =   init_c_time                             
                            num_wr      =   num_wr  +   1
            
                #if the num_wr is exceeded we in increment the cycle time and reset the num_wr
                if (num_wr > n):

                            init_c_time     =   init_c_time + 0.5
                            #CL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
                            CL = [1,2,3,4,5,6,7,8,9,10,11,12]
                            print("-------------new")
                            break


    def local_search_phase(self, solution, ct, work_s):

        #temp_list = solution.copy()
        nbw = 1
        stock = []
        limit = 0

        while(True):

                
                c_init = 25

                while(limit < 60):

                    temp_list = solution.copy()
                    while(True):

                        key = True
                        i = random.choice(temp_list)  
                        #print(gr.nx.nodes(gr.nx.dfs_tree(gr.G, i, orientation='reverse')))


                        while(True):
                            
                            j = random.choice(temp_list)
                            if (j != i):
                                break

                                
                        print("i:",i," index:", temp_list.index(i))
                        print("j:",j," index:", temp_list.index(j))


                        t1 = i
                        t2 = j
                        print("t1: ",t1," t2: ",t2)    
                        
                        x = temp_list.index(i)
                        y = temp_list.index(j) 
                        print("x: ",x," y: ",y) 
                        
                        if( temp_list.index(i) < temp_list.index(j)):
                            
                            if(i not in gr.nx.nodes(gr.nx.bfs_tree(gr.G, j, reverse=True))):
                                
                                for a in temp_list[temp_list.index(i)+1:temp_list.index(j)]:
                                    
                                    if(i in gr.nx.nodes(gr.nx.bfs_tree(gr.G, a, reverse=True)) or a in gr.nx.nodes(gr.nx.bfs_tree(gr.G, j, reverse=True))):
                                        key = False
                                        continue

                                if(key == True):
                                    
                                    temp_list[x] = t2
                                    temp_list[y] = t1

                                    
                                    print("bingo 1")
                                    break
                                

                        else:

                            if(j not in gr.nx.nodes(gr.nx.bfs_tree(gr.G, i, reverse=True))):
                            
                                for a in temp_list[temp_list.index(j)+1:temp_list.index(i)]:
                                    
                                    if(j in gr.nx.nodes(gr.nx.bfs_tree(gr.G, a, reverse=True)) or a in gr.nx.nodes(gr.nx.bfs_tree(gr.G, i, reverse=True)) ):
                                        key = False
                                        break
                                
                                if(key == True):
                                    
                                    temp_list[x] = t2
                                    temp_list[y] = t1

                                    
                                    print("bingo 2")
                                    break

                    if(temp_list not in stock):
                        stock.append(temp_list)
                        break
                    
                    limit = limit + 1
                print(limit) 
                 

                        
                
               

                while nbw != work_s :

                    c = c_init
                    t_tab = []

                    for j in range(len(temp_list)):

                        a = temp_list[j]

                        if(c >= gr.G.nodes[a]["task"+str(a)]):
                            c = c - gr.G.nodes[a]["task"+str(a)] 
                            t_tab.append(a)
                                                                                                                                                            
                            #print("task:",a," Opt : ",G.nodes[a]["task"+str(a)])

                        else :
                            print("station :",t_tab)
                            t_tab = []
                            t_tab.append(a)
                            nbw = nbw + 1
                            c = c_init
                            c = c - gr.G.nodes[a]["task"+str(a)]

                    print("station :",t_tab)

                    if (nbw != work_s):
                        print("--------------------new sol")
                        c_init = c_init + 0.5
                        c = c_init 
                        nbw = 1  
                    
                print(temp_list)                                                                                                         
                print("new c : ", c_init) 
                #input()
                
                best_ct = 100

                if(c_init < ct or limit >= 60):

                    if(c_init < best_ct):
                        """
                        print(stock)
                        print("new optimal neighborhood solution with c = ", c_init)
                        input()
                        return temp_list, c_init
                        """
                        best_solution = temp_list
                        best_ct = c_init


                    if(limit >= 60):

                       
                        if(ct > best_ct):
                            return best_solution, best_ct
                        else:
                            print(stock)
                            return solution, ct
                    #print(stock)
                    #break        
                nbw = 1    






                        
                 


obj1 = Grasp()
#ts_list = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


for i in range(6):

    final_sol = []

    it = 0
    final_cycle_time = 100

    while(it<10):
        ts_list = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12]
        sol, c  = obj1.construction_phase(25, 4, ts_list, 3)
        
        print("sol:",sol," c:",c)
        #input()
        pre_final_sol, pre_c = obj1.local_search_phase(sol, c, 4)
        #print("l :",l)
        #print("nei_list:",nei_list)
        #input()

        
        if(pre_c < final_cycle_time):
            old_sol = sol
            old_c = c
            final_cycle_time = pre_c
            final_sol = pre_final_sol
            """
            print("old solution:", old_sol)
            print("with old cycle time:", old_c)
            print("the final optiaml sequence : ", final_sol)
            print("with cycle time = ", final_cycle_time)
            """
        it = it + 1 
        print("it : ",it)

        

    print("----------------------start------------------")
    print("old solution:", old_sol)
    print("with old cycle time:", old_c)
    print("the final optiaml sequence : ", final_sol)
    print("with cycle time = ", final_cycle_time)
    print("----------------------END------------------")
    input()