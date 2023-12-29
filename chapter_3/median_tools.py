import numpy as np
import matplotlib.pyplot as plt
import normal_distribution
"""
Compute the median of a probability distribution, p(d).  Where:
 - d is an array of equally-spaced coordinates in d-space
 - p is an array containing the values of p(d) at the corresponding
   coordinates in d
"""

# Can cumulative sum be done with recursion and memoization?  It's so close to the Fibonnaci sequence thing.
def cum_sum_of_nth_element(p, n):
    if n == 0:
        return p[n]
    else:
        return p[n-1] + p[n]

def cum_sum(p):
    for i in range(0, len(p)):
        p[i] = cum_sum_of_nth_element(p, i)
    return p

def compute_median(p, d):
    # Ensure p and d arrays are the same length, deduce array lengths
    if len(p) == len(d):
        N = len(p)
    else:
        raise  Exception("The input arrays p and d should have the same length.")

    # Deduce delta_d
    try:
        delta_d = d[1] - d[0]
    except IndexError:
        print("Unable to deduce delta_d due to index out of bounds.")

    # Integrate area under the pdf p
    p_slice_areas = p*delta_d
    print(p_slice_areas)

    p_cum_area = cum_sum(p_slice_areas)
    print(p_cum_area)

    plt.plot(d,p_cum_area, '-o')
    plt.title('Cumulative sum of slice areas')
    plt.show()

    # The median is the value of d where 50% of the 
    # probability lies above it and 50% below it
    for i in range(0, N):
        if p_cum_area[i] > 0.5:
            d_median = i*delta_d
            break
    
    return d_median


if __name__ == '__main__':
    print("Compute median of a probability distribution, p(d)")

    N = 100
    d_min = 0.0
    d_max = 10.0
    delta_d = (d_max - d_min) / N
    d = np.linspace(d_min, d_max, N)
    
    mean = 5.0
    sigma = 2.0
    p = normal_distribution.normal_distribution(d, mean, sigma)

    print(d)
    print(p)

    plt.plot(d, p, '-o')
    plt.title('Normalised probability density function')
    plt.show()

    print("The median d_median is: ", compute_median(p, d))
