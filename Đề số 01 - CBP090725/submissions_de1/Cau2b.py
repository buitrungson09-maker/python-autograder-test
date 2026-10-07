s = input()
start = int(input())
end = int(input())

doan = s[start - 1:end]

dem = 0
for ky_tu in doan:
    if ky_tu.isdigit():
        dem += 1

print(dem)
