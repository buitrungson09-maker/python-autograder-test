<div align="center">

# 🐍 Python Autograder Test

**Luyện Python từng bài · Kiểm tra tự động · Theo dõi tiến bộ**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bài luyện](https://img.shields.io/badge/Đề_11301-13_ý-2563EB?style=for-the-badge)
![Kiểm thử](https://img.shields.io/badge/Bộ_test-41_trường_hợp-7C3AED?style=for-the-badge)

[Bài làm](submissions_de2/) · [Bộ test](test_de2.py) · [Bộ chấm](autograde_de2.py) · [Chạy nhanh](#-chạy-nhanh)

</div>

---

## 👋 Giới thiệu

Mình là **Bùi Trung Sơn**, sinh viên **Cao đẳng Công Thương TP.HCM**. Đây là nơi mình lưu bài luyện lập trình Python, thực hành giải đề và kiểm tra kết quả bằng bộ chấm tự động.

Mỗi ý được tách thành một file nhỏ để dễ đọc, chạy thử và sửa lỗi. Nội dung hiện có tập trung vào số nguyên, hàm, chuỗi, danh sách, từ điển và lập trình hướng đối tượng.

## 🏁 Tiến độ đề 11301

| Hạng mục | Kết quả |
| :--- | :--- |
| Bài làm | Hoàn thành 13 ý thuộc 5 câu |
| Kiểm thử | 41 trường hợp trong bộ test |
| Kết quả chạy trên máy Windows | **10,00 / 10** |
| Ngày ghi nhận | 04/11/2026 |
| Phiên bản đã đẩy lên GitHub | [`1065586`](https://github.com/buitrungson09-maker/python-autograder-test/commit/1065586) |

> Kết quả trên được ghi nhận từ lần chạy bộ chấm trên máy cá nhân. Đây là bộ kiểm thử luyện tập; điểm thể hiện mức đáp ứng các test hiện có, chưa thay thế việc xem xét thuật toán và yêu cầu của giảng viên.

## 🚀 Chạy nhanh

Mở Terminal PowerShell trên Windows:

```powershell
git clone https://github.com/buitrungson09-maker/python-autograder-test.git
cd python-autograder-test
python autograde_de2.py
```

Nếu đã có repo tại `D:\python-autograder-test`:

```powershell
cd D:\python-autograder-test
python autograde_de2.py
```

Nếu máy dùng lệnh `py`, thay `python` bằng `py`.

Bộ chấm đề 11301 sử dụng thư viện chuẩn Python, không cần cài thêm gói bằng `pip`.

## 📚 Nội dung 5 câu

| Câu | Nội dung thực hành | File bài làm | Điểm |
| :---: | :--- | :--- | :---: |
| 1 | Kiểm tra n hợp lệ, đếm chữ số lẻ, tính tổng phân số | [1a](submissions_de2/Cau1a.py) · [1b](submissions_de2/Cau1b.py) · [1c](submissions_de2/Cau1c.py) | 2 |
| 2 | Đếm chữ hoa, kiểm tra đối xứng, cộng chữ số trong chuỗi | [2a](submissions_de2/Cau2a.py) · [2b](submissions_de2/Cau2b.py) · [2c](submissions_de2/Cau2c.py) | 2 |
| 3 | Nhập list đến số 0, tổng dương chẵn, đếm phần tử | [3a](submissions_de2/Cau3a.py) · [3b](submissions_de2/Cau3b.py) · [3c](submissions_de2/Cau3c.py) | 2 |
| 4 | Lưu thông tin sách bằng dictionary, xóa sách theo mã | [4a](submissions_de2/Cau4a.py) · [4b](submissions_de2/Cau4b.py) | 2 |
| 5 | Tạo lớp DienThoai, khởi tạo và hiển thị hai đối tượng | [5a](submissions_de2/Cau5a.py) · [5b](submissions_de2/Cau5b.py) | 2 |

**Tổng: 13 ý · 10 điểm.** Khi nộp theo đề gốc, cần tổ chức lại thành **5 file Python**, mỗi câu một file.

## 🗂️ Các thành phần của đề 11301

| Thành phần | Vai trò |
| :--- | :--- |
| [`submissions_de2/`](submissions_de2/) | Chứa 13 file lời giải từ `Cau1a.py` đến `Cau5b.py` |
| [`test_de2.py`](test_de2.py) | Dữ liệu đầu vào, kết quả mong đợi, kiểu so sánh và điểm từng ý |
| [`autograde_de2.py`](autograde_de2.py) | Chạy bài làm, kiểm tra đầu ra và tổng hợp điểm |

Tên file dùng đúng chữ hoa/thường như trong bộ test: **`Cau1a.py`**, **`Cau5a.py`**.

## 💻 Học và chạy trong VS Code

1. Chọn **File → Open Folder** và mở thư mục repo.
2. Mở file cần luyện trong `submissions_de2`.
3. Viết hoặc chỉnh sửa bài, sau đó chọn **File → Save All**.
4. Chạy riêng một bài để nhập dữ liệu bằng tay:

   ```powershell
   python submissions_de2/Cau1b.py
   ```

5. Chạy bộ chấm để kiểm tra toàn bộ:

   ```powershell
   python autograde_de2.py
   ```

Bộ chấm mặc định tìm bài trong `submissions_de2`. Có thể truyền một thư mục khác:

```powershell
python autograde_de2.py "D:\duong-dan\bai-lam"
```

## 🧪 Bộ chấm hoạt động thế nào?

| Dạng bài | Cách kiểm tra |
| :--- | :--- |
| Kết quả số | So sánh số cuối trong đầu ra; cho phép sai số `1e-6` |
| Chuỗi đối xứng | Chấp nhận có/không dấu, thông báo ngắn, True/False hoặc 1/0 |
| List và dictionary | Đọc cấu trúc dữ liệu từ đầu ra rồi so sánh giá trị |
| Câu 5a | Chỉ chấm thông tin điện thoại được in; có hỗ trợ gọi lớp cũ để lấy đầu ra |
| Hai điện thoại mẫu | Kiểm tra đầu ra chứa đầy đủ các giá trị yêu cầu |

Mỗi test có thời hạn **3 giây**. Bài thiếu file, gặp lỗi chạy hoặc quá thời gian không được điểm ở test tương ứng. Điểm từng ý tính theo tỷ lệ test đúng nhân trọng số.

Bộ chấm chỉ xét kết quả đầu ra, không bắt buộc tên hàm, biến, thuộc tính hay thuật toán. Câu 5a chấp nhận in trực tiếp đủ thông tin DT01; nếu bài cũ chỉ khai báo lớp `DienThoai`, bộ chấm sẽ gọi lớp để lấy đầu ra. List/dict vẫn phải biểu diễn đúng dữ liệu mong đợi. Khi nộp bài, tự đối chiếu thêm yêu cầu viết hàm và lớp trong đề gốc.

<details>
<summary><strong>📝 Quy ước nhập/xuất để luyện từng ý độc lập</strong></summary>

- **Câu 1a:** nhập lại đến khi `1 <= n <= 1500`, cuối cùng in n hợp lệ.
- **Câu 1b, 1c:** mỗi file tự nhập n.
- **Câu 2:** mỗi ý tự nhập chuỗi; đếm hoặc tính tổng được 0 thì in số 0.
- **Câu 2b:** có thể in `Doi xung` / `Khong doi xung`, thông báo có dấu, hoặc `True` / `False` (tương ứng `1` / `0`); vẫn phân biệt hoa/thường khi xét chuỗi đầu vào.
- **Câu 3:** mỗi ý tự nhập các số, mỗi số một dòng; nhập 0 để dừng, không thêm số 0 kết thúc vào list. Ý 3c nhập thêm k sau đó.
- **Câu 4:** nhập số lượng sách rồi lần lượt nhập mã, tên, tác giả, nhà xuất bản và năm của mỗi cuốn. Năm là số nguyên. Dùng dict dạng `{"S01": ["Python", "An", "NXB A", 2020]}`.
- **Câu 4b:** nhập thêm mã cần xóa; in dict cuối cùng sau khi xử lý. Nếu không có mã, chỉ cần giữ đúng dict cuối cùng; thông báo không bắt buộc.
- **Câu 5a:** in đủ `DT01`, `iPhone 15 Pro`, `Apple`, `3274`, `28990000`, hoặc giữ lớp `DienThoai` và phương thức hiển thị như bài cũ để bộ chấm gọi lấy đầu ra.
- **Câu 5b:** có thể lấy lớp bằng `from Cau5a import DienThoai`; hai file phải cùng thư mục.

In list/dict trên một dòng để bộ chấm đọc được. Các quy ước này giúp chấm riêng từng ý, cụ thể hóa đầu ra của bài luyện.

</details>

## 🔧 Xử lý lỗi thường gặp

| Hiện tượng | Cách xử lý |
| :--- | :--- |
| Không mở được `autograde_de2.py` | Kiểm tra Terminal đang ở thư mục gốc repo |
| Báo thiếu file bài làm | Kiểm tra tên file và vị trí trong `submissions_de2` |
| Đầu ra rỗng | Lưu file, kiểm tra đã gọi hàm và có lệnh `print` |
| Câu 5a không có đầu ra | In đủ thông tin DT01, hoặc dùng lớp và phương thức hiển thị của bài cũ |
| Không tìm thấy list/dict hợp lệ | In cấu trúc bằng `print(danh_sach)` hoặc `print(thu_vien)` |
| Quá thời gian | Kiểm tra điều kiện dừng vòng lặp và số lần nhập dữ liệu |

## 🌱 Hướng luyện tập tiếp theo

- [x] Hoàn thành 13 ý của đề 11301.
- [x] Chạy bộ test đạt 10/10 trên máy cá nhân.
- [x] Lưu bài làm và bộ chấm lên GitHub.
- [ ] Tự giải lại từng câu, giải thích được từng dòng.
- [ ] Gộp bài thành 5 file theo cách tổ chức của đề gốc.
- [ ] Bổ sung thêm trường hợp biên và kiểm thử.
- [ ] Tự động chạy kiểm thử bằng GitHub Actions.

---

<div align="center">

**Bùi Trung Sơn** · [GitHub](https://github.com/buitrungson09-maker)

<sub>Học từng bước, hiểu từng dòng, kiểm tra từng bài.</sub>

</div>
