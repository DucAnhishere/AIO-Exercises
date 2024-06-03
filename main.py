import math
import random

#Ex1
def F1_score(TP, FP, FN):
    if not isinstance(TP, int):
        raise TypeError("TP must be an integer")
    if not isinstance(FP, int):
        raise TypeError("FP must be an integer")
    if not isinstance(FN, int):
        raise TypeError("FN must be an integer")
    Precision = (TP) / (TP + FP)
    Recall = (TP) / (TP + FN)
    F1_score = 2 * (Precision * Recall) / (Precision + Recall)
    if TP <= 0 or FP <= 0 or FN <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    return F1_score, Precision, Recall

#Ex2
e = math.e

def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def sigmoid(x):
    if not is_number(x):
        print("x must be a number")
        return
    return 1 / (1 + e ** (-x))


def relu(x):
    if not is_number(x):
        print("x must be a number")
        return
    if x > 0:
        return x
    else:
        x = 0
    return x


def elu(x, alpha=0.01):
    if not is_number(x):
        print("x must be a number")
        return
    return x if x > 0 else alpha * (e ** x - 1)


def activation_function(x, activation_name):
    x = float(x)
    if activation_name == "sigmoid":
        return sigmoid(x)
    elif activation_name == "relu":
        return relu(x)
    elif activation_name == "elu":
        return elu(x)
    else:
        print(activation_name + "is not supported")
        return
    
#Ex3
def caculate_loss(num_samples):
    try:
        num_samples = int(num_samples)
    except ValueError:
        print("number of samples must be an integer number")
        return

    def MSE(y_pred, y):
        return (y_pred - y) ** 2

    def MAE(y_pred, y):
        return abs(y_pred - y)

    def RMSE(y_pred, y):
        return math.sqrt((y_pred - y) ** 2)

    for i in range(num_samples):
        y_pred = random.uniform(0, 10)
        y = random.uniform(0, 10)
        mse_loss = MSE(y, y_pred)
        mae_loss = MAE(y, y_pred)
        rmse_loss = RMSE(y, y_pred)
        return mse_loss, mae_loss, rmse_loss
    
#Ex4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2*i + 1)) / factorial(2*i + 1)
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2*i)) / factorial(2*i)
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2*i + 1)) / factorial(2*i + 1)
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2*i)) / factorial(2*i)
    return result

#Ex5
def MD_nRE(y, y_hat, n, p):
    loss = abs(y - y_hat) / (abs(y) ** (1/p)) ** (1/n)
    return loss

print("F1_score(1, 2, 3) = ", F1_score(1, 2, 3)[0])
print("Precision(1, 2) = ", F1_score(1, 2, 3)[1])
print("Recall(1, 2) = ", F1_score(1, 2, 3)[2], "\n")

print("sigmoid: ",activation_function(3, "sigmoid"))
print("relu: ", activation_function(3, "relu"))
print("elu:" ,activation_function(3, "elu"), "\n")

print("mse loss: ", caculate_loss(10)[0])
print("mae loss: ", caculate_loss(10)[1])
print("rmse loss: ", caculate_loss(10)[2], "\n")

print("approx_sin: ", approx_sin(3.14, 10))
print("approx_cos: ", approx_cos(3.14, 10))
print("approx_sinh: ", approx_sinh(3.14, 10))
print("approx_cosh: ", approx_cosh(3.14, 10), "\n")

print("MD_nRE: ", MD_nRE(1, 2, 3, 4))