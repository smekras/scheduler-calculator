import robin
import utils
from process import Process

# processes = [Process("P1", 1, 3), Process("P2", 3, 7), Process("P3", 5, 1),
#              Process("P4", 11, 5), Process("P5", 13, 2)]
processes = [Process("P1", 1, 3), Process("P2", 3, 7)]

if __name__ == '__main__':
    start = 0
    rr = robin.RoundRobin(start, processes)
    rr.turn_handler()

    turnaround_array = []
    wait_array = []

    print("\nWait queue:", end=" ")
    utils.print_array_names(rr.wait_queue)
    print("\nGantt queue:", end=" ")
    utils.print_array_names(rr.final_queue)
    print("\n")

    # for p in rr.final_queue:
    #     turnaround_array.append(p.turnaround)
    #     wait_array.append(p.wait)
    # print("Average turnaround time:", utils.average(turnaround_array))
    # print("Average wait time:", utils.average(wait_array))
