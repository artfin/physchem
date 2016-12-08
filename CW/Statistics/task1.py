import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

dy = np.zeros(y.shape, np.float)
dy[0:-1] = np.diff(y)/ np.diff(x)

trace1 = go.Scatter(
    x = x,
    y = y,
    mode = 'line',
    name = 'sin(x)'
)

trace2 = go.Scatter(
    x = x,
    y = dy,
    mode = 'line',
    name = 'numerical derivative of sin(x)'
)

trace_data = [trace1, trace2]
py.iplot(trace_data)
