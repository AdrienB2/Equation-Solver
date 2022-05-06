### Import des librairies utiles : math, nummpy et matplotlib, tkinter
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math as math
from matplotlib.axis import Axis
from numpy import e, sin, cos, tan, sqrt
from cmath import nan

# variable contenant la fonction en string
function = ""

# le h va déterminer l'ordre de précision de la dérivée
# h = 0.000000000001 est la plus petite valeur que Python supporte
h = 0.000000000001


### Fonctions

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


# la dérivée
def derivative(f, x):
    # utilisation de la définition de la dérivée avec la limite ; f'(a) = lim h->0 ((f(a + h) - f(a))/h)
    f1 = f(x)
    f2 = f(x + h)
    fDerivee = (f2 - f1)/h  
    return fDerivee


# la tangente
def tangente(f, x, a):
    y3 = f(a) + derivative(f, a)*(x - a)
    return y3

