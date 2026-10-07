a = int(input())
b = int(input())

tong = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        tong += i

print(tong)
