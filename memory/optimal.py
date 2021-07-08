pages = [6, 5, 8, 7, 8, 2, 1, 4, 1, 4, 8, 2, 4, 5, 4, 7, 3, 4, 7, 3]
frame = []
index_list = ["", "", ""]

frames = 3
faults = 0
hits = 0
success = False

for i in range(len(pages)):
    if pages[i] not in frame:
        if len(frame) < frames:
            frame.append(pages[i])
        else:
            for x in range(len(frame)):
                remaining = pages[i+1:]
                if frame[x] not in remaining:
                    frame[x] = pages[i]
                    break
                else:
                    index_list[x] = remaining.index(frame[x])
            frame[index_list.index(max(index_list))] = pages[i]
        faults += 1
        success = False
    else:
        hits += 1
        success = True

    print(i+1, end=":\t")
    print(pages[i], "\t", end='')
    for f in frame:
        print(f, end=' ')
    for x in range(frames - len(frame)):
        print(' ', end=' ')
    print("\t", success)

print("\nSuccess rate:", hits / len(pages) * 100)
print("Faults:", faults)
print("Hits:", hits)
