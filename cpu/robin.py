# processes = [
#     {"name": "P1", "arrival": 1, "burst": 3, "remain": 3, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
#     {"name": "P2", "arrival": 3, "burst": 7, "remain": 7, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
#     {"name": "P3", "arrival": 5, "burst": 1, "remain": 1, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
#     {"name": "P4", "arrival": 11, "burst": 5, "remain": 5, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
#     {"name": "P5", "arrival": 13, "burst": 2, "remain": 2, "start": "Unset", "last": 0, "end": "Unset", "segments": 1}]
#
# control = ['--', 'P1', 'P1', 'P2', 'P2', 'P1', 'P3', 'P2', 'P2', 'P2',
#            'P2', 'P4', 'P4', 'P2', 'P5', 'P5', 'P4', 'P4', 'P4', '--']

processes = [
    {"name": "P1", "arrival": 0, "burst": 6, "remain": 6, "start": "Unset", "last": 0, "end": "Unset", "segments": 1,
     "priority": 1},
    {"name": "P2", "arrival": 1, "burst": 2, "remain": 2, "start": "Unset", "last": 0, "end": "Unset", "segments": 1,
     "priority": 1},
    {"name": "P3", "arrival": 2, "burst": 1, "remain": 1, "start": "Unset", "last": 0, "end": "Unset", "segments": 1,
     "priority": 1},
    {"name": "P4", "arrival": 5, "burst": 3, "remain": 3, "start": "Unset", "last": 0, "end": "Unset", "segments": 1,
     "priority": 1},
    {"name": "P5", "arrival": 7, "burst": 4, "remain": 4, "start": "Unset", "last": 0, "end": "Unset", "segments": 1,
     "priority": 1}]

control = ['P1', 'P1', 'P2', 'P2', 'P3', 'P1', 'P1', 'P4', 'P4', 'P5',
           'P5', 'P1', 'P1', 'P4', 'P5', 'P5', '--', '--', '--', '--']

active = []
temp = []
running_queue = []
wait_queue = []
final_queue = []

done = 0
current_time = 0
quantum = 2


def load_active():
    if wait_queue[0]["start"] == "Unset":
        wait_queue[0]["start"] = current_time
    wait_queue[0]["last"] = current_time
    active.append(wait_queue[0])
    wait_queue.pop(0)


def unload_active():
    active[0]["end"] = current_time
    running_queue.append(active[0])
    active.pop(0)


while not done:
    for p in processes:
        if p["arrival"] == current_time:
            wait_queue.append(p)

    if active:
        if active[0]["remain"] > 0:
            active[0]["remain"] -= 1
            if active[0]["remain"] == 0:
                unload_active()
            if active and active[0]["last"] == current_time - quantum:
                active[0]["segments"] += 1
                temp = active[0]
                active.pop(0)

    if wait_queue:
        while temp != []:
            for p in wait_queue:
                if p["arrival"] >= current_time:
                    wait_queue.insert(0, temp)
                    temp = []
                    print("1", wait_queue)
                # if active and p["arrival"] < 0:
                #     print("2", wait_queue)
                #     wait_queue.insert(1, active[0])
                #     active.pop(0)

    if active and active[0]["remain"] == 0:
        unload_active()

    if not active and wait_queue:
        if wait_queue[0]["arrival"] <= current_time:
            load_active()

    if active:
        final_queue.append(active[0]["name"])
    else:
        final_queue.append("--")

    print("Time:", current_time, end=" > ")
    if active:
        print(active[0]["name"])
    else:
        print("--")

    current_time += 1

    if current_time == 20:
        done = 1

response = []
turnaround = []
wait = []

print()

for p in running_queue:
    print(p)
    rt = p["start"] - p["arrival"]
    response.append(rt)
    tt = p["end"] - p["arrival"]
    turnaround.append(tt)
    wt = tt - p["burst"]
    wait.append(wt)
    print(p["name"], "rt:", rt, "tt:", tt, "wt:", wt)

print()

if response:
    print("Average response time:", sum(response) / len(response))
if turnaround:
    print("Average turnaround time:", sum(turnaround) / len(turnaround))
if wait:
    print("Average waiting time:", sum(wait) / len(wait))

if final_queue == control:
    print("\nSuccess:", final_queue)
else:
    print("\nFailure:", final_queue)
