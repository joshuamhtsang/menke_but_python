import numpy as np

def normal_distribution(x, mean, sigma):
    return 1.0/((np.sqrt(2.0*np.pi)*sigma))*np.exp(-np.power(x-mean,2)/(2*sigma*sigma))
