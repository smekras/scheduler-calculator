pages = [6, 5, 8, 7, 8, 2, 1, 4, 1, 4, 8, 2, 4, 5, 4, 7, 3, 4, 7, 3]
frame = []
index_list = ["", "", ""]

frames = 3
faults = 0
hits = 0
success = False

# while not done:
#     for i in range(len(pages)):
#         page = pages[i]
#         clock += 1
#
#         if page in frame:
#             success.append(True)
#             hits += 1
#         else:
#             remaining = pages[i + 1:]
#             last_index = -1
#             free_option = -1
#
#             for f in frame:
#                 if f in remaining:
#                     f_index = remaining.index(f)
#                     if f_index > last_index:
#                         last_index = f_index
#                 else:
#                     if "-" in frame:
#                         pass
#                     else:
#                         if free_option == -1:
#                             free_option = f
#
#             if free_option != -1:
#                 frame.pop(frame.index(free_option))
#                 frame.insert(0, page)
#                 # frame.insert(frame.index(free_option), page)
#             else:
#                 if "-" not in frame or last_index != -1:
#                     frame.insert(last_index, page)
#                 else:
#                     frame.insert(0, page)
#
#             if len(frame) > 3:
#                 frame.pop(3)
#             success.append(False)
#             faults += 1
#         print(clock, "Frame:", frame, "-", success[clock - 1])
#         virtual.append(page)
#
#     if virtual == pages:
#         done = 1

# for page in pages:
#     if page in frame:
#         success = True
#         hits += 1
#     else:
#         if len(frame) < frames:
#             frame.append(page)
#         else:
#             remaining = pages[pages.index(page)+1:]
#
#             for f in frame:
#                 if f not in remaining:
#                     f = page
#                     break
#                 else:
#                     f_index = frame.index(f)
#                     index_list[f_index] = remaining.index(f)
#             frame[index_list.index(max(index_list))] = page
#
#         success = False
#         faults += 1
#     print(frame, success)

for i in range(len(pages)):
    if pages[i] not in frame:
        if len(frame) < frames:
            frame.append(pages[i])
        else:
            for x in range(len(frame)):
                if frame[x] not in pages[i + 1:]:
                    frame[x] = pages[i]
                    break
                else:
                    index_list[x] = pages[i + 1:].index(frame[x])
            frame[index_list.index(max(index_list))] = pages[i]
        faults += 1
        success = False
    else:
        hits += 1
        success = True
    print("   %d\t\t" % pages[i], end='')
    for x in frame:
        print(x, end=' ')
    for x in range(frames - len(frame)):
        print(' ', end=' ')
    print("\t", success)

print("\nSuccess rate:", hits / len(pages) * 100)
print("Faults:", faults)
print("Hits:", hits)
