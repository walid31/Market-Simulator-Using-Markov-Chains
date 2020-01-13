import numpy as np
import matplotlib.pyplot as plt

a_val,b_val,c_val = [],[],[]

# initial state
init_state = np.array([188969, 81356, 14210])

# transition matrix
a = np.array([[ 0.89, 0.75 ,0.49], [ 0.10, 0.22 ,0.44], [ 0.01, 0.03 ,0.07]])

for x in range(10):
    a_val.append(init_state[0])
    b_val.append(init_state[1])
    c_val.append(init_state[2])
    b = init_state
    init_state = a.dot(b)

# plotting
plt.figure(figsize=(11,8))
plt.plot( [x for x in range(10)], a_val, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4,label='Inactive users')
plt.plot( [x for x in range(10)], b_val, marker='o', markerfacecolor='red', markersize=12, color='pink', linewidth=4,label='Active users')
plt.plot( [x for x in range(10)], c_val, marker='o', markerfacecolor='orange', markersize=12, color='yellow', linewidth=4,label='Very active users')
plt.legend(loc='best')
plt.xlabel('Months')
plt.ylabel('Number of customers')

# CHANGES TO INITIAL STATE - NUMBERS RECEIVED FROM MATRIX VECTOR PRODUCT

before = (855,130,15) # Without any change
after = (509,389,102) # After placing deal

# create plot
plt.figure(figsize=(11,8))
index = np.arange(3)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, before, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Without deal')
 
rects2 = plt.bar(index + bar_width, after, bar_width,
                 alpha=opacity,
                 color='g',
                 label='With deal')
 
plt.xlabel('Segments')
plt.ylabel('Number of Users')
plt.title('Customer behavior after a month')
plt.xticks(index + bar_width- 0.18, ('Inactive','Active','Very Active'))
plt.legend()
 
plt.tight_layout()
plt.show()

