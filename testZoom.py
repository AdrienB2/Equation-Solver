from numpy import arange, sin, pi, float, size

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure


fig = Figure((5, 4), 75)
scroll_range = 400

sizer = BoxSizer(VERTICAL)
sizer.Add(canvas, -1, EXPAND)

init_data()
init_plot()

canvas.Bind(EVT_SCROLLWIN, OnScrollEvt)

def init_data():
    global t, x, i_min, i_max, i_window, i_start, i_end
    # Generate some data to plot:
    dt = 0.01
    t = arange(0,5,dt)
    x = sin(2*pi*t)

    # Extents of data sequence:
    i_min = 0
    i_max = len(t)

    # Size of plot window:
    i_window = 100

    # Indices of data interval to be plotted:
    i_start = 0
    i_end = i_start + i_window

def init_plot():
    global x, i_min, i_max, i_window, i_start, i_end, plot_data
    axes = fig.add_subplot(111)
    plot_data = \
              axes.plot(t[i_start:i_end],
                             x[i_start:i_end])[0]

def draw_plot():

    # Update data in plot:
    plot_data.set_xdata(t[i_start:i_end])
    plot_data.set_ydata(x[i_start:i_end])

    # Adjust plot limits:
    axes.set_xlim((min(t[i_start:i_end]),
                       max(t[i_start:i_end])))
    axes.set_ylim((min(x[i_start:i_end]),
                        max(x[i_start:i_end])))

    # Redraw:
    canvas.draw()

    
def OnScrollEvt(event):
    # Update the indices of the plot:
        i_start = i_min + event.GetPosition()
        i_end = i_min + i_window + event.GetPosition()
        draw_plot()