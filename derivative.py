### Import des librairies utiles : math, nummpy et matplotlib, tkinter
import math as math
import matplotlib.pyplot as plt
import numpy as np



### Variables

# le h va déterminer l'ordre de précision de la dérivée
h = 0.000000000001
# borne entre lesquelles la fonction sera affichée
borneInf = -5
borneSup = 5
# nombres de x vérifiés dans le graphe
d = 100000
a = 0



### Fonctions

# la fonction f qu'on veut avoir pour une valeur unique (float)
def func(x):
    # Définition de la fonction ici
    try:
        return x**6+5*x**5-4*x**4+2*x**3-100*x**2-x-10
    except:
        return "Erreur"

# la fonction f qu'on veut avoir avec numpy (sous forme d'array)
def f(x):
    # définition de la fonction ici pour numpy (pour faire un beau graphe)
    return x**6+5*x**5-4*x**4+2*x**3-100*x**2-x-10


# le h va déterminer l'ordre de précision de la dérivée
h = 0.000000000001
# la dérivée
def derivative(f, x):
    # utilisation de la définition de la dérivée avec la limite ; f'(a) = lim h->0 ((f(a + h) - f(a))/h)
    f1 = f(x)
    f2 = f(x + h) # h = 0.000000000001 est la plus petite valeur que Python supporte
    fDerivee = (f2 - f1)/h  
    return fDerivee



# fonction qui trouve les 0
def findZero(f, a):
    # "a" est point autour duquel la tangente se fait
    anti_bug = 0
    try:
        while abs(f(a)) > h and anti_bug < 10000:
            if abs(derivative(f, a)) < h:
                return "Erreur"
            else:
                a = -f(a)/derivative(f, a) + a
                anti_bug += 1
                print(anti_bug)
        return a
    except:
        if f(0) == 0:
            return 0
        else:
            return "Erreur"



liste_zero = []
for x in range(-20,21):
    x = x/2
    a = findZero(func, x)
    if a != "Erreur":
        if len(liste_zero) == 0:
            liste_zero.append(a)
        else:
            removed = True
            for zero in liste_zero:
                if abs(zero-a) < 2*h:
                    if func(zero) >= func(a):
                        liste_zero.remove(zero)
                        liste_zero.append(a)
                        removed = False
                        break
                    removed = False
            if removed:
                liste_zero.append(a)

print(liste_zero)


### Graphe

plt.style.use("dark_background") # fond noir car c'est plus stylax
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
plt.plot(x, f(x), 'y', label="f(x)")
plt.legend(loc='upper left')

# affiche la fenêtre des graphes
plt.show()