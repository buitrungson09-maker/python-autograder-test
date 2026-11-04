danh_sach = []

while True:
    x = int(input("Nhập số nguyên, nhập 0 để dừng: "))

    if x == 0:
        break

    danh_sach.append(x)

k = int(input("Nhập k cần đếm: "))

dem = 0

for x in danh_sach:
    if x == k:
        dem += 1

print("Số lần xuất hiện của k:", dem)