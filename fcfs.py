processes = [
    {"name": "P1", "arrival": 1, "burst": 3, "remain": 3, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
    {"name": "P2", "arrival": 3, "burst": 7, "remain": 7, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
    {"name": "P3", "arrival": 5, "burst": 1, "remain": 1, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
    {"name": "P4", "arrival": 11, "burst": 5, "remain": 5, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
    {"name": "P5", "arrival": 13, "burst": 2, "remain": 2, "start": "Unset", "last": 0, "end": "Unset", "segments": 1}]

control = ["--", "P1", "P1", "P1", "P2", "P2", "P2", "P2", "P2", "P2",
           "P2", "P3", "P4", "P4", "P4", "P4", "P4", "P5", "P5", "--"]

active = []
running_queue = []
wait_queue = processes
final_queue = []

done = 0
current_time = 0

while not done:
    if active:
        if active[0]["remain"] > 0:
            active[0]["remain"] -= 1
            if active[0]["remain"] == 0:
                active[0]["end"] = current_time
                running_queue.append(active[0])
                active.pop(0)
    if not active:
        if wait_queue:
            if wait_queue[0]["arrival"] <= current_time:
                wait_queue[0]["start"] = current_time
                wait_queue[0]["last"] = current_time
                active.append(wait_queue[0])
                wait_queue.pop(0)

    if active:
        final_queue.append(active[0]["name"])
    else:
        final_queue.append("--")

    if not wait_queue and not active:
        done = 1

    # print("Time:", current_time)
    # if active:
    #     print("Active:", active[0]["name"])
    # else:
    #     print("Active: --")

    current_time += 1

turnaround = []
wait = []

for p in running_queue:
    tt = p["end"] - p["arrival"]
    turnaround.append(tt)
    wt = tt - p["burst"]
    wait.append(wt)

print("\nAverage turnaround time:", sum(turnaround) / len(turnaround))
print("\nAverage waiting time:", sum(wait) / len(wait))

if final_queue == control:
    print("\nSuccess:", final_queue)
else:
    print("\nFailure:", final_queue)
