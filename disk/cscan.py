disk_min = 0
disk_max = 199
start = 130
positions = [8, 113, 81, 154, 195, 85, 42, 156, 154, 146]
seek = 0
done = 0

temp = sorted(positions)

smaller = sorted(i for i in temp if i < start)
smaller.insert(0, disk_min)
larger = sorted(i for i in temp if i >= start)
larger.append(disk_max)
temp = larger + smaller

for pos in temp:
    distance = abs(pos - start)
    seek += distance
    start = pos

print(seek)
