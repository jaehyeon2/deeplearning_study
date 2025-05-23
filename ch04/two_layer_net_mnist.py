import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet
import matplotlib.pyplot as plt

(x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, one_hot_label = True)


# hyper parameter
iters_num = 1
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

# epoch - one complete pass through the entire training dataset
iter_per_epoch = max(train_size / batch_size, 1)

network = TwoLayerNet(input_size = 784, hidden_size = 50, output_size=10)

for i in range(iters_num):

    # mnist batch
    batch_mask = np.random.choice(train_size, batch_size)

    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # cal grad
    grad = network.numerical_gradient(x_batch, t_batch)

    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    # training history
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    print(loss)

    if i % iter_per_epoch == 0:

        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)

        train_acc_list.append(train_acc)
        test_acc_list.append(train_acc)

        print("train acc, test acc - " + str(train_acc) + ", " + str(test_acc))