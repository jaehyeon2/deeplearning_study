#%%
import pickle
import os
import numpy as np
from dataset.mnist import load_mnist
#%%
def sigmoid(x):
    return 1 / (1+np.exp(-x))

def softmax(x):
    c = np.max(x)
    exp_a = np.exp(x-c)
    sum_exp_a = np.sum(exp_a)
    return exp_a/sum_exp_a
#%%
def get_data():
    (x_train, y_train), (x_test, y_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, y_test
#%%
def init_network():
    with open(os.getcwd()+"/sample_weight.pkl", "rb") as f:
        network = pickle.load(f)

    return network
#%%
def predict(network, x):
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)

    return y
#%%
x, t = get_data()
print(x.shape)
network = init_network()
print(network['W1'].shape, network['W2'].shape, network['W3'].shape)
print(network['b1'].shape, network['b2'].shape, network['b3'].shape)
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(accuracy_cnt/len(x)))