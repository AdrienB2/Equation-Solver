### import des librairies utiles : tkinter et math
import math as math
import tkinter as tk

def rec_eq(equat_str, x):
    b = equat_str.replace("x", f"({str(x)})")
    return eval(b)
### fonction et dérivée

# la fonction f qu'on veut avoir, dépend de la valeur x entrée
def f(x):
    # nouvelle fonction pour faciliter la correction de bugs
    def func(x):
        # Définition de la fonction ici
        return rec_eq("x**2", x)
    # essaie de retourner la valeur de f(x)
    try:
        return float(func(x))

    # types d'erreurs informatiques possibles (division par 0 par exemple):
    except:
        return "Erreur"


# la dérivée, qui va dépendre de la fonction f et de la valeur entrée x
def derivative(f, x):
    # regarde si f en x fait du sens (-> dérivée possible)
    if f(x) != "Erreur" or f(x+0.000000000001)!= "Erreur":
        # utilisation de la définition d'une dérivée ; lim h->0 {(f(a+h)-f(a)/h)}
        f1 = f(x)           #f(a)
        f2 = f(x+0.000000000001)            #f(a+h) h = 0.000000000001, plus petite valeur que Python supporte
        f_deriv = (f2-f1)/ 0.000000000001       #dérivée en x 

        # essaie de retourner la valeur de f'(x)
        try:
            return float(f_deriv)

        # comme pour la fonction, erreurs informatiques possibles
        except:
            return "Erreur"

    # regarde si f en x pas de sens (-> dérivée infinie -> impossible)
    else:
        return "Erreur"


# test pour avoir les dimensions de l'écran en fullscreen
fen_test = tk.Tk()
h = fen_test.winfo_screenheight()  # variable qui va récupérer la hauteur maxiamale de l'écran 
w = fen_test.winfo_screenwidth()   # variable qui va récupérer la largeur maximale de l'écran 
fen_test.destroy()

b_inf = -10        # borne minimale de x dans le graphe
b_sup = 10        # borne maximale de x dans le graphe
d = 100000      # nombres de x vérifiés dans le graphe

# fenêtre qui montre le graphe
win = tk.Tk()
win.title("Traceur de courbes")
win.geometry()

# canvas, surface où va dessiner le graphe
can = tk.Canvas(win, bg="white", width=w, height=h)
can.pack()


# fonction qui va faire le graphique 
def grapheur(f, deriv, b_inf, b_sup, d):
    liste = []          # liste des résultats de f(x) pour déterminer les bornes de f(x)
    t = (b_sup-b_inf)/d         # pas de x de controle de f(x)

    b_inf = b_inf - (b_sup-b_inf)/40      # adaptations estétiques
    b_sup = b_sup + (b_sup-b_inf)/40

    # boucle pour déterminer les bornes de f(x)
    for c in range(0,d+1):
        x = b_inf + c*t     # détermination de x
        # controle si f(x) est possible
        if f(x)!= "Erreur":
            liste.append(f(x))


    b = w/(b_sup-b_inf)
    mn = min(liste) - (max(liste)-min(liste))/20        # valeur min de f   (-(max(liste)-min(liste))/20 est purement estétique)
    mx = max(liste) + (max(liste)-min(liste))/20        # valeur max de f   (+(max(liste)-min(liste))/20 est purement estétique)
    # Cas où la fonction est constante
    if mx - mn == 0:
        # redéfinition pour redimensionner le cas d'une fonction constante
        mx = mx + abs(mx) + 1
        mn = mn - abs(mn) - 1


    # défini les écarts de notations en fonction de la longueur de pixels(t), la borne inférieure(inf) et supérieure(sup)
    def i(t, inf, sup, yes):    
        ec_pix = 50                # écart idéal (enfin pour vous) entre les notations [pixels]
        if yes==1:
            if mx!=0 and abs(mx)>=abs(mn):
                if (abs(math.log10(abs(mx)))//1*3)>=ec_pix:
                    ec_pix=(abs(math.log10(abs(mx)))//1*3)+10
            elif mn!=0 and abs(mn)>abs(mx):
                if (abs(math.log10(abs(mn)))//1*3)>=ec_pix:
                    ec_pix=(abs(math.log10(abs(mn)))//1*3)+10
        x=ec_pix*(sup-inf)/t         # intervalle précis
        #tous les écarts entre les intevalles arrondis et les intervalles précis
        a=10**(math.log10(abs(x))//1)-abs(x)
        b=2*10**(math.log10(abs(x))//1)-abs(x)
        c=5*10**(math.log10(abs(x))//1)-abs(x)
        d=10*10**(math.log10(abs(x))//1)-abs(x)
        if a<0 :
            if b<0:
                if c<0:
                    if d>=0:
                        x=10*10**(math.log10(abs(x))//1)
                        return x
                elif c>=0:
                    x=5*10**(math.log10(abs(x))//1)
                    return x
            elif b>=0:
                x=2*10**(math.log10(abs(x))//1)
                return x
        elif a>=0:
            x=10**(math.log10(abs(x))//1)
            return x
    i_x=i(w,b_inf,b_sup,1)/2
    i_y=i(h,mn,mx,0)/2
    a=h/(mx-mn) #multiplicateur en y


    #INFO#
    for c in range(int(b_inf//i_x)-1,int(b_sup//i_x)+2):    #créateur de lignes verticales
        c*=i_x
        can.create_line((c-b_inf)*b,0,(c-b_inf)*b,h,fill="grey75")
        if c%(2*i_x)==0: #créateur des nombres références       "S'il n'y a pas de texte au dessus d'une notation c'est un bug de python."
            can.create_line((c-b_inf)*b,a*mx-5,(c-b_inf)*b,a*mx+5,fill="black",width=1)
            if c%1==0:
                c=int(c)
            can.create_text((c-b_inf)*b,a*mx+15,text=c)
    for c in range(int(mn//i_y)-1,int(mx//i_y)+2): #créateur de lignes horizontales
        c*=i_y
        can.create_line(0,a*(mx-c),w,a*(mx-c),fill="grey75")
        if c%(2*i_y)==0:  #créateur des nombres références
            can.create_line(-b_inf*b-5,a*(mx-c),-b_inf*b+5,a*(mx-c),fill="black",width=1)
            if c%1==0:
                c=int(c)
            if c==0:    #afin d'empêcher une erreur avec le log10 du dessous
                can.create_text(-b_inf*b+15,a*mx,text=c)
            else:       #afin de centrer le nombre sur la droite
                can.create_text(-b_inf*b+15+(abs(math.log10(abs(c)))//1)*3,a*(mx-c),text=c)
    can.create_line(-b_inf*b,0,-b_inf*b,h,width=1)
    can.create_line(0,a*mx,w,a*mx,width=1)



    for c in range(0,d): #créateur du graphe
        x=b_inf+c*t
        if f(x)!="Erreur" and f(x+t)!="Erreur":
            can.create_line((x-b_inf)*b,a*(mx-f(x)),(x-b_inf+t)*b,a*(mx-f(x+t)),fill="blue",width=0.1)
        if deriv(f, x) != "Erreur" and deriv(f, x+t) != "Erreur":
            can.create_line((x-b_inf)*b,a*(mx-deriv(f, x)),(x-b_inf+t)*b,a*(mx-deriv(f, x+t)),fill="red",width=0.1)
    win.mainloop()

grapheur(f, derivative, b_inf, b_sup, d)