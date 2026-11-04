def DemChuSoLe(n):
    dem = 0

    while n > 0:
        chu_so = n % 10

        if chu_so % 2 != 0:
            dem += 1

        n //= 10

    return dem


n = int(input("Nhập số nguyên dương n: "))

print("Số lượng chữ số lẻ:", DemChuSoLe(n))