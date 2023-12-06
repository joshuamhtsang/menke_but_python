import numpy as np
import matplotlib.pyplot as plt
"""
Compute the median of a probability distribution, p(d).  Where:
 - d is an array of equally-spaced coordinates in d-space
 - p is an array containing the values of p(d) at the corresponding
   coordinates in d
"""

def gaussian_function(x):
    return np.exp(-x*x)

# Can this be done with recursion and memoization?
def cum_sum(p_in):
    return 0

def compute_median(d_in, p_in):
    return 0

if __name__ == '__main__':
    print("Compute median of a probability distribution, p(d)")

    N = 100
    d = np.linspace(0, 10, N)
    p = gaussian_function(d)

    print(d)
    print(p)

    plt.plot(d, p, '-o')
    plt.show()


    