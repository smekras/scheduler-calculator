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
            else:
                print("Temp: None")

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
                if len(temp_queue) > 0:
                    self.wait_queue.append(temp_queue[0])

            if self.active != "":
                if self.active.start == "Unset":
                    self.active.start = self.current_time
                    self.active.last = self.active.start
                else:
                    self.active.last = self.current_time
                self.final_queue.append(self.active)

            if self.active != "":
                if self.active.remain > 0:
                    self.active.remain -= 1

                if self.active.remain == 0 or self.active.last == self.current_time - self.quantum:
                    print("Time out for", self.active.name)
                    self.active.empty += 1
                    self.active.segments += 1
                    self.wait_queue.append(self.active)
                    self.active = self.wait_queue[0]

            print("Wait Queue:", end=" ")
            utils.print_array_names(self.wait_queue)
            print("\n", end="")

            print("Process Queue:", end=" ")
            utils.print_array_names(self.process_queue)
            print("\n", end="")

            self.check_done()

    def check_done(self):
        if self.active != "" and self.active != []:
            remaining = self.active.remain
        else:
            remaining = 0

        for p in self.process_queue:
            remaining += p.remain

        if self.active != "":
            print("Active:", end=" ")
            self.active.print_info()
        else:
            print("Active: None")
        print("Total remaining:", remaining)

        if remaining == 0 or self.current_time == 20:
            self.done = 1
        self.current_time += 1
