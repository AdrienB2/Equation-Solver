import matplotlib.pyplot as plt
import numpy as np

d = 100000

def f(x):
    return x**2

def zoom_factory(ax):
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0])*0.5
        cur_yrange = (cur_ylim[1] - cur_ylim[0])*0.5
        xdata = event.xdata / 2 # get event x location
        ydata = event.ydata  / 2 # get event y location
        if event.button == "up" or event.button == "":
            # deal with zoom in
            scale_factor = 1/1.05
        elif event.button == "down":
            # deal with zoom out
            scale_factor = 1.05
        # set new limits
        x_inf = xdata - cur_xrange*scale_factor
        x_sup = xdata + cur_xrange*scale_factor
        ax.set_xlim([x_inf, x_sup])
        ax.set_ylim([ydata - cur_yrange*scale_factor, ydata + cur_yrange*scale_factor])

        #x = np.linspace(x_inf, x_sup, d)
        #plt.plot(x, f(x), 'y', label="f(x)")
        plt.draw()

    fig = ax.get_figure() # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event', zoom_fun)

    #return the function
    return zoom_fun

fig = plt.figure()
x = np.linspace(-1000, 1000, d)
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position(('data', 0)) # la commande 'data' permet de positionner correctement les axes par rapport à la fonction
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# plot les fonctions
plt.ion
plt.plot(x, f(x), 'y', label="f(x)")
plt.legend(loc='upper left')

g = zoom_factory(ax)
# affiche la fenêtre des graphes
plt.show()
