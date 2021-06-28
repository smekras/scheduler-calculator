import utils


class RoundRobin:

    def __init__(self, start, processes):
        self.quantum = 2
        self.current_time = start
        self.processes = processes
        self.active = ""
        self.process_queue = []
        self.wait_queue = []
        self.final_queue = []
        self.done = 0

    def turn_handler(self):
        print("Starting Round Robin algorithm\n")

        if self.done == 0:
            for p in self.processes:
                self.process_queue.append(p)

        while not self.done:
            print("\nTime:", self.current_time)

            temp_queue = []

            if len(self.process_queue) > 0:
                if self.process_queue[0].arrival == self.current_time:
                    temp_queue.append(self.process_queue[0])
                    self.process_queue.pop(0)
            if len(temp_queue) > 0:
                print("Temp:", temp_queue[0].name)

            if self.active == "":
                print("Active: None")
                if len(temp_queue) > 0:
                    self.active = temp_queue[0]
                    temp_queue.pop(0)
                else:
                    if len(self.wait_queue) > 0:
                        self.active = self.wait_queue[0]
                        self.wait_queue.pop(0)
            else:
                print("Active:", end=" ")
                self.active.print_info()

            if self.active != "":
                if self.active.start == "Unset":
                    self.active.start = self.current_time
                else:
                    self.active.last = self.current_time
                self.final_queue.append(self.active)

            if self.active != "":
                if self.active.remain > 0:
                    self.active.remain -= 1

                if self.active.remain == 0 or self.active.last == self.current_time - self.quantum:
                    self.active.empty += 1
                    self.active.segments += 1
                    self.wait_queue.append(self.active)
                    self.active = ""

            print("Wait Queue:", end=" ")
            utils.print_array_names(self.wait_queue)
            print("\n", end="")

            print("Process Queue:", end=" ")
            utils.print_array_names(self.process_queue)
            print("\n", end="")

            self.check_done()

    def check_done(self):
        if self.active != "" and self.active != []:
            self.active.print_info()
            remaining = self.active.remain
        else:
            remaining = 0

        for p in self.process_queue:
            remaining += p.remain

        print("Total remaining:", remaining)

        if remaining == 0 or self.current_time == 20:
            self.done = 1
        self.current_time += 1

    # def load_process(self, process):
    #     if process.arrival == self.current_time:
    #         self.load_to_wait(process)
    #
    # def load_to_active(self, process):
    #     if self.active == "---" or "":
    #         self.active = process.name
    #         self.calculate_start(process)
    #         print(self.wait_queue)
    #         self.wait_queue.pop(0)
    #         print(self.wait_queue)

    # def calculate_start(self, process):
    #     if 0 < process.remain <= self.quantum:
    #         process.last = self.current_time
    #     else:
    #         process.start = self.current_time
    #
    # def calculate_turnaround(self, process):
    #     process.turnaround = process.end - process.arrival
    #
    # def calculate_wait(self, process):
    #     # way 1
    #     wait1 = process.turnaround - process.burst
    #     # way 2
    #     wait2 = process.last - process.arrival - (process.empty * self.quantum)
    #     if wait1 == wait2:
    #         process.wait = wait1
    #     else:
    #         process.wait = "error"
    #
    # def suspend_process(self, process):
    #     if process.start == self.current_time - 2 and process.remain > 0:
    #         if process.remain <= 2:
    #             process.remain = 0
    #         else:
    #             process.remain += -2
    #         process.empty += 1
    #         process.segments += 1
    #         self.final_queue.append(self.active)
    #         self.load_to_wait(process)

    # def update_processes(self):
    #     for key in self.processes:
    #         print("*", key, self.processes[key])
    #         self.calculate_start(self.processes[key])
    #         self.calculate_turnaround(self.processes[key])
    #         self.calculate_wait(self.processes[key])
    #         print("-", key, self.processes[key])
