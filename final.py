### Import des librairies utilisée par le programme
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.axis import Axis
from numpy import e, sin, cos, tan, sqrt
from cmath import nan



####################
#VARIABLES GLOBALES#
####################

# variable contenant la fonction en string
function = ""
# variable contenant la position des zéros
strZeros = ""
# borne entre lesquelles la fonction sera affichée
borneInf = -10
borneSup = 10



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
    # essaye d'évaluer la fonction en x
    try:
        # on reformate la fonction avec des opérations connues par python
        functionFormated = function.replace("^", "**").replace("√", "root2").replace("∛", "cbrt").replace("∜", "root4").replace("sin", "np.sin").replace("cos", "np.cos").replace("tan", "np.tan").replace("log", "np.log10").replace("ln", "np.log").replace("exp", "np.exp").replace("abs", "abs").replace("π", "np.pi")
        return eval(functionFormated)
    # si elle y arrive pas, retourne un nan ("Not A Number")
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
        while abs(f(a)) > h/100 and anti_bug < 1000:
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
        if anti_bug < 1000 and abs(f(a)) < h/100:
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
        return "Erreur"


    # Etape 2: on vérifie que le signe de f(a) et f(b) n'est pas le même
    if abs(f(a))/f(a) == abs(f(b))/f(b):
        # Etape 2.1: on ajoute -1 à a ou +1 à b pour trouver des signes de f(a) et f(b) différents 
        anti_bug = 0    # variable anti_bug évite les cas où la fonction ne change pas de signe
        while anti_bug < 1000:
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
        if anti_bug == 1000:
            return "Erreur"

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
    return "Erreur"

# fonction qui détermine les zeros de f avec la méthode Newton-Raphson (à revoir)
def detListeZero(methode):
    # liste qui stocke les zeros
    liste_zero = []
    # boucle sur x pour déterminer beaucoup de zéros avec les deux techniques
    for x in range(40, 41):
        # on divise x par 4 pour avoir beaucoup de possiblités de zéros
        x = x/4
        # si la méthode est Newton-Raphson
        if methode == "Newton-Raphson":
            # détermination d'un zero à partir de x
            a = newtonRaphson(f, x)
        # si la méthode est la dichotomie
        elif methode == "Dichotomie":
            # détermination d'un zero entre x et x+1
            a = dichotomie(f, x, x+(1/4))
        else:
            return []
        # si a n'est pas une erreur, on peut continuer
        if a != "Erreur":
            # arrondi du zéro trouvé à 10^(-8)
            a = round(a, 8)
            # il faut s'assurer que le zéro trouvé n'est pas déjà répertorié
            if not a in liste_zero:
                liste_zero.append(a)

    # retourne à la toute fin la liste des zéros 
    return liste_zero


##########################
#FONCTIONS DE L'INTERFACE#
##########################

# fonction pour activer le zoomage sur le graphe
def activer_zoom(ax):
    global borneInf, borneSup
    # fonction qui zoome une fois sur le graphe
    def zoom(event):
        global borneInf, borneSup
        if event.button == "down":
            # zoom in
            scale_factor = 1/1.05
        elif event.button == "up":
            # zoom out
            scale_factor = 1.05
        
        # définiton des nouvelles limites
        borneInf *= scale_factor
        borneSup *= scale_factor
    

        # mise des nouvelles limites dans le grapheur
        ax.set_xlim([borneInf, borneSup])
        ax.set_ylim([borneInf, borneSup])

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
    # global permet d'avoir partout la même référence à la variable "strZeros" et "zeroLabel" 
    global strZeros, zeroLabel
    # prend la valeur dans la zone pour choisir sa méthode
    methode = methodeStr.get()
    # calcule la liste des zeros selon la méthode choisie
    liste_zero = detListeZero(methode)
    strZeros = ""
    for y in range(len(liste_zero)): # prend 1 à 1 chaque zéro trouvé 
        # affiche le zéro sur le graphique
        plt.plot(liste_zero[y], 0, 'o')
        # orthographe française ; le 1er zéro doit être marqué comme "1er", pas "1eme"
        if y == 0:
            strZeros += f"\n Le 1er zéro de la fonction est en x = {liste_zero[y]}"
        else:
            strZeros += f"\n Le {y+1}ème zéro de la fonction est en x = {liste_zero[y]}"

    # update du texte dans zone de texte qui montre les zéros
    zeroLabel.config(text=strZeros)

# fonction exectutée lorsque l'utilisateur clique sur un bouton qui modifie la fonction, pour actualiser la fonction dans la variable et l'afficher
def update_function(stringToAdd):
    # global permet d'avoir partout la même référence à la variable "function" 
    global function
    
    # si il y a deux opérations conséqutives, la fonction n'est pas valable
    if stringToAdd in ["+", "-", "*", "/", "^"]:
        return
    # si il y a une opération à la fin de la fonction, la fonction n'est pas valable
    elif function[-1] in  ["+", "-", "*", "/", "^"]:
        return
    
    # si le bouton appuyé est "delete", on enlève le dernier élément
    if stringToAdd == "DEL":
        function = function[:-1]
    # sinon, on ajoute le terme présent sur le bouton choisi
    else:
        function += stringToAdd
    # si le terme est une fonction, on est obligé de mettre les parenthèses
    if stringToAdd in ["sin","cos","tan","log","ln","exp","abs","√","∛", "∜"]:
        function += "("
    
    # actualisation du champ de texte dans lequel il y a la fonction affichée
    functionInput.delete(0,END)
    functionInput.insert(0,function)
    # si la fonction est réussite, on actualise le graphe
    update_graph()

# fonction appelée losque l'utilisateur modifie le champ de texte de la fonciton
def inputChange():
    # global permet d'avoir partout la même référence à la variable "function" 
    global function
    # on récupère la fonction entrée dans le champ de texte
    function = functionInput.get()
    # on actualise le graphe
    update_graph()

# fonction qui actualise l'affichage du graphique
def update_graph():
    # redéfinition de l'ensemble des x qui est plot
    x = np.linspace(borneInf, borneSup, d)
    # clear du plot
    plt.cla()
    # redessinage du graphe
    plt.plot(x, f(x), 'y', label="f(x)")
    # choix de la location du plot
    plt.legend(loc='upper left')
    # la commande 'data' permet de positionner correctement les axes par rapport à la fonction, c.à.d en (0,0)
    ax.spines['left'].set_position(('data', 0)) 
    ax.spines['bottom'].set_position(('data', 0))
    # limitation du la vue du graphe au début
    plt.xlim(-10, 10)   # pour l'axe des x  
    plt.ylim(-10, 10)   # pour l'axe des y
    # dessinage du plot dans la fenêtre tkinter
    canvas.draw()



###########
#INTERFACE#
###########

root = Tk() # création de la fenêtre
root.title("Equation Solver") # titre de la fenêtre
root.state('zoomed') # fenêtre maximisée (pas en plein écran)

root.columnconfigure(1, weight=1) # permet à la colone contenant le grphique de prendre toute la largeur de la fenêtre
root.rowconfigure(0, weight=1) # permet à la ligne du haut de prendre toute la hauteur de la fenêtre

leftFrame = Frame(root) # création d'une zone l'où l'on pourra mettre d'autres zones (comme du texte p.ex)
leftFrame.grid(row=0, column=0) # mise de la zone tout en haut à gauche ((0,0) est tout en haut à gauche du tkinter)

# création d'une zone de texte l'où écrit : "Méthode de résolution"
methodeStr = StringVar() 
methodeStr.set("Méthode de résolution")
methodeMenu = OptionMenu(leftFrame, methodeStr, "Newton-Raphson", "Dichotomie") # création d'une zone choix multiple (menu) l'où écrit il y a : "Newton-Raphson" et "Dichotomie"
methodeMenu.pack(side=TOP, fill=X)  # mise du menu dans la zone "leftFrame", le plus en haut possible 

functionInputFrame = Frame(leftFrame)    # création d'une zone l'où mettera l'input de la fonction
functionInputFrame.pack(fill=X, side=TOP)   # mise de la zone dans la zone "leftFrame", le plus en haut possible 

# création d'une zone de texte l'où écrit : "f(x) = " à gauche 
functionLabel = Label(functionInputFrame, text="f(x) = ")   
functionLabel.pack(side=LEFT)
# création d'une zone où l'on peut écrire la fonction, à droite 
functionInput = Entry(functionInputFrame)
functionInput.pack(side=RIGHT, fill=X)
# Connection entre l'événement "Relachement de touche" et la fonction inputChange()
functionInput.bind("<KeyRelease>", lambda event: inputChange())

calculer = Button(leftFrame, text="Calculer", command=solve)    # création d'un bouton qui va appeler la fonction solve()
calculer.pack(side=TOP, fill=X)  # mise du bouton dans la zone "leftFrame", le plus en haut possible 

zeroLabel = Label(leftFrame, text=strZeros) # zone de texte dans la zone de gauche, qui montre les zéros
zeroLabel.pack()    # mise de la zone de texte sur la zone de gauche

graphFrame = Frame(root)    # création d'une zone l'où l'on mettera le graphique
graphFrame.grid(row=0, column=1, sticky=N+S+E+W)    # mise de la zone tout en haut à droite


bottomFrame = Frame(root)    # création d'une zone l'où l'on mettera les boutons comme sur la calculette
bottomFrame.grid(row=1, column=0, columnspan=2) # mise de la zone tout en bas au milieu (avec columnspan)



# boutons pour les chiffres de 0 à 9

# affichage des boutons de 1 à 9, qui appelent toutes la fonction update_fonction(), avec paramètre leur chiffre respectif
for i in range(3):
    for j in range(3):
        # on boucle doublement pour avoir 3 boutons par ligne
        Button(bottomFrame, text=str(i*3+j+1), command=lambda x=str(i*3+j+1): update_function(x), font=("Helvetica",20)).grid(row=i, column=j)
# affichage des boutons de 0
Button(bottomFrame, text="0", command=lambda: update_function("0"), font=("Helvetica",20)).grid(row=3, column=0, columnspan=2, sticky='ew')
# bouton pour la virgule
Button(bottomFrame, text=".", command=lambda: update_function("."), font=("Helvetica",20)).grid(row=3, column=2, sticky='ew')

# juste pour avoir une marge entre les chiffre et les opérations
Label(bottomFrame, text=" ").grid(row=0, column=3, sticky='ew', padx=5)

# création des boutons pour les opérations
for i in range(4):
    for j in range(4):
        # on boucle doublement pour avoir 4 boutons par ligne
        Button(bottomFrame, text=operations[i+4*j], command=lambda x=operations[i+4*j]: update_function(x), font=("Helvetica",20)).grid(row=i, column=j + 4, sticky='ew')

# creation du bouton pour delete
Button(bottomFrame, text="←", command=lambda: update_function("DEL"), font=("Helvetica",20)).grid(row=3, column=8, sticky='ew')
# creation des boutons pour x, (, )
Button(bottomFrame, text="x", command=lambda: update_function("x"), font=("Helvetica",20)).grid(row=0, column=8, sticky='ew')
Button(bottomFrame, text="(", command=lambda: update_function("("), font=("Helvetica",20)).grid(row=1, column=8, sticky='ew')
Button(bottomFrame, text=")", command=lambda: update_function(")"), font=("Helvetica",20)).grid(row=2, column=8, sticky='ew')

# on définit des fonctions de racine pour que python les comprenne
def root2(x):
    return x**(1/2)
def cbrt(x):
    return x**(1/3)
def root4(x):
    return x**(1/4)


plt.style.use("dark_background") # fond noir pour le graphe
plt.ion() # on active l'affichage en temps réel
# crée n éléments (inversement proportionnel à d) qu'on va plot dans la fonction entre les bornes choisies
x = np.linspace(borneInf, borneSup, d)

# création de la figure du graphe
fig = plt.figure()
# création de 2 axes dans la figure
ax = fig.add_subplot(1, 1, 1)
# la commande 'data' permet de positionner correctement les axes par rapport à la fonction (ici en (0,0))
ax.spines['left'].set_position(('data', 0)) 
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# on appelle la fonction qui active le zoomage
g = activer_zoom(ax)

# plot les fonctions
plt.plot(x, x, 'y', label="f(x)")
plt.legend(loc='upper left')

# limitation du la vue du graphe au début
plt.xlim(-10, 10)   # pour l'axe des x  
plt.ylim(-10, 10)   # pour l'axe des y

# creation du canvas pour le graphe
canvas = FigureCanvasTkAgg(fig, master = graphFrame)  
canvas.draw()

# affichage du graphe
canvas.get_tk_widget().pack(fill=BOTH, expand=1)


root.mainloop()