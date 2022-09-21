import numpy as np

#calculate jacobi matrix: -(x1-2x2)^2
def jacobi(x):
    return np.array([[-2*(x[0]-2*x[1])], [-4*(x[0]-2*x[1])]])
