# calculate y = x^n

def expo(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * expo(x, n - 1)