import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import symbols, solve
 
x = np.arange(2, 22, 1)
 
def generate_values(input_range):
    f = []
    g = []
   
    for num in input_range:
        log_factorial = np.log(math.factorial(num))
        f_expression = (log_factorial - (num * np.log(num)))/log_factorial
        f.append(f_expression)
        g.append(f_expression + (num/log_factorial))
        
    return f, g
 
f, g = generate_values(x)
 
def plot_rel_errors():
  plt.plot(x, f)
  plt.plot(x, g)
  plt.show()
  
def solve_g():
    for x, numb in enumerate(g):
        if numb <= .01:
            print(x+2)
            break
solve_g()
plot_rel_errors()
