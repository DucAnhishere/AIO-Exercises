def MD_nRE(y, y_hat, n, p):
    loss = abs(y - y_hat) / (abs(y) ** (1/p)) ** (1/n)
    return loss

print("MD_nRE: ", MD_nRE(1, 2, 3, 4))