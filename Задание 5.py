num = (list(range(1,21)))

ch = list(filter(lambda x: x % 2 == 0, num))
print(ch)
plus = list(map(lambda x: x + 10, num))
print(plus)
rev = num.sort(reverse = True)
print(num)