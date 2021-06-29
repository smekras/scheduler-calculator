# processes = {0: {"name": "P1", "arrival": 1, "burst": 3, "start": 0, "last": 0},
#              1: {"name": "P2", "arrival": 3, "burst": 7, "start": 0, "last": 0},
#              2: {"name": "P3", "arrival": 5, "burst": 1, "start": 0, "last": 0}}
processes = [["P1", 1, 3, 0, 0], ["P2", 3, 7, 0, 0], ["P3", 5, 1, 0, 0]]
control = ["--", "P1", "P1", "P2", "P2", "P1", "P3", "P2", "P2", "P2", "P2", "P2"]

active = []
running_queue = []
wait_queue = processes

final_queue = []

current_time = 0
quantum = 2

done = False

while not done:
    print("\nTime:", current_time)

    if running_queue:
        if running_queue[0][4] == current_time - quantum:
            wait_queue.insert(0, running_queue[0])
            running_queue.pop(0)

    if wait_queue:
        print("Wait:", wait_queue)
        print("Running:", running_queue)
        if wait_queue[0][1] == current_time:
            running_queue.insert(0, wait_queue[0])
            running_queue[0][4] = current_time
            wait_queue.pop(0)
        print("Wait:", wait_queue)
        print("Running:", running_queue)

    # for p in processes:
    #     if p[1] == current_time:
    #         turn_queue.append(p)
    #         print("Turn:", turn_queue[0][0])
    #
    # if not active or active[0] == "--":
    #     print("Active: None")
    #     if turn_queue:
    #         active = turn_queue[0]
    #         print("Active:", active[0])
    #         turn_queue = []
    # else:
    #     print("Active:", active[0])
    #
    # if active:
    #     if active[4] > current_time - quantum:
    #         wait_queue.append(active)
    #         active = ["--", 0, 0, 0, 0]
    #     else:
    #         if turn_queue:
    #             wait_queue.append(turn_queue[0])
    #             turn_queue = []

    if current_time == 13:
        done = True
    else:
        current_time += 1

if done:
    print("\n")
    if final_queue == control:
        print("Success:", final_queue)
    else:
        print("Failure:", final_queue)
