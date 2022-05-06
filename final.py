### Import des librairies utilisée par le programme
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math as math
from matplotlib.axis import Axis
from numpy import e, sin, cos, tan, sqrt
from cmath import nan


####################
#VARIABLES GLOBALES#
####################
# variable contenant la fonction en string
function = ""
# liste des zeros
liste_zero = []
# borne entre lesquelles la fonction sera affichée
borneInf = -5
borneSup = 5



#####################
#CONSTANTES GLOBALES#
#####################
# nombres de x vérifiés dans le graphe
d = 10000
# le h va déterminer l'ordre de précision de la dérivée
# h = 0.000000000001 est la plus petite valeur que Python supporte
h = 0.000000000001
# liste des operations/fonctions/constantes
operations=["+","-","*","/","^", "√","∛", "∜","sin","cos","tan", "π", "log","ln","exp", "abs"]

###########
#FONCTIONS#
###########

# la fonction f dont on cherche les zéros
def f(x):
    # global permet d'avoir partout la même référence à la variable "function" 
    global function
    # Essaie de calculer f(x) (en fonction du x)
    try:
        return eval(function)
    # Si il n'y arrive pas (par exemple lors de division par 0), le code retourne un "Not a Number", ce qui permet au programme de continuer sans erreurs
    except:
        return nan


# fonction qui calcule la dérivée de f en x
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
        while abs(f(a)) > h/1000 and anti_bug < 10000:
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
        if anti_bug < 10000 and abs(f(a)) < h/1000:
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

# méthode de dichotomie, la fonction retourne un zero de la fonction
def dichotomie(f, a, b, prec):
    #a < b par convention et prec représente la précision de la solution en décimales

    # Etape 1: On vérifie si f(a) et f(b) ne sont pas des zéros, ou qu'ils sont impossibles
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    if f(a) == "Erreur" or f(b) == "Erreur":
        return "Erreur des valeurs choisies (une des valeurs est impossible)"


    # Etape 2: on vérifie que le signe de f(a) et f(b) n'est pas le même
    if abs(f(a))/f(a) == abs(f(b))/f(b):
        # Etape 2.1: on ajoute -1 à a ou +1 à b pour trouver des signes de f(a) et f(b) différents 
        anti_bug = 0
        while anti_bug < 10000:
            a -= 1
            b += 1
            try:
                if f(a) == 0:
                    return a
                    
                elif f(b) == 0:
                    return b

                elif abs(f(a))/f(a) != abs(f(b))/f(b):
                    break

            except:
                a -= 1
                b += 1

            anti_bug += 1
        if anti_bug == 10000:
            print("Erreur des valeurs choisies (RunTimeError)")

    # Etape 3: méthode de dichotomie, si abs(f(x)) < 10^(-précision) alors on arrête la boucle et on retourne x
    try:
        while abs(f((a+b)/2))>(10**(-prec)):
            if f((a+b)/2)<0:
                if f(a) < 0:
                    a = (a+b)/2
                else:
                    b = (a+b)/2
            else:
                if f(a) > 0:
                    a = (a+b)/2
                else:
                    b = (a+b)/2
        return (a+b)/2
    except:
        return "Erreur, la fonction est pas continue"

# fonction qui détermine les zeros de f avec la méthode Newton-Raphson (a refaire)
def detListeZero():
    global liste_zero
    for x in range(-20,21):
        x = x/2
        a = newtonRaphson(f, x, 0)
        if a == "Erreur":
            return

        if len(liste_zero) == 0:
            liste_zero.append(a)
        else:
            removed = True
            for zero in liste_zero:
                if abs(zero-a) < 2*h:
                    try:
                        if f(zero) >= f(a):
                            liste_zero.remove(zero)
                            print(round(a))
                            if abs(a-round(a)) < 2*h or abs(round(a)-a) < 2*h:
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

###########
#INTERFACE#
###########

# fonciton exectutée lorsque l'utilisateur clique sur le bouton "calculer", pour déterminer les zeros de f
def solve():
    value = functionInput.get()

# fonction exectutée lorsque l'utilisateur clique sur un bouton qui modifie la fonction, pour actualiser la fonction dans la variable et l'afficher
def update_function(stringToAdd):
    # global permet d'avoir partout la même référence à la variable "function" 
    global function
    
    if stringToAdd in ["+", "-", "*", "/", "^"] and function[-1] in  ["+", "-", "*", "/", "^"]:
        return

    if stringToAdd == "DEL":
        function = function[:-1]
    else:
        function += stringToAdd
    if stringToAdd in ["sin","cos","tan","log","ln","exp","abs","√","∛", "∜"]:
        function += "("
    functionInput.delete(0,END)
    functionInput.insert(0,function)
    update_graph()

# fonction appelée losque l'utilisateur modifie le champs de texte de la fonciton
def inputChange():
    global function
    function = functionInput.get()
    update_graph()

# fonction qui actualise l'afficahge du graphique
def update_graph():
    x = np.linspace(borneInf, borneSup, d)
    plt.cla()
    plt.plot(x, f(x), 'y', label="f(x)")
    plt.legend(loc='upper left')
    ax.spines['left'].set_position(('data', 0)) # la commande 'data' permet de positionner correctement les axes par rapport à la fonction
    ax.spines['bottom'].set_position(('data', 0))
    canvas.draw()

# Afficahger de l'interface
root = Tk() # création de la fenêtre
root.title("Equation Solver") # titre de la fenêtre
root.state('zoomed') # fenêtre maximisée

root.columnconfigure(1, weight=1) # permet à la colone contenant le grphique de prendre toute la largeur de la fenêtre
root.rowconfigure(0, weight=1) # permet à la ligne du haut de prendre toute la hauteur de la fenêtre

leftFrame = Frame(root)
leftFrame.grid(row=0, column=0)

methode = StringVar()
methode.set("méthode de résolution")
methodeMenu = OptionMenu(leftFrame, methode, "Newton-Raphson", "Dichotomie")
methodeMenu.pack(side=TOP, fill=X)

functionInputFrame = Frame(leftFrame)
functionInputFrame.pack(fill=X, side=TOP)

functionLabel = Label(functionInputFrame, text="f(x) = ")
functionLabel.pack(side=LEFT)
functionInput = Entry(functionInputFrame)
functionInput.pack(side=RIGHT, fill=X)
functionInput.bind("<KeyRelease>", lambda event: inputChange())


calculer = Button(leftFrame, text="Calculer", command=solve)
calculer.pack(side=TOP, fill=X)

graphFrame = Frame(root)
graphFrame.grid(row=0, column=1, sticky=N+S+E+W)


bottomFrame = Frame(root)
bottomFrame.grid(row=1, column=0, columnspan=2)

#Boutons pour les chiffres de 0 à 9
#affichage des boutons de 1 à 9
for i in range(3):
    for j in range(3):
        Button(bottomFrame, text=str(i*3+j+1), command=lambda x=str(i*3+j+1): update_function(x), font=("Helvetica",20)).grid(row=i, column=j)
#affichage des boutons de 0
Button(bottomFrame, text="0", command=lambda: update_function("0"), font=("Helvetica",20)).grid(row=3, column=0, columnspan=2, sticky='ew')
#bouton pour la virgule
btnDot = Button(bottomFrame, text=".", command=lambda: update_function("."), font=("Helvetica",20))
btnDot.grid(row=3, column=2, sticky='ew')

#juste pour avoir une marge entre les chiffre et les opérations
Label(bottomFrame, text=" ").grid(row=0, column=3, sticky='ew', padx=5)

#création des boutons pour les opérations
for i in range(4):
    for j in range(4):
        Button(bottomFrame, text=operations[i+4*j], command=lambda x=operations[i+4*j]: update_function(x), font=("Helvetica",20)).grid(row=i, column=j + 4, sticky='ew')
Button(bottomFrame, text="←", command=lambda: update_function("DEL"), font=("Helvetica",20)).grid(row=3, column=8, sticky='ew')
#creation des boutons x, (,)
Button(bottomFrame, text="x", command=lambda: update_function("x"), font=("Helvetica",20)).grid(row=0, column=8, sticky='ew')
Button(bottomFrame, text="(", command=lambda: update_function("("), font=("Helvetica",20)).grid(row=1, column=8, sticky='ew')
Button(bottomFrame, text=")", command=lambda: update_function(")"), font=("Helvetica",20)).grid(row=2, column=8, sticky='ew')

def sqrt(x):
    return x**(1/2)
def cbrt(x):
    return x**(1/3)
def root4(x):
    return x**(1/4)

def f(x):
    try:
        functionFormated = function.replace("^", "**").replace("√", "sqrt").replace("∛", "cbrt").replace("∜", "root4").replace("sin", "np.sin").replace("cos", "np.cos").replace("tan", "np.tan").replace("log", "np.log10").replace("ln", "np.log").replace("exp", "np.exp").replace("abs", "abs").replace("π", "np.pi")
        return eval(functionFormated)
    except:
        return 0

plt.style.use("dark_background") # fond noir pour le graphe
plt.ion() # on active l'affichage en temps réel
# crée n éléments (inversement proportionnel à d) qu'on va plot dans la fonction entre les bornes choisies
x = np.linspace(borneInf, borneSup, d)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position(('data', 0)) # la commande 'data' permet de positionner correctement les axes par rapport à la fonction
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# plot les fonctions
plt.plot(x, x, 'y', label="f(x)")
plt.legend(loc='upper left')

# creation du canvas pour le graphe
canvas = FigureCanvasTkAgg(fig, master = graphFrame)  
canvas.draw()

# affichage du graphe
canvas.get_tk_widget().pack(fill=BOTH, expand=1)


root.mainloop()