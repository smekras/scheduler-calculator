disk_min = 0
disk_max = 199
start = 130
positions = [8, 113, 81, 154, 195, 85, 42, 156, 154, 146]
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
