### Import des librairies utiles : math, nummpy et matplotlib, tkinter
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math as math
from matplotlib.axis import Axis
from numpy import e, sin, cos, tan, sqrt
from cmath import nan



### Fonctions

# la fonction f 
def f(x):
    # Définition de la fonction ici
    try:
        return eval("1/x")
    except:
        return nan      #not a number



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


# la tangente
def tangente(f, x, a):
    y3 = f(a) + derivative(f, a)*(x - a)
    return y3

