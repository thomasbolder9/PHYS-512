import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline

def fun(x):
    return 1/np.log(x)

x = np.linspace(2, 3, 21)
dx = x[1]-x[0]
print(x)
y = fun(x)

spln = CubicSpline(x,y)
xx = np.linspace(x[1]-x[0])
yy = spln(xx)
