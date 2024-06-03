import math
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

print("F1_score(1, 2, 3) = ", F1_score(1, 2, 3)[0])
print("Precision(1, 2) = ", F1_score(1, 2, 3)[1])
print("Recall(1, 2) = ", F1_score(1, 2, 3)[2])
