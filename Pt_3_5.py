def prost(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    return k


print([x for x in range(100) if prost(x) > 0])
