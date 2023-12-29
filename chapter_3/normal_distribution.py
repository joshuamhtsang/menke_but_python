import numpy as np

# Compute the normal distribution for coordinates array x
# i.e eqn (3.5) in Menke book
def normal_distribution(x, mean, sigma):
    return 1.0/((np.sqrt(2.0*np.pi)*sigma))*np.exp(-np.power(x-mean,2)/(2*sigma*sigma))

# Computer normalized normal distribution in 2 dimensions
# i.e. eqn (3.24) in Menke book
def normal_distribution_2d(x_1, x_2, xbar_1, xbar_2, sigma_1, sigma_2):
    norm = 1.0/(2*np.pi*sigma_1*sigma_2)
    p_1 = np.exp(-np.power(x_1-xbar_1,2)/(2*sigma_1*sigma_1))
    p_2 = np.exp(-np.power(x_2-xbar_2,2)/(2*sigma_2*sigma_2))
    return norm*np.outer(p_1, p_2)
