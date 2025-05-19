#%%
import numpy as np
#%%
# If value == 0 -> result became minus infinite value
# Add minimum value 1e-7
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
#%%
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# answer is 2
#%%
# case1: if the answer is expected to be 2
y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
result1 = cross_entropy_error(np.array(y1), np.array(t))
print(result1)
#%%
# case2: if the answer is expected to be 7
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
result2 = cross_entropy_error(np.array(y2), np.array(t))
print(result2)