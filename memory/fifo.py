import time

pages = [6, 5, 8, 7, 8, 2, 1, 4, 1, 4, 8, 2, 4, 5, 4, 7, 3, 4, 7, 3]

frame = ["-", "-", "-"]
hits = []
virtual = []

frames = 3
clock = 0
first = 0
last = 0
done = 0

while not done:
    time.sleep(1)
    for page in pages:

        if page in frame:
            hits.append(True)
            print(clock, "Frame:", frame, "-", hits[clock])

        if page not in frame:
            frame[last] = page
            last = frame.index(page)
            if last == 2:
                last = 0
            else:
                last += 1
            hits.append(False)
            print(clock, "Frame:", frame, "-", hits[clock])

        virtual.append(page)
        clock += 1

    if virtual == pages:
        done = 1

print("\nVirtual:", virtual)
