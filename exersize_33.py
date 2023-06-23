def func(i, nums, count, incr):
    """"""
    if i >= count:
        return
    print(f"At the top i is {i}")
    nums.append(i)
    print("Numbers now: ", nums)
    print(f"At the bottom i is {i - 1}")
    func(i + incr, nums, count, incr)


p = 0
numbers = []
n = int(input())
addCount = int(input())
func(p, numbers, n, addCount)
print("The numbers: ")
for num in numbers:
    print(num)
