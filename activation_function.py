import math
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

print("sigmoid: ",activation_function(3, "sigmoid"))
print("relu: ", activation_function(3, "relu"))
print("elu:" ,activation_function(3, "elu"), "\n")