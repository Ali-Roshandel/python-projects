# Writing -n to n Forward and Backward
x = int(input('Enter a number: '))
for i in range(-x, x + 1):
    print(i)

for i in range(x, -x - 1, -1):
    print(i)
