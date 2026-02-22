nums = list(map(int, input().split()))

def func(nums):
    for i in range(nums[0], nums[1] + 1):
        yield i * i

for x in func(nums):
    print(x)
