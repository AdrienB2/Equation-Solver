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
# liste des zeros
liste_zero = []



### Fonctions

# la fonction f qu'on veut avoir pour une valeur unique (float)
def func(x):
    # Définition de la fonction ici
    try:
        return np.sin(x)
    except:
        return "Erreur"



# le h va déterminer l'ordre de précision de la dérivée
# h = 0.000000000001 est la plus petite valeur que Python supporte
h = 0.000000000001
# la dérivée
def derivative(f, x):
    # utilisation de la définition de la dérivée avec la limite ; f'(a) = lim h->0 ((f(a + h) - f(a))/h)
    f1 = f(x)
    f2 = f(x + h) 
    fDerivee = (f2 - f1)/h  
    return fDerivee



# fonction qui trouve les 0 avec la méthode de Newton-Raphson
def newtonRaphson(f, a):
    # "a" est point autour duquel la tangente se fait
    anti_bug = 0        # possibilité d'osciller entre deux points
    try:
        # tant que la valeur f(a) n'est pas proche de 0 (ou que anti-bug est trop élevé)
        while abs(f(a)) > h/100 and anti_bug < 10000:
            # si la dérivée est nulle, retourne une erreur
            if abs(derivative(f, a)) == 0:
                return "Erreur"
            # si la dérivée est pas nulle, il est possible de faire la méthode de Newton-Raphson
            else:
                # comme on l'a vu en classe : f(a)+f'(a)*(x-a) = 0  =>  (-f(a)/f'(a)) + a = x
                a = -f(a)/derivative(f, a) + a
                # incrémentation de l'anti-bug
                anti_bug += 1
        # si il n'y a pas d'oscillation
        if anti_bug < 10000:
            # si on arrive ici, alors ça veut dire que f(a) est nulle, donc c'est un zero
            return a
        # si il y a une oscillation, retourne une erreur
        else:
            return "Erreur"

    # si le code n'arrive pas à déterminer f(a), ou f'(a)
    except:
        # essaie comme zero de la fonction le 0 (plus probable des zeros)
        if f(0) == 0:
            return 0
        # sinon, retourne une erreur
        else:
            return "Erreur"


# determine la liste de zeros (pas tous mais la plupart)
def detListeZero():
    global liste_zero
    for x in range(-20,21):
        x = x/2
        a = newtonRaphson(func, x)
        if a != "Erreur":
            if len(liste_zero) == 0:
                liste_zero.append(a)
            else:
                removed = True
                for zero in liste_zero:
                    if abs(zero-a) < 2*h:
                        try:
                            if func(zero) >= func(a):
                                liste_zero.remove(zero)
                                if abs(a-round(a)) < h or abs(round(a)-a) < h:
                                    liste_zero.append(round(a))
                                else:
                                    liste_zero.append(a)
                                removed = False
                                break
                            removed = False
                        except:
                            removed = False
                            break
                if removed:
                    liste_zero.append(a)

detListeZero()
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
plt.plot(x, func(x), 'y', label="f(x)")
plt.legend(loc='upper left')

# affiche la fenêtre des graphes
plt.show()