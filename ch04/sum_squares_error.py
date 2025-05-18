#%%
import numpy as np
#%%
def sum_squares_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)
#%%
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# answer is 2
#%%
# case1: if the answer is expected to be 2
y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
result1 = sum_squares_error(np.array(y1), np.array(t))
result1
#%%
# case2: if the answer is expected to be 7
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
result2 = sum_squares_error(np.array(y2), np.array(t))
result2