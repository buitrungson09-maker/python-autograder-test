# Bộ test đề Python mã 11301.
# Mỗi ý tương ứng một file: Cau1a.py, Cau1b.py, ...

tests = {
    "Cau1a": [
        {"input": "1\n", "expected": 1},
        {"input": "1500\n", "expected": 1500},
        {"input": "0\n-1\n1501\n635\n", "expected": 635},
    ],

    "Cau1b": [
        {"input": "635\n", "expected": 2},
        {"input": "248\n", "expected": 0},
        {"input": "1111\n", "expected": 4},
        {"input": "1500\n", "expected": 2},
    ],

    "Cau1c": [
        {"input": "1\n", "expected": 0.5},
        {"input": "2\n", "expected": 0.75},
        {"input": "3\n", "expected": 11 / 12},
        {
            "input": "10\n",
            "expected": sum(1 / (2 * i) for i in range(1, 11)),
        },
    ],

    "Cau2a": [
        {"input": "AbC123\n", "expected": 2},
        {"input": "python\n", "expected": 0},
        {"input": "ABC XYZ\n", "expected": 6},
        {"input": "\n", "expected": 0},
    ],

    "Cau2b": [
        {"input": "abba\n", "expected": "Chuỗi đối xứng"},
        {"input": "abc\n", "expected": "Chuỗi không đối xứng"},
        {"input": "a\n", "expected": "Chuỗi đối xứng"},
        {"input": "Aa\n", "expected": "Chuỗi không đối xứng"},
    ],

    "Cau2c": [
        {"input": "abc123\n", "expected": 6},
        {"input": "a9b0c8\n", "expected": 17},
        {"input": "Python\n", "expected": 0},
        {"input": "\n", "expected": 0},
    ],

    "Cau3a": [
        {"input": "1\n-2\n3\n0\n", "expected": [1, -2, 3]},
        {"input": "0\n", "expected": []},
        {"input": "2\n2\n0\n", "expected": [2, 2]},
    ],

    "Cau3b": [
        {"input": "-2\n2\n4\n3\n0\n", "expected": 6},
        {"input": "1\n-4\n3\n0\n", "expected": 0},
        {"input": "0\n", "expected": 0},
        {"input": "2\n2\n6\n0\n", "expected": 10},
    ],

    "Cau3c": [
        {"input": "2\n3\n2\n0\n2\n", "expected": 2},
        {"input": "1\n3\n0\n2\n", "expected": 0},
        {"input": "0\n0\n", "expected": 0},
        {"input": "-1\n-1\n2\n0\n-1\n", "expected": 2},
    ],

    "Cau4a": [
        {
            "input": "1\nS01\nPython\nAn\nNXB A\n2020\n",
            "expected": {
                "S01": ["Python", "An", "NXB A", 2020],
            },
        },
        {
            "input": (
                "2\n"
                "S01\nPython\nAn\nNXB A\n2020\n"
                "S02\nGodot\nBinh\nNXB B\n2021\n"
            ),
            "expected": {
                "S01": ["Python", "An", "NXB A", 2020],
                "S02": ["Godot", "Binh", "NXB B", 2021],
            },
        },
    ],

    "Cau4b": [
        {
            "input": "1\nS01\nPython\nAn\nNXB A\n2020\nS01\n",
            "expected": {},
        },
        {
            "input": "1\nS01\nPython\nAn\nNXB A\n2020\nS99\n",
            "expected": {
                "S01": ["Python", "An", "NXB A", 2020],
            },
            "message": "Không tìm thấy cuốn sách cần xóa",
        },
        {
            "input": (
                "2\n"
                "S01\nPython\nAn\nNXB A\n2020\n"
                "S02\nGodot\nBinh\nNXB B\n2021\n"
                "S01\n"
            ),
            "expected": {
                "S02": ["Godot", "Binh", "NXB B", 2021],
            },
        },
    ],

    "Cau5a": [
        {"input": "", "expected": None},
    ],

    "Cau5b": [
        {
            "input": "",
            "expected": [
                "DT01", "iPhone 15 Pro", "Apple", "3274", "28990000",
                "DT02", "Galaxy S24 Ultra", "Samsung", "5000", "29990000",
            ],
        },
    ],
}

# Cách so sánh kết quả từng bài.
kinds = {name: "number" for name in tests}

kinds.update({
    "Cau2b": "text",
    "Cau3a": "literal",
    "Cau4a": "dict",
    "Cau4b": "dict",
    "Cau5a": "class",
    "Cau5b": "all_text",
})

# Thang điểm theo từng ý, tổng 10 điểm.
weights = {
    "Cau1a": 0.5,
    "Cau1b": 0.75,
    "Cau1c": 0.75,

    "Cau2a": 0.75,
    "Cau2b": 0.5,
    "Cau2c": 0.75,

    "Cau3a": 0.75,
    "Cau3b": 0.75,
    "Cau3c": 0.5,

    "Cau4a": 1.5,
    "Cau4b": 0.5,

    "Cau5a": 1.0,
    "Cau5b": 1.0,
}