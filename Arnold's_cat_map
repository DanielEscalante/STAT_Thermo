import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import symbols, solve

X = .3
P = .5

f = np.array([])
g = np.array([])

def generate_value(X,P,M):
    x = (3*X+1*P)%M
    p = (2*X+1*P)%M
    return x, p

for i in range(10000):
    f = np.append(f,X)
    g = np.append(g,P)
    X, P = generate_value(X,P,1)

def plot_cat():
    fig = plt.figure()    
    plt.plot(f, g, 'r.')
    plt.show()
    fig.savefig("cat.jpg")
plot_cat()
