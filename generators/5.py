n = int(input())

def func(n):
    for i in range(n, -1, -1):
        yield i

for x in func(n):
    print(x)
