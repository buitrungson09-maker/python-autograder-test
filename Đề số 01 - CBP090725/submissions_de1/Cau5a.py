s = "hello world"

dem = {}

for ky_tu in s:
    if ky_tu in dem:
        dem[ky_tu] += 1
    else:
        dem[ky_tu] = 1

print(dem)
