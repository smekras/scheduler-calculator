pages = [6, 2, 5, 2, 3, 6, 8, 3, 6, 2, 8, 3, 5, 6, 5, 4, 1, 8, 2, 3]

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
            page_index = frame.index(page)
            frame.pop(page_index)
            frame.insert(0, page)
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
