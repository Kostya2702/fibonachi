
def fibonachi(elements):
    a = b = 1
    for i in range(0, elements):
        a, b = b, a + b
        
        print(a)

fibonachi(10)
