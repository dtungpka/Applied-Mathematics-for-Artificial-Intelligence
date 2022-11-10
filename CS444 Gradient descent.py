import numpy as np

_X = np.array([[1, -2, 0], [2, 5, 1]])
Y = np.array([1,6,1])
X = np.ones(np.shape(_X.T)[0])
X = np.vstack((X, _X.T))
w = np.array([0,1,5]).T
def h(w,x):
    return  w.T @ X
def loss(w,x,y):
    return 0.5*np.sum((y.T - h(w,x))**2)
def grad_descent(w,x,y):
    return  w + 0.1*(Y.T - h()) @ X
for i in range(100):
    print(f"{i}: {loss()}")
    w = grad_descent()

print(f"Final: {loss()} {w}")
