#%%
import numpy as np

def logic_and(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    if np.sum(w*x)+b <= 0:
        return 0
    else:
        return 1
#%%
logic_and(0, 0)
#%%
logic_and(1, 0)
#%%
logic_and(0, 1)
#%%
logic_and(1, 1)
#%%
def logic_nand(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    if np.sum(w*x)+b <= 0:
        return 0
    else:
        return 1
#%%
logic_nand(0, 0)
#%%
logic_nand(1, 0)
#%%
logic_nand(0, 1)
#%%
logic_nand(1, 1)
#%%
def logic_or(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.1

    if np.sum(w*x)+b <= 0:
        return 0
    else:
        return 1
#%%
logic_or(0, 0)
#%%
logic_or(1, 0)
#%%
logic_or(0, 1)
#%%
logic_or(1, 1)
#%%
def logic_xor(x1, x2):
    s1 = logic_nand(x1, x2)
    s2 = logic_or(x1, x2)
    return logic_and(s1, s2)
#%%
logic_xor(0, 0)
#%%
logic_xor(1, 0)
#%%
logic_xor(0, 1)
#%%
logic_xor(1, 1)