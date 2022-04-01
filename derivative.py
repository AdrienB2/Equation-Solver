### import des librairies utiles : tkinter et math
from http.client import EXPECTATION_FAILED
import math as math
import matplotlib.pyplot as plt
import numpy as np
 

### fonction et dérivée

# la fonction f qu'on veut avoir, dépend de la valeur x entrée
def func(x):
    # Définition de la fonction ici
    try:
        return math.log(x)
    except:
        return "Pas trouvé"

# la fonction f qu'on veut avoir pour matplotlib, dépend de la valeur x entrée
def f(x):
    # Définition de la fonction ici pour numpy (pour faire un beau graphe)
    return np.log(x)

# le h va déterminer l'ordre de précision de la dérivée
h = 0.000000000001
# la dérivée, qui va dépendre de la fonction f et de la valeur entrée x
def derivative(f, x):
    # utilisation de la définition d'une dérivée ; lim h->0 {(f(a+h)-f(a)/h)}
    f1 = f(x)           #f(a)
    f2 = f(x+h)            #f(a+h), h = 0.000000000001, plus petite valeur que Python supporte
    f_deriv = (f2-f1)/h       #dérivée en x par définition
    return f_deriv


def find_zero(f, a):
    # "a" est point autour duquel la tangente se fait
    try:
        while abs(f(a)) > h:
            if abs(derivative(f, a)) < h:
                return ZeroDivisionError
            else:
                a = -f(a)/derivative(f, a) + a
        return a
    except:
        if f(0) == 0:
            return 0
        else:
            return "\n \n Erreur du point choisi, essayez un autre point !! \n \n"
    
        


plt.style.use("dark_background") # fond noir car c'est plus stylax


# borne entre lesquelles la fonction sera affichée
borneInf = -10
borneSup = 10
d = 100000      # nombres de x vérifiés dans le graphe

a = find_zero(func, 1)
print(a, func(a))
# crée n éléments (inversement proportionnel à d) qu'on va plot dans la fonction entre les bornes choisies
x = np.linspace(borneInf, borneSup, d)

# création des axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position(('data', 0)) # la commande 'data' permet de positionner correctement les axes par rapport à la fonction
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


# plot les fonctions
plt.plot(x, f(x), 'y', label='f(x)')
#plt.plot(x, derivative(f, x), 'c', label="f'(x)")
plt.legend(loc='upper left')

# affiche la fenêtre des graphes
plt.show()