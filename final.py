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
# borne entre lesquelles la fonction sera affichée
borneInf = -100
borneSup = 100



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


# méthode de dichotomie, la fonction retourne un zero de la fonction (à améliorer / commentaires)
def dichotomie(f, a, b):
    # a < b par convention

    # Etape 1: On vérifie si f(a) et f(b) ne sont pas des zéros, ou qu'ils sont impossibles
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    if f(a) == nan or f(b) == nan:
        return nan


    # Etape 2: on vérifie que le signe de f(a) et f(b) n'est pas le même
    if abs(f(a))/f(a) == abs(f(b))/f(b):
        # Etape 2.1: on ajoute -1 à a ou +1 à b pour trouver des signes de f(a) et f(b) différents 
        anti_bug = 0    # variable anti_bug évite les cas où la fonction ne change pas de signe
        while anti_bug < 10000:
            # on cherche un nombre a et un nombre b tels que signe(f(a)) n'est pas égal à signe(f(b)) 
            a -= 1   
            b += 1
            # on essaye de regarder si signe(f(a)) n'est pas égal à signe(f(b))
            # try est nécessaire pour le cas où f(a) ou f(b) est nan
            try:
                # on essaye de regarder si f(a) ou f(b) sont 0 (pour éviter les divisions par 0)
                if f(a) == 0:
                    return a
                
                elif f(b) == 0:
                    return b
                
                # si signe(f(a)) n'est pas signe(f(b)), on passe à l'étape suivante
                elif abs(f(a))/f(a) != abs(f(b))/f(b):
                    break
            
            # si f(a) ou f(b) est nan, on continue de chercher
            except:
                pass

            # incrémentation du nombre d'essais par 1
            anti_bug += 1
    
        # si la fonction ne change pas de signe, il n'y a pas de zéro
        if anti_bug == 10000:
            return nan 

    # Etape 3: méthode de dichotomie, si abs(f(x)) < 10^(-précision) alors on arrête la boucle et on retourne x
    anti_bug = 0    # variable anti_bug évite les cas où la fonction n'est pas continue 
    while anti_bug < 100:
        # try est nécessaire pour éviter le cas où f((a+b)/2) est nan
        try:
            # tant que f((a+b)/2) n'est un zéro, on continue de chercher
            while abs(f((a+b)/2))>h:
                # si f((a+b)/2) est inférieur à zéro, ...
                if f((a+b)/2)<0:
                    # ... et f(a) inférieur à zéro, alors a doit se rapprocher plus de b
                    if f(a) < 0:
                        a = (a+b)/2
                    # ... et f(a) supérieur à zéro, alors b doit se rapprocher plus de a
                    else:
                        b = (a+b)/2
                # si f((a+b)/2) est supérieur à zéro, ...
                else:
                    # ... et f(a) supérieur à zéro, alors a doit se rapprocher plus de b
                    if f(a) > 0:
                        a = (a+b)/2
                    # ... et f(a) inférieur à zéro, alors b doit se rapprocher plus de a
                    else:
                        b = (a+b)/2
            # si on arrive ici, ça veut dire que f((a+b)/2) est un zéro, donc on le retourne
            return (a+b)/2

        # si f((a+b)/2) est un nan
        except:
            # on incrémente a un tout petit peu, pour éviter une erreur à la prochaine tentative
            a += h
            # incrémentation du nombre d'essais loupés par 1
            anti_bug += 1

    # si l'on arrive ici, alors la fonction n'est pas continue => pas de zéros
    return nan

# fonction qui détermine les zeros de f avec la méthode Newton-Raphson (à revoir)
def detListeZero(methode):
    # liste qui stocke les zeros
    liste_zero = []
    # boucle sur x pour déterminer beaucoup de zéros avec les deux techniques
    for x in range(borneInf, borneSup+1):
        # si la méthode est Newton-Raphson
        if methode == "Newton-Raphson":
            # détermination d'un zero à partir de x
            a = newtonRaphson(f, x)
        # si la méthode est la dichotomie
        elif methode == "Dichotomie":
            # détermination d'un zero entre x et x+1
            a = dichotomie(f, x, x+1)
        else:
            return []
        # si a n'est pas une erreur, on peut continuer
        if a != "Erreur":
            # si il n'y a pas encore de 0, on ajoute le zéro à la liste
            if len(liste_zero) == 0:
                liste_zero.append(a)
            # si il y a déjà un zéro, il faut s'assurer que deux zéros ne sont pas proches
            else:
                for zero in liste_zero:
                    # si un zéro et le nouveau zéro sont très proches, on prend le résultat le plus petit et on l'ajoute dans la liste des zéros
                    print(abs(zero-a) < 0.0001, a)

                    if abs(zero-a) < 0.0001:
                        # si le nouveau zéro a une valeur dans f plus petite, on enlève le zéro proche et on ajoute le nouveau zéro
                        if f(zero) > f(a):
                            liste_zero.remove(zero)
                            liste_zero.append(a)
                            break   # coupe la boucle puisqu'on a ajouté le zéro voulu
                        # si l'ancien zéro a une valeur dans f plus petite, on coupe la boucle, pusique le nouveau zéro est "moins bon" que l'ancien
                        else:
                            break
                # si le nouveau zéro est proche d'aucun des zéros, on l'ajoute à la liste
                liste_zero.append(a)

    # retourne à la toute fin la liste des zéros 
    return liste_zero




###########
#INTERFACE#
###########

# fonction pour activer le zoomage sur le graphe
def activer_zoom(ax):
    # fonction qui zoome une fois sur le graphe
    def zoom(event):
        # on prends les limites actuelles de l'axe x et y
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()

        # on définit la longueur des intervalles dans lesquelles sont définies la fonction
        xrange = (cur_xlim[1] - cur_xlim[0])/2
        yrange = (cur_ylim[1] - cur_ylim[0])/2

        # on prends la location du curseur, là on l'on veut zoomer
        zoomToX = event.xdata  
        zoomToY = event.ydata  

        if event.button == "up":
            # zoom in
            scale_factor = 1/1.05
        elif event.button == "down":
            # zoom out
            scale_factor = 1.05
        
        # définiton des nouvelles limites
        x_inf = zoomToX - xrange*scale_factor
        x_sup = zoomToX + xrange*scale_factor
        y_inf = zoomToY - yrange*scale_factor
        y_sup = zoomToY + yrange*scale_factor

        # mise des nouvelles limites dans le grapheur
        ax.set_xlim([x_inf, x_sup])
        ax.set_ylim([y_inf, y_sup])

        # redessine la fonction avec les nouvelles limites
        plt.draw()

    # on prend la figure dans laquelle on veut zoomer (la fenêtre du graphe)
    fig = ax.get_figure() 
    
    # on connecte l'évenement "scroll" avec la fonction de zoomage
    fig.canvas.mpl_connect('scroll_event', zoom)

    # retourne la fonction
    return zoom

# fonciton exectutée lorsque l'utilisateur clique sur le bouton "calculer", pour déterminer les zeros de f
def solve():
    # prend la valeur dans la zone pour choisir sa méthode
    methode = methodeStr.get()
    print(methode)
    # calcule la liste des zeros selon la méthode choisie
    liste_zero = detListeZero(methode)

    print(liste_zero)
    strZeros = ""
    for y in range(len(liste_zero)): # prend 1 à 1 chaque zéro trouvé 
        # affiche le zéro sur le graphique
        plt.plot(liste_zero[y], 0, 'o')
        # orthographe française ; le 1er zéro doit être marqué comme "1er", pas "1eme"
        if y == 0:
            strZeros += f"\n Le 1er zéro de la fonction est en x = {liste_zero[y]}."
        else:
            strZeros += f"\n Le {y+1}ème zéro de la fonction est en x = {liste_zero[y]}."

    # zone de texte dans la zone de gauche, qui montre les zéros
    zeroLabel = Label(leftFrame, text=strZeros)
    # mise de la zone de texte sur la fenêtre
    zeroLabel.pack()

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

methodeStr = StringVar()
methodeStr.set("méthode de résolution")
methodeMenu = OptionMenu(leftFrame, methodeStr, "Newton-Raphson", "Dichotomie")
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
x = np.linspace(-1000, 1000, d)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position(('data', 0)) # la commande 'data' permet de positionner correctement les axes par rapport à la fonction
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# limitation du la vue du graphe au début
plt.xlim(-10, 10)   # pour l'axe des x  
plt.ylim(-10, 10)   # pour l'axe des y

# on appelle la fonction de zoom pour l'activer
g = activer_zoom(ax)

# plot les fonctions
plt.plot(x, x, 'y', label="f(x)")
plt.legend(loc='upper left')


# creation du canvas pour le graphe
canvas = FigureCanvasTkAgg(fig, master = graphFrame)  
canvas.draw()

# affichage du graphe
canvas.get_tk_widget().pack(fill=BOTH, expand=1)


root.mainloop()