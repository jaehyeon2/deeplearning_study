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
network = init_network()

batch_size = 100

accuracy_cnt = 0
for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(accuracy_cnt/len(x)))