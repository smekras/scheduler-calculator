disk_min = 0
disk_max = 199
start = 158
positions = [53, 155, 119, 129, 103, 78, 93, 48, 157, 73]
seek = 0
done = 0


def find_dist(array, s):
    distances = []
    for a in array:
        distance = abs(a - s)
        distances.append({"position": a, "distance": distance})
    return sorted(distances, key=lambda k: k['distance'])


temp = positions

while not done:
    new_dist = find_dist(temp, start)

    seek += new_dist[0]["distance"]
    start = new_dist[0]["position"]

    for p in temp:
        if new_dist[0]["position"] == p:
            temp.pop(temp.index(p))

    if not temp:
        done = 1

print(seek)
