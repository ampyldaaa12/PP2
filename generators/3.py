n = int(input())

def calc(n):
    for i in range(0, n + 1):
        if i % 4 == 0 and i % 3 == 0:
            yield i

for x in calc(n):
    print(x, end =" ")