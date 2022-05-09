### Graphe

def plot():
    global f, tangente, L, d, borneInf, borneSup, fig, ax
    plt.style.use("dark_background") # fond noir car c'est plus stylax
    # crée n éléments (inversement proportionnel à d) qu'on va plot dans la fonction entre les bornes choisies
    x = np.linspace(borneInf, borneSup, d)

    # création des axes
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', 0)) # la commande 'data' permet de positionner correctement les axes par rapport à la fonction
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot les fonctions
    plt.ion
    plt.plot(x, f(x), 'y', label="f(x)")
    plt.legend(loc='upper left')
    fig.canvas.mpl_connect("scroll_event", zoom)
    # plot des tangentes
    for i in range(len(L)) :
        plt.plot(x, tangente(f, x, L[i]), label="t_"+str(i))

    for zero_j in liste_zero: # affiche chaque zero trouvé 
        plt.plot(zero_j, 0, 'o')

    # affiche la fenêtre des graphes
    plt.show()

scale = 0
plot()   