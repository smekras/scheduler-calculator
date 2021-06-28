# if arrival == current_time:
#     temp_queue.append()

# if active is empty and wait_queue not empty:
#     load_to_active(wait_queue[0])
#     if active.start == "Unset":
#         active.start = current_time
#     else:
#         active.last = current_time
#     final_queue.append(active)

# active.remain -= 1

# if active.remain == 0 or active.last == current_time - quantum:
#     if active.remain is not 0:
#         active.empty += 1
#         active.segments += 1
#         wait_queue.append(active)
#     else:
#         active.last = active.start
#     active = ""

# for _ in temp_queue:
#     wait_queue.append(_)
