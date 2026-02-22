n = int(input())
def square(n):
    cnt = 1
    while cnt <= n:
        yield cnt * cnt
        cnt += 1

sq = square(n)

for i in sq:
    print(i)
