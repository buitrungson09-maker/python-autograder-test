def TinhS(n):
    tong = 0

    for i in range(1, n + 1):
        tong += 1 / (2 * i)

    return tong


n = int(input("Nhập số nguyên dương n: "))

print("S =", TinhS(n))