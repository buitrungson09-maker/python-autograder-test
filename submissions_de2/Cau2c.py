s = input("Nhập chuỗi s: ")

tong = 0

for ky_tu in s:
    if "0" <= ky_tu <= "9":
        tong += int(ky_tu)

print("Tổng các chữ số:", tong)