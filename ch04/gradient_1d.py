#%%
def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)
#%%
def function_1(x):
    return 0.01*x**2 + 0.1*x
#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()
#%%
def function_2(x):
    return x[0]**2 + x[1]**2
#%%
# x0 = 3, x1 = 4 일때 / x0에 대한 편미분
def function_tmp1(x0):
    return x0*x0+ 4.0**2.0

numerical_diff(function_tmp1, 3.0)
#%%
# x0 = 3, x1 = 4 일때 / x1에 대한 편미분
def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

numerical_diff(function_tmp2, 4.0)