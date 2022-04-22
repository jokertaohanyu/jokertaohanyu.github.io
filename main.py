L = [1, 3, 5, 7, 9, 19]
def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)
total = 0
for i in L:
    total = total + func(i)
print(total)

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j}\t', end='')
    print()

a=range(1,20,2)
print(list(a))