# processes = {0: {"name": "P1", "arrival": 1, "burst": 3, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
#              1: {"name": "P2", "arrival": 3, "burst": 7, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
#              2: {"name": "P3", "arrival": 5, "burst": 1, "start": "Unset", "last": 0, "end": "Unset", "segments": 1}}
# processes = [["P1", 1, 3, "Unset", 0], ["P2", 3, 7, "Unset", 0], ["P3", 5, 1, "Unset", 0]]
processes = [{"name": "P1", "arrival": 1, "burst": 3, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
             {"name": "P2", "arrival": 3, "burst": 7, "start": "Unset", "last": 0, "end": "Unset", "segments": 1},
             {"name": "P3", "arrival": 5, "burst": 1, "start": "Unset", "last": 0, "end": "Unset", "segments": 1}]
control = ["--", "P1", "P1", "P2", "P2", "P1", "P3", "P2", "P2", "P2", "P2", "P2"]

active = []
running_queue = []
wait_queue = processes

final_queue = []

current_time = 0
quantum = 2

done = False


def load_running():
    running_queue.insert(0, wait_queue[0])
    if running_queue[0]["start"] == "Unset":
        running_queue[0]["start"] = current_time
    running_queue[0]["last"] = current_time


def print_dict_array(array):
    for _ in array:
        print(_["name"], end="")
        print(":", end=" ")
        print(_["burst"], end=", ")


while not done:
    print("\nTime:", current_time)
    print("Wait:", end=" ")
    print_dict_array(wait_queue)
    print("\nRunning:", end=" ")
    print_dict_array(running_queue)
    print("\n")

    if wait_queue and wait_queue[0]["burst"] == 0:
        wait_queue.pop(0)

    if wait_queue:
        if wait_queue[0]["arrival"] == current_time and not running_queue:
            load_running()
            wait_queue.pop(0)

    if running_queue and running_queue[0]["last"] == current_time - quantum:
        temp = running_queue[0]
        running_queue.pop(0)
        load_running()
        if temp["burst"] != 0:
            wait_queue.insert(0, temp)

    if running_queue and running_queue[0]["burst"] > 0:
        running_queue[0]["burst"] -= 1

    if running_queue and running_queue[0]["burst"] == 0:
        running_queue[0]["end"] = current_time
        running_queue.pop(0)

    if not running_queue:
        final_queue.append("--")
    else:
        final_queue.append(running_queue[0]["name"])

    print("Wait:", end=" ")
    print_dict_array(wait_queue)
    print("\nRunning:", end=" ")
    print_dict_array(running_queue)
    print("\n")

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
