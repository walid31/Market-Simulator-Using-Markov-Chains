import numpy as np
import matplotlib.pyplot as plt

a_val,b_val,c_val = [],[],[]

# etat inital
etat_initial = np.array([188969, 81356, 14210])

# matrice de transition
a = np.array([[ 0.89, 0.75 ,0.49], [ 0.10, 0.22 ,0.44], [ 0.01, 0.03 ,0.07]])

for x in range(10):
    a_val.append(etat_initial[0])
    b_val.append(etat_initial[1])
    c_val.append(etat_initial[2])
    b = etat_initial
    etat_initial = a.dot(b)

# plotting
plt.figure(figsize=(11,8))
plt.plot( [x for x in range(10)], a_val, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4,label='Utilisateur Inactif')
plt.plot( [x for x in range(10)], b_val, marker='o', markerfacecolor='red', markersize=12, color='pink', linewidth=4,label='Utilisateur Actif')
plt.plot( [x for x in range(10)], c_val, marker='o', markerfacecolor='orange', markersize=12, color='yellow', linewidth=4,label='Utilisateur Tres Actif')
plt.legend(loc='best')
plt.xlabel('Mois')
plt.ylabel('Nombre de clients')

# CHANGEMENTS À L'ÉTAT INITIAL

avant = (855,130,15) # Sans aucun changement
apres = (509,389,102) # Après avoir conclu un accord

# create plot
plt.figure(figsize=(11,8))
index = np.arange(3)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, avant, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Sans accord')
 
rects2 = plt.bar(index + bar_width, apres, bar_width,
                 alpha=opacity,
                 color='g',
                 label='avec accord')
 
plt.xlabel('Segments')
plt.ylabel('Nombre de clients')
plt.title('Le comportement du client après un mois')
plt.xticks(index + bar_width- 0.18, ('Inactif','Actif','Tres Actif'))
plt.legend()
 
plt.tight_layout()
plt.show()

