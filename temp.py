processes = [["P1", 1, 3], ["P2", 3, 7], ["P3", 5, 1]]
control = ["--", "P1", "P1", "P2", "P2", "P1", "P3", "P2", "P2", "P2", "P2", "P2"]

active = []
turn_queue = []
wait_queue = []
final_queue = []

current_time = 0

done = False

while not done:
    print("\nTime:", current_time)
    for p in processes:
        if p[1] == current_time:
            turn_queue.append(p)

    print("Turn:", turn_queue)

    if not active:
        if len(turn_queue) > 0:
            active = turn_queue[0]
            turn_queue.pop(0)
        else:
            if len(wait_queue) > 0:
                active = wait_queue[0]

    if not turn_queue and not wait_queue:
        active = ["--", 0, 0]

    if active != [] and active[2] > 0:
        wait_queue.append(active)

    print("Active:", active)

    if len(turn_queue) > 0:
        wait_queue.append(turn_queue[0])

    print("Wait:", wait_queue)

    current_time += 1

    if current_time == 13:
        done = True

if done:
    if final_queue == control:
        print("Success:", final_queue)
    else:
        print("Failure:", final_queue)
