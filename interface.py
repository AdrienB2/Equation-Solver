from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

function=""

def get_function():
    #get the value of the entry
    value=functionInput.get()
    #print the value
    print(value)

#create a function to update the entry
def update_function(stringToAdd):
    global function
    function=functionInput.get()
    if function[-len(stringToAdd):]==stringToAdd:
        return
    if stringToAdd == "DEL":
        function=function[:-1]
    else:
        function+=stringToAdd
    functionInput.delete(0,END)
    functionInput.insert(0,function)

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

functionInput = Entry(functionInputFrame)
functionInput.pack(side=RIGHT, fill=X)

functionLabel = Label(functionInputFrame, text="f(x) = ")
functionLabel.pack(side=LEFT)


calculer = Button(leftFrame, text="Calculer", command=get_function)
calculer.pack(side=TOP, fill=X)

graphFrame = Frame(root)
graphFrame.grid(row=0, column=1, sticky=N+S+E+W)


bottomFrame = Frame(root)
bottomFrame.grid(row=1, column=0, columnspan=2)

#Boutons pour les chiffres de 0 à 9
btn1 = Button(bottomFrame, text="1", command=lambda: update_function("1"), font=("Helvetica",20))
btn1.grid(row=0, column=0)
btn2 = Button(bottomFrame, text="2", command=lambda: update_function("2"), font=("Helvetica",20))
btn2.grid(row=0, column=1)
btn3 = Button(bottomFrame, text="3", command=lambda: update_function("3"), font=("Helvetica",20))
btn3.grid(row=0, column=2)
btn4 = Button(bottomFrame, text="4", command=lambda: update_function("4"), font=("Helvetica",20))
btn4.grid(row=1, column=0)
btn5 = Button(bottomFrame, text="5", command=lambda: update_function("5"), font=("Helvetica",20))
btn5.grid(row=1, column=1)
btn6 = Button(bottomFrame, text="6", command=lambda: update_function("6"), font=("Helvetica",20))
btn6.grid(row=1, column=2)
btn7 = Button(bottomFrame, text="7", command=lambda: update_function("7"), font=("Helvetica",20))
btn7.grid(row=2, column=0)
btn8 = Button(bottomFrame, text="8", command=lambda: update_function("8"), font=("Helvetica",20))
btn8.grid(row=2, column=1)
btn9 = Button(bottomFrame, text="9", command=lambda: update_function("9"), font=("Helvetica",20))
btn9.grid(row=2, column=2)
btn0 = Button(bottomFrame, text="0", command=lambda: update_function("0"), font=("Helvetica",20))
btn0.grid(row=3, column=0, columnspan=2, sticky='ew')
#bouton pour la virgule
btnDot = Button(bottomFrame, text=".", command=lambda: update_function("."), font=("Helvetica",20))
btnDot.grid(row=3, column=2, sticky='ew')

#Boutons pour les opérateurs
btnAdd = Button(bottomFrame, text="+", command=lambda: update_function("+"), font=("Helvetica",20))
btnAdd.grid(row=0, column=3, sticky='ew', padx=(20, 0))
btnSub = Button(bottomFrame, text="-", command=lambda: update_function("-"), font=("Helvetica",20))
btnSub.grid(row=1, column=3, sticky='ew', padx=(20, 0))
btnMul = Button(bottomFrame, text="*", command=lambda: update_function("*"), font=("Helvetica",20))
btnMul.grid(row=2, column=3, sticky='ew', padx=(20, 0))
btnDiv = Button(bottomFrame, text="/", command=lambda: update_function("/"), font=("Helvetica",20))
btnDiv.grid(row=3, column=3, sticky='ew', padx=(20, 0))
#add buttons for the x
btnX = Button(bottomFrame, text="x", command=lambda: update_function("x"), font=("Helvetica",20))
btnX.grid(row=0, column=4, sticky='ew')
#add buttons for the pi
btnPi = Button(bottomFrame, text="π", command=lambda: update_function("π"), font=("Helvetica",20))
btnPi.grid(row=1, column=4, sticky='ew')
#add buttons for the e
btnE = Button(bottomFrame, text="e", command=lambda: update_function("e"), font=("Helvetica",20))
btnE.grid(row=2, column=4, sticky='ew')

#add a delete button
btnDel = Button(bottomFrame, text="←", command=lambda: update_function("DEL"), font=("Helvetica",20))
btnDel.grid(row=3, column=4, sticky='ew')



# borne entre lesquelles la fonction sera affichée
borneInf = -5
borneSup = 5
# nombres de x vérifiés dans le graphe
d = 100000
function = "x"
def f(x):
    #check if the function is valid
    try:
        return eval(function)
    except:
        return 0

plt.style.use("dark_background") # fond noir car c'est plus stylax
plt.ion() # on active l'affichage en temps réel
# crée n éléments (inversement proportionnel à d) qu'on va plot dans la fonction entre les bornes choisies
x = np.linspace(borneInf, borneSup, d)

# the figure that will contain the plot
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

# creating the Tkinter canvas
# containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master = graphFrame)  
canvas.draw()

# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack(fill=BOTH, expand=1)

# placing the toolbar on the Tkinter window
canvas.get_tk_widget().pack()

root.mainloop()