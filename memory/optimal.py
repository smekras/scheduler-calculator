pages = [6, 5, 8, 7, 8, 2, 1, 4, 1, 4, 8, 2, 4, 5, 4, 7, 3, 4, 7, 3]

frame = ["-", "-", "-"]
safe = []
success = []
virtual = []

frames = 3
clock = 0
next_page = 0
last_page = 0
faults = 0
hits = 0
done = 0

while not done:
    for page in pages:
        page_index = pages.index(page)
        clock += 1

        if page in frame:
            success.append(True)
            hits += 1
            print(clock, "Frame:", frame, "-", success[clock - 1])

        if page not in frame:
            if page_index + 1 <= len(pages):
                next_page = pages[page_index + 1]
            if page_index + 2 <= len(pages):
                last_page = pages[page_index + 2]

            if next_page and next_page in frame:
                safe.append(frame.index(next_page))

            if last_page and last_page in frame:
                safe.append(frame.index(last_page))

            print(safe)

            for i in range(len(frame), 0, 1):
                if frame[i] not in safe:
                    frame.append(frame.pop(i))

            safe = []
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
