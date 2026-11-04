danh_sach = []

while True:
    x = int(input("Nhập số nguyên, nhập 0 để dừng: "))

    if x == 0:
        break

    danh_sach.append(x)

tong = 0

for x in danh_sach:
    if x > 0 and x % 2 == 0:
        tong += x

print("Tổng các số dương chẵn:", tong)