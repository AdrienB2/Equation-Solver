import math as math
import time as time
import tkinter as tk



def f(x): #la fonction qu'on veut voir
    def func(x):
        return math.tan(x)
    if -10000 > func(x) or func(x) > 10000:
        return "Erreur"
    try:
        return float(func(x))
    except OverflowError:
        try:
            return int(func(x))
        except OverflowError:
            return "Erreur"
    except (ValueError, ZeroDivisionError,TypeError):
        return "Erreur"

def derivative(f, x):
    if f(x) != "Erreur" or f(x+0.000000000001)!= "Erreur":
        f1 = f(x)
        f2 = f(x+0.000000000001)
        res = (f2-f1)/ 0.000000000001
        if -10000 > res or res > 10000:
            return "Erreur"
        try:
            return float(res)
        except OverflowError:
            try:
                return int(res)
            except OverflowError:
                return "Erreur"
        except (ValueError, ZeroDivisionError,TypeError):
            return "Erreur"
    else:
        return "Erreur"



w=1900
h=1100
b_inf=-10        #x min
b_sup=10        #x max
d= 100000 #nombres de x vérifiés
win=tk.Tk()
win.title("Traceur de courbes")
win.geometry()
can=tk.Canvas(win,bg="white",width=w,height=h)
can.pack()

def grapheur(f, deriv, b_inf, b_sup, d):

    liste=[]
    b_inf=b_inf-(b_sup-b_inf)/40
    b_sup=b_sup+(b_sup-b_inf)/40
    t=(b_sup-b_inf)/d #pas de x 
    for c in range(0,d+1):
        x=b_inf+c*t
        if f(x)!="Erreur":
            if -100 < f(x) < 100:
                liste.append(f(x))
        if deriv(f, x) != "Erreur":
            if -10 < deriv(f, x) < 10:
                liste.append(deriv(f, x))

    b=w/(b_sup-b_inf)           #multiplicateur en x
    mn=min(liste)-(max(liste)-min(liste))/20
    mx=max(liste)+(max(liste)-min(liste))/20
    if mx-mn==0:
        mx=mx+abs(0-mx)+1
        mn=mn-abs(0-mn)-1


    def i(t,inf,sup,yes):       #défini les écarts de notations en fonction de la longueur de pixels(t), la borne inférieure(inf) et supérieure(sup)
        g=40                # écart idéal (enfin pour vous) entre les notations [pixels]
        if yes==1:
            if mx!=0 and abs(mx)>=abs(mn):
                if (abs(math.log10(abs(mx)))//1*3)>=g:
                    g=(abs(math.log10(abs(mx)))//1*3)+10
            elif mn!=0 and abs(mn)>abs(mx):
                if (abs(math.log10(abs(mn)))//1*3)>=g:
                    g=(abs(math.log10(abs(mn)))//1*3)+10
        x=g*(sup-inf)/t         # intervalle précis
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