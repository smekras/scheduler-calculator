pages = [6, 5, 8, 7, 8, 2, 1, 4, 1, 4, 8, 2, 4, 5, 4, 7, 3, 4, 7, 3]

frame = ["-", "-", "-"]
success = []
virtual = []

frames = 3
clock = 0
first = 0
last = 0
faults = 0
hits = 0
done = 0

while not done:
    for page in pages:
        clock += 1

        if page in frame:
            success.append(True)
            hits += 1
            print(clock, "Frame:", frame, "-", success[clock - 1])

        if page not in frame:
            frame.insert(0, page)
            if len(frame) > 2:
                frame.pop(3)
            success.append(False)
            faults += 1
            print(clock, "Frame:", frame, "-", success[clock - 1])

        virtual.append(page)

    if virtual == pages:
        done = 1

print("\nSuccess rate:", hits / clock)
print("Faults:", faults)
print("Hits:", hits)
