#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
def sigmoid(x):
    return 1/(1+np.exp(-x))

def step_function(x):
    return np.array(x > 0, dtype=int)
#%%
x = np.arange(-5, 5, 0.1)
plt.plot(x, sigmoid(x))
plt.plot(x, step_function(x), linestyle='--')
plt.ylim(-0.1, 1.1)
plt.show()