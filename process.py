class Process:
    def __init__(self, name="", arrival=0, burst=0):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.start = "Unset"
        self.last = 0
        self.end = 0
        self.remain = burst
        self.wait = 0
        self.turnaround = 0
        self.empty = 0
        self.segments = 1

    def print_info(self):
        print("Name:", self.name, "arrival:", self.arrival, "burst:", self.burst, "start:", self.start,
              "last:", self.last, "end:", self.end, "remain:", self.remain, "wait:", self.wait,
              "turnaround:", self.turnaround, "empty:", self.empty, "segments:", self.segments)
