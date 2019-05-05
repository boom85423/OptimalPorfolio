#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_return(stock_price):

    return_list = []
    for i in range(len(stock_price)):
        if i < stock_price.shape[0]-1:
            return_list.append(np.log(stock_price[i+1]/stock_price[i]))

    return np.array(return_list).reshape(-1, 1)


def loss_function(x, y, weight):

    var = sum(np.power(weight[0]*x[:,0] + weight[1]*x[:,1] - 0.1, 2)) / x.shape[0]

    return var


def gradient_descent(x, y, weight, lr, num_iters):

    weight_init = weight.copy()
    loss_history = []
    for i in range(num_iters):
        w0_grad = (2/x.shape[0]) * sum(weight[0]*x[:,0] + weight[1]*x[:,1] - 0.1) * np.mean(x[:,0])
        w1_grad = (2/x.shape[0]) * sum(weight[0]*x[:,0] + weight[1]*x[:,1] - 0.1) * np.mean(x[:,1])
        weight[0] = weight[0] - lr * w0_grad
        weight[1] = weight[1] - lr * w0_grad
        var = loss_function(x, y, weight)
        if i%5000 == 0:
            loss_history.append(var)
            print("[iter {0}]: var={1}".format(i, var))

    print("Variance of equal weight:", loss_function(x, y, weight_init))

    w0 = 1 / (1 + np.exp(-weight[0]))
    w1 = 1 - w0

    return w0, w1, loss_history


if __name__ == "__main__":

    refresh_price = pd.read_csv("refresh_price.csv")
    print("available stock:", refresh_price.columns.values)
    stock_1 = input("input stock_1: ")
    stock_2 = input("input stock_2: ")
    stock_1_return = get_return(refresh_price[stock_1].values[0:1000])
    stock_2_return = get_return(refresh_price[stock_2].values[0:1000])

    portfolio = np.hstack((stock_1_return, stock_2_return))
    weight = [0.5, 0.5]
    expect_return = float(input("input expect_return: "))
    lr = 1
    num_iters = 500000
    w0, w1, loss_history = gradient_descent(portfolio, expect_return, weight, lr, num_iters)
    print("Best weight with min variance: ({0}, {1})".format(w0, w1))

    plt.plot(loss_history)
    plt.title("loss with iters")
    plt.show()



