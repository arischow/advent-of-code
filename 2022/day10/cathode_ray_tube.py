class Program:
    def __init__(self):
        self.cycle = 0
        self.register = 1
        self.records = []
        self.record()

    def execute(self, instruction):
        instruction = instruction.split()
        command, arg = 0, 1
        if instruction[command] == "noop":
            self.cycle += 1
            self.record()
        elif instruction[command] == "addx":
            self._addx(int(instruction[arg]))

    def _addx(self, number):
        for idx, _ in enumerate(range(2)):
            self.cycle += 1
            if idx == 1:
                # print(number)
                self.register += number
            self.record()

    def record(self):
        self.records.append((self.cycle, self.register))

    def signal_strength(self):
        data = self.records[20 - 1 :: 40]  # because it's "during" so minus 1
        return sum([(x[0] + 1) * x[1] for x in data])

    def draw_chunks(self):
        for i in range(1, len(self.records), 40):
            yield self.records[i - 1 : i + 39]

    def draw(self):
        result = []

        for record in self.draw_chunks():
            result.append(self._draw(record))
        return result

    def _draw(self, record):
        result = ""
        crt_position = 0

        for cycle, register in record:
            # print(cycle, register)
            if crt_position in range(register - 1, register + 2):
                result += "#"
            else:
                result += "."
            crt_position += 1
        return result


if __name__ == "__main__":
    program = Program()
    f = open("cathode_ray_tube.txt")
    for line in f:
        line = line.strip()
        program.execute(line)
    f.close()
    print(program.signal_strength())
    print("\n".join(program.draw()))
