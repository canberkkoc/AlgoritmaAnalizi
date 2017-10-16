def pw(x, y):
    result = 1
    for i in range(y):
        result = result * x
    return result

print(pw(2,3))
