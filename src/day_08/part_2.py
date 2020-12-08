from collections import namedtuple

Command = namedtuple('Command', ['operation', 'argument'])


class Program:
    def __init__(self, data):
        self.lines = Program._parse_program(data)
        self.next_line_index = 0
        self.accumulator = 0
        self.executed_jumps = set()
        self.steps = []

    def reset(self):
        self.next_line_index = 0
        self.accumulator = 0
        self.executed_jumps.clear()
        self.steps.clear()

    def run(self):
        while True:
            if not self.execute_line():
                return False
            if self.next_line_index >= len(self.lines):
                return True

    def execute_line(self):
        current_line = self.lines[self.next_line_index]

        if current_line.operation == 'acc':
            value = int(current_line.argument)
            self.accumulator += value
            self.next_line_index += 1
            self.steps.append('Add {} to acc [{}], go to {}'.format(value, self.accumulator, self.next_line_index))
            return True

        if current_line.operation == 'jmp':
            if self.next_line_index in self.executed_jumps:
                return False
            self.executed_jumps.add(self.next_line_index)
            value = int(current_line.argument)
            self.next_line_index += value
            self.steps.append('Jump of {}, acc [{}], go to {}'.format(value, self.accumulator, self.next_line_index))
            return True

        if current_line.operation == 'nop':
            self.next_line_index += 1
            self.steps.append('Go to {}'.format(self.next_line_index))
            return True

    @staticmethod
    def _parse_program(data):
        lines = []
        for line in data:
            operation, argument = line.split(' ')
            lines.append(Command(operation, argument))
        return lines

    @staticmethod
    def swap_operation(operation):
        operation_swaps = {'jmp': 'nop', 'nop': 'jmp', 'acc': 'acc'}
        return operation_swaps[operation]


def solution(data):
    p = Program(data.split('\n'))
    original_lines = p.lines

    to_swap = []
    for i in range(len(original_lines)):
        line = original_lines[i]
        if line.operation == 'jmp' or line.operation == 'nop':
            to_swap.append(i)

    while not p.run():
        p.reset()
        p.lines = original_lines.copy()
        index_to_swap = to_swap.pop()
        p.lines[index_to_swap] = Command(
            Program.swap_operation(p.lines[index_to_swap].operation), p.lines[index_to_swap].argument
        )

    return p.accumulator
