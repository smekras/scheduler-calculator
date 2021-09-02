disk_min = 0
disk_max = 199
start = 158
positions = [53, 155, 119, 129, 103, 78, 93, 48, 157, 73]
seek = 0
done = 0

temp = sorted(positions)

smaller = sorted(i for i in temp if i < start)
larger = sorted(i for i in temp if i >= start)
temp = larger + smaller
print(temp)

for pos in temp:
    distance = abs(pos - start)
    seek += distance
    start = pos

print(seek)
