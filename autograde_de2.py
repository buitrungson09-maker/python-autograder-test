import ast
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata

from test_de2 import tests, kinds, weights


ROOT = Path(__file__).resolve().parent


def normalize(text):
    # Chap nhan ca tieng Viet co dau va khong dau.
    text = str(text).casefold().replace("\u0111", "d")
    text = unicodedata.normalize("NFD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    return " ".join(text.split()).rstrip(".!:")


def last_literal(output, literal_type):
    # Tìm list/dict cuối cùng được in ra.
    for line in reversed(output.splitlines()):
        for position, char in enumerate(line):
            if char not in "[{":
                continue

            try:
                value = ast.literal_eval(line[position:])
            except (ValueError, SyntaxError):
                continue

            if isinstance(value, literal_type):
                return value

    raise ValueError("Không tìm thấy list/dict được in hợp lệ")


def phone_output_command(path, case):
    # Ho tro lop cu de lay dau ra; khong kiem tra thuoc tinh.
    harness = '''
import contextlib
import io
import json
import runpy
import sys
import unicodedata

def normalize(text):
    text = str(text).casefold().replace("\\u0111", "d")
    text = unicodedata.normalize("NFD", text)
    return " ".join("".join(c for c in text if not unicodedata.combining(c)).split())

stream = io.StringIO()
with contextlib.redirect_stdout(stream):
    namespace = runpy.run_path(sys.argv[1], run_name="__main__")
output = stream.getvalue()
print(output, end="")
expected = json.loads(sys.argv[2])
if not all(normalize(value) in normalize(output) for value in expected):
    cls = namespace.get("DienThoai")
    if callable(cls):
        phone = cls("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
        phone.thongtindienthoai()
'''
    import json
    return [sys.executable, "-c", harness, str(path), json.dumps(case["expected"])]


def compare(output, case, kind):
    expected = case["expected"]

    if kind == "number":
        numbers = re.findall(
            r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?",
            output,
        )

        return bool(numbers) and math.isclose(
            float(numbers[-1]),
            expected,
            rel_tol=1e-6,
            abs_tol=1e-6,
        )

    if kind == "literal":
        return last_literal(output, list) == expected

    if kind == "dict":
        return last_literal(output, dict) == expected

    if kind == "text":
        wanted = normalize(expected)
        if wanted in ("chuoi doi xung", "chuoi khong doi xung"):
            lines = [normalize(line) for line in output.splitlines() if line.strip()]
            if not lines:
                return False
            line = lines[-1]
            if re.search(r"\bkhong (?:phai )?(?:la )?(?:chuoi )?doi xung$", line):
                actual = False
            elif re.search(r"\bdoi xung$", line):
                actual = True
            elif re.search(r"\b(?:false|0)$", line):
                actual = False
            elif re.search(r"\b(?:true|1)$", line):
                actual = True
            else:
                return False
            return actual == (wanted == "chuoi doi xung")
        return any(normalize(line).endswith(wanted) for line in output.splitlines())

    if kind in ("all_text", "phone_output"):
        return all(
            normalize(value) in normalize(output)
            for value in expected
        )

    raise ValueError(f"Kiểu kiểm tra không hợp lệ: {kind}")


def grade(base_dir):
    total = 0.0

    env = dict(
        os.environ,
        PYTHONIOENCODING="utf-8",
        PYTHONUTF8="1",
    )

    for name, cases in tests.items():
        path = (base_dir / f"{name}.py").resolve()
        correct = 0

        print(f"\n{name} ({weights[name]} điểm)")

        if not path.is_file():
            print(f"  THIẾU FILE: {path}")
            continue

        for index, case in enumerate(cases, 1):
            kind = kinds[name]
            detail = ""

            if kind == "phone_output":
                command = phone_output_command(path, case)
            else:
                command = [sys.executable, str(path)]

            try:
                result = subprocess.run(
                    command,
                    input=case["input"],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=3,
                    cwd=base_dir,
                    env=env,
                )

                if result.returncode != 0:
                    ok = False

                    if result.stderr.strip():
                        detail = result.stderr.strip().splitlines()[-1]
                    else:
                        detail = f"Mã thoát {result.returncode}"
                else:
                    ok = compare(result.stdout, case, kind)

                    if not ok:
                        detail = (
                            f"Mong đợi: {case['expected']!r}; "
                            f"nhận: {result.stdout.strip()!r}"
                        )

            except subprocess.TimeoutExpired:
                ok = False
                detail = "Quá thời gian 3 giây"

            except (ValueError, OSError) as error:
                ok = False
                detail = str(error)

            correct += int(ok)

            status = "ĐÚNG" if ok else "SAI"
            print(f"  Test {index}: {status}")

            if detail:
                print(f"    {detail}")

        score = weights[name] * correct / len(cases)
        total += score

        print(
            f"  {correct}/{len(cases)} test "
            f"-> {score:.2f} điểm"
        )

    print(f"\nTỔNG ĐIỂM: {total:.2f}/10")
    return total


if __name__ == "__main__":
    if len(sys.argv) > 1:
        base_dir = Path(sys.argv[1]).resolve()
    else:
        base_dir = ROOT / "submissions_de2"

    grade(base_dir)