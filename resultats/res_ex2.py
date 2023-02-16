import matplotlib.pyplot as plt

names = ['W1','W2','W3','W4']
#values = [48.0, 51.0, 47.5, 50.0, 47.5, 47.5, 50.0, 51.0, 48.0, 50.0, 51.0, 52.5, 51.0, 50.0, 52.5, 51.0, 53.5, 56.0, 47.5, 48.0]
#values = [44, 46, 20, 36]
#values = [42, 3, 38, 54]
values = [43, 43, 44, 45]
#values = [8, 8, 8, 8, 8, 8, 9, 9, 8, 8]
#plt.bar(x, , bottom=None,  align='center', data=None, **kwargs)
#plt.figure(figsize=(15, 3))


plt.bar(names, values, width=0.3)
plt.ylim(0, 60)


plt.xlabel('Workstations')
plt.ylabel('Time')
plt.suptitle('Average Workload')


plt.show()