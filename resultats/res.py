import matplotlib.pyplot as plt
import numpy as np
"""
plt.plot([1, 1.5 , 2, 2.5,  3, 3.5, 4], [1, 2.5, 4, 6,  9, 12, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.ylabel('some numbers')
plt.show()"""

"""
t= np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t*2, 'bs', t, t**3, 'g^')
plt.show()"""

"""
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()"""

"""
plt.style.use('fivethirtyeight')

axe_x = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20']
#first_population_simple_GA
axe_y = [48.0, 51.0, 47.5, 50.0, 47.5, 47.5, 50.0, 51.0, 48.0, 50.0, 51.0, 52.5, 51.0, 50.0, 52.5, 51.0, 53.5, 56.0, 47.5, 48.0]

#final_population_simple_GA
axe_y2 = [45.5, 45.5, 47.5, 51.0, 53.5, 50.0, 52.0, 48.0, 50.0, 50.0, 51.0, 45.5, 47.5, 48.0, 51.0, 47.5, 47.5, 55.5, 53.5, 51.0]


plt.plot(axe_x, axe_y, color='b', linestyle='-', linewidth ='3',label='The first population')

plt.plot(axe_x, axe_y2, color='r', linestyle='-', marker='o', linewidth ='3', label="The final population")
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
first = [52.5, 48.5, 48.5, 49.0, 48.5, 49.5, 48.0, 49.0, 52.5, 48.0, 48.0, 49.0, 48.0, 48.5, 51.0, 48.5, 48.5, 48.0, 52.0, 48.5]
final = [47.5, 48.0, 48.0, 48.0, 47.5, 48.0, 48.0, 48.0, 47.5, 47.5, 48.0, 47.5, 48.0, 47.5, 48.0, 48.0, 47.5, 48.0, 48.0, 48.0]
        
ind = np.arange(N) 
width = 0.35       
plt.bar(ind, first, width, label='Solutions')
plt.bar(ind + width, final, width, label='Neighborhoods')

plt.ylabel('Cycle time')
plt.title('GRASP')

plt.xticks(ind + width / 2, ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20'))
plt.legend(loc='best')
plt.show()