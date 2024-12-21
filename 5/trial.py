
import numpy as np

def gd(x_initial, step_size, max_iterations):
    xNew = x_initial.copy()
    for i in range(max_iterations):
        gradient = 2*(xNew)**3 - 16*(xNew) + (5/2)
        xNew -= step_size * gradient
    
    print("x after running specified number of iterations:", xNew)
    print("f(x) at point:", 0.5 * np.sum(xNew**4 - 16*xNew**2 + 5*xNew))
