import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)

fig = plt.figure() # initialise la figure
line, = plt.plot([], []) 
plt.xlim(xmin, xmax)
plt.ylim(-1, 1)

def init():
    line.set_data([], [])
    return line,

def animate(i): 
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, 
                              interval=1, blit=True, repeat=True)

plt.show()



def F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif):
        print("coucou1")
        if type_case != 0 and nb_recursif > 1:
            print("coucou")
            while ressources == "":
                val_ressource = random.randint(0, 1400)
                
                if val_ressource > 0 and val_ressource <= val_max_ressources[0] :
                    if type_case in [6]:
                        ressources = liste_ressources[0]
                        couleur = "olivedrab"
                        forme = "cercle"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 100 and val_ressource <= val_max_ressources[1] :
                    if type_case in [1]:
                        ressources = liste_ressources[1]
                        couleur = "yellowgreen"
                        forme = "cercle"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 200 and val_ressource <= val_max_ressources[2] :
                    if type_case in [1,3,4]:
                        ressources = liste_ressources[2]
                        couleur = "black"
                        forme = "carre"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 300 and val_ressource <= val_max_ressources[3]:
                    if type_case in [1]:
                        #ressources = liste_ressources[3]
                        #couleur = "saddlebrown"
                        #forme = "cercle"
                        ### remplacer par betail => 
                        ressources = liste_ressources[1]
                        couleur = "yellowgreen"
                        forme = "cercle"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 400 and val_ressource <= val_max_ressources[4]:
                    if type_case in [6]:
                        ressources = liste_ressources[4]
                        couleur = "aquamarine"
                        forme = "cercle"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 500 and val_ressource <= val_max_ressources[5]:
                    if type_case in [1,3,4]:
                        ressources = liste_ressources[5]
                        couleur = "red"
                        forme = "carre"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 600 and val_ressource <= val_max_ressources[6]:
                    if type_case in [3,4]:
                        ressources = liste_ressources[6]
                        couleur = "royalblue"
                        forme = "carre"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 700 and val_ressource <= val_max_ressources[7]:
                    if type_case in [3, 4]:
                        ressources = liste_ressources[7]
                        couleur = "red"
                        forme = "cercle"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 800 and val_ressource <= val_max_ressources[8]:
                    if type_case in [1,3,4]:
                        ressources = liste_ressources[8]
                        couleur = "gold"
                        forme = "carre"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 900 and val_ressource <= val_max_ressources[9]:
                    if type_case in [1,2,3,5,6]:
                        ressources = liste_ressources[9]
                        couleur = "black"
                        forme = "etoile"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 1000 and val_ressource <= val_max_ressources[10]:
                    if type_case in [2,5]:
                        ressources = liste_ressources[10]
                        couleur = "violet"
                        forme = "cercle"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 1100 and val_ressource <= val_max_ressources[11]:
                    if type_case in [1,2,3,5]:
                        ressources = liste_ressources[11]
                        couleur = "red"
                        forme = "etoile"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 1200 and val_ressource <= val_max_ressources[12]:
                    if type_case in [1,2,3,4,5,6]:
                        ressources = liste_ressources[12]
                        couleur = "gold"
                        forme = "etoile"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                elif val_ressource > 1300 and val_ressource <= val_max_ressources[13]:
                    if type_case in [1,2,3,5]:
                        ressources = liste_ressources[13]
                        couleur = "snow"
                        forme = "etoile"
                    else:
                        ressources,couleur,forme = F_type_case_recursif(type_case, val_max_ressources, liste_ressources, nb_recursif-1)
                else:
                    ressources = liste_ressources[14]
            if ressources != "vide":    
                ressources_generees.append([ressources,idx,idy])    
