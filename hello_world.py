
def summa_kratnyh(t, f, c):
    result = 0
    for i in range(1, c):
        if i % t == 0  or i % f == 0:
            result += i
    print(result)

summa_kratnyh(3, 5, 1000)
