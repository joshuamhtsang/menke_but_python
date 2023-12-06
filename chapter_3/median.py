import numpy as np
import matplotlib.pyplot as plt
"""
Compute the median of a probability distribution, p(d).  Where:
 - d is an array of equally-spaced coordinates in d-space
 - p is an array containing the values of p(d) at the corresponding
   coordinates in d
"""

def normal_distribution(x, mean, sigma):
    return 1.0/((np.sqrt(2.0*np.pi)*sigma))*np.exp(-np.power(x-mean,2)/(2*sigma*sigma))

# Can cumulative sum be done with recursion and memoization?  It's so close to the Fibonnaci sequence thing.
def cum_sum_of_nth_element(p_in, n):
    if n == 0:
        return p_in[n]
    else:
        return p_in[n-1] + p_in[n]

def cum_sum(p_in):
    for i in range(0, len(p_in)):
        p_in[i] = cum_sum_of_nth_element(p_in, i)
    return p_in

def compute_median(d_in, p_in):
    return 0

if __name__ == '__main__':
    print("Compute median of a probability distribution, p(d)")

    N = 100
    d_min = 0.0
    d_max = 10.0
    delta_d = (d_max - d_min) / N
    d = np.linspace(d_min, d_max, N)
    
    mean = 5.0
    sigma = 2.0
    p = normal_distribution(d, mean, sigma)

    print(d)
    print(p)

    plt.plot(d, p, '-o')
    plt.show()

    v1 = np.array([1,2,2,3,3])
    print(cum_sum(v1))