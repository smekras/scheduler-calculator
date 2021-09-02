disk_min = 0
disk_max = 199
start = 158
positions = [53, 155, 119, 129, 103, 78, 93, 48, 157, 73]

seek = 0

for p in positions:
    distance = abs(p - start)
    seek += distance
    start = p

print(seek)
