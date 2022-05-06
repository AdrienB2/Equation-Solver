from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#liste des operations/fonctions/constantes
operations=["+","-","*","/","^", "√","∛", "∜","sin","cos","tan", "π", "log","ln","exp", "abs"]

function = ""

def solve():
    value = functionInput.get()

def update_function(stringToAdd):
    global function
    function = functionInput.get()
    
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

def inputChange():
    global function
    function = functionInput.get()
    update_graph()

def update_graph():
    x = np.linspace(borneInf, borneSup, d)
    plt.cla()
    plt.plot(x, f(x), 'y', label="f(x)")
    plt.legend(loc='upper left')
    canvas.draw()

root = Tk()
root.title("Equation Solver")
root.state('zoomed')

root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

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
#detect when the user edit the function
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

# borne entre lesquelles la fonction sera affichée
borneInf = -5
borneSup = 5
# nombres de x vérifiés dans le graphe
d = 100000
function = "x"
def sqrt(x):
    return x**(1/2)
def cbrt(x):
    return x**(1/3)
def root4(x):
    return x**(1/4)

def f(x):
    try:
        functionFormated = function.replace("^", "**").replace("√", "sqrt").replace("∛", "cbrt").replace("∜", "root4").replace("sin", "np.sin").replace("cos", "np.cos").replace("tan", "np.tan").replace("log", "np.log10").replace("ln", "np.log").replace("exp", "np.exp").replace("abs", "abs")
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
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot les fonctions
plt.plot(x, f(x), 'y', label="f(x)")
plt.legend(loc='upper left')

# creation du canvas pour le graphe
canvas = FigureCanvasTkAgg(fig, master = graphFrame)  
canvas.draw()

# affichage du graphe
canvas.get_tk_widget().pack(fill=BOTH, expand=1)



root.mainloop()