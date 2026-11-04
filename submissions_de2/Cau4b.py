from datetime import datetime


n = int(input("Nhập số lượng sách: "))

while n <= 0:
    n = int(input("Nhập lại số lượng sách lớn hơn 0: "))

thu_vien = {}
nam_hien_tai = datetime.now().year

for i in range(n):
    ma_sach = input("Nhập mã sách: ")
    ten_sach = input("Nhập tên sách: ")
    tac_gia = input("Nhập tên tác giả: ")
    nha_xuat_ban = input("Nhập nhà xuất bản: ")
    nam_xuat_ban = int(input("Nhập năm xuất bản: "))

    while nam_xuat_ban > nam_hien_tai:
        nam_xuat_ban = int(input("Năm vượt quá hiện tại, nhập lại: "))

    thu_vien[ma_sach] = [
        ten_sach,
        tac_gia,
        nha_xuat_ban,
        nam_xuat_ban,
    ]

ma_can_xoa = input("Nhập mã sách cần xóa: ")

if ma_can_xoa in thu_vien:
    del thu_vien[ma_can_xoa]
    print("Đã xóa cuốn sách.")
else:
    print("Không tìm thấy cuốn sách cần xóa")

print(thu_vien)