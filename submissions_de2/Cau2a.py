s = input("Nhập chuỗi s: ")

dem = 0

for ky_tu in s:
    if ky_tu.isupper():
        dem += 1

print("Số ký tự chữ hoa:", dem)