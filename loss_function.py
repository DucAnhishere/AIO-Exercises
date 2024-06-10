import random
import math
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
    
print("mse loss: ", caculate_loss(10)[0])
print("mae loss: ", caculate_loss(10)[1])
print("rmse loss: ", caculate_loss(10)[2], "\n")