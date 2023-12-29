import numpy as np
import matplotlib.pyplot as plt
import normal_distribution
import mean_tools
import math

def compute_variance(p, d):
    # Ensure p and d arrays are the same length, deduce array lengths
    if len(p) == len(d):
        N = len(p)
    else:
        raise  Exception("The input arrays p and d should have the same length.")

    # Compute mean
    d_mean = mean_tools.compute_mean(p, d)

    # Deduce delta_d
    try:
        delta_d = d[1] - d[0]
    except IndexError:
        print("Unable to deduce delta_d due to index out of bounds.")
    
    # Variance is computed from: \int_{d_min}^{d_max} (d - d_mean)^2 * p(d) * dd 
    # i.e eqn (3.4) in Menke book
    integrand = (d-d_mean)**2 * p
    slice_areas = integrand*delta_d

    cum_area = np.cumsum(slice_areas)
    return cum_area[-1]

if __name__ == '__main__':
    print("Compute variance of a probability distribution, p(d)")
    N = 100000
    d_min = -30.0
    d_max = 30.0
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

    print("The variance d_variance is: ", compute_variance(p, d))
    print("The sigma is square root of the variance: ", math.sqrt(compute_variance(p, d)))

    # Attempt to compute variance with:
    # Var(d) = E[d^2] - E^2[d]
    d_squared = d**2
    print(d_squared)
    plt.plot(d_squared, p, '-o')
    plt.title('Normalised probability density function')
    plt.show()

    # Compute mean of d^2
    d_mean = mean_tools.compute_mean(p, d_squared)
    print(d_mean)