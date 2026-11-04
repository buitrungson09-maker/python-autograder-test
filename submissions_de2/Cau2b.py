def DoiXung(s):
    return s == s[::-1]


s = input("Nhập chuỗi s: ")

if DoiXung(s):
    print("Chuỗi đối xứng")
else:
    print("Chuỗi không đối xứng")