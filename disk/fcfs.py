disk_min = 0
disk_max = 199
start = 130
positions = [8, 113, 81, 154, 195, 85, 42, 156, 154, 146]

seek = 0

for p in positions:
    distance = abs(p - start)
    seek += distance
    start = p

print(seek)
