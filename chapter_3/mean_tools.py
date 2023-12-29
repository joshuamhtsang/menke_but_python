import numpy as np
import matplotlib.pyplot as plt
import normal_distribution

def compute_mean(p, d):
    # Ensure p and d arrays are the same length, deduce array lengths
    if len(p) == len(d):
        N = len(p)
    else:
        raise  Exception("The input arrays p and d should have the same length.")

    # Deduce delta_d
    try:
        delta_d = np.abs(d[1] - d[0])
    except IndexError:
        print("Unable to deduce delta_d due to index out of bounds.")
    
    # Mean is computed from: \int_{d_min}^{d_max} d*p(d)*dd i.e eqn (3.3) in Menke book
    integrand = d*p
    slice_areas = integrand*delta_d

    cum_area = np.cumsum(slice_areas)
    return cum_area[-1]

if __name__ == '__main__':
    print("Compute mean of a probability distribution, p(d)")

    N = 1100
    d_min = -20.0
    d_max = 20.0
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

    print("The mean d_mean is: ", compute_mean(p, d))