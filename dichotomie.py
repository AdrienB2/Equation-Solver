# méthode de dichotomie, la fonction retourne un zero de la fonction
def dichotomie(f, a, b, prec, mode):
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
        # Si le mode choisi fait rien de spécial
        if mode == 0: 
            return "Valeurs impossibles"

        # Etape 2.1: on ajoute -1 à a ou +1 à b pour trouver des signes de f(a) et f(b) différents 
        else:
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