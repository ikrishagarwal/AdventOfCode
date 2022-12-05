from math import floor
from pathlib import Path
file_path = Path(__file__, '..', '..', 'input.txt').resolve()

with open(file_path) as f:
    data = f.read().splitlines()
    stack = {}

    for i, line in enumerate(data):
        if line.replace(' ', '').isdigit():
            break

        for j in range(1, len(line), 4):
            k = j % 4 + floor(j/4)

            if not k in stack:
                stack[k] = []

            if len(line[j].strip()) != 0:
                stack[k].insert(0, line[j])

    for i in range(i + 2, len(data)):
        line = data[i]
        count = int(line[5]) if not line[5].isdigit() else int(line[5:7])

        giver = int(line[13 if count > 9 else 12])
        receiver = int(line[len(line) - 1])

        for j in range(count):
            stack[receiver].append(stack[giver].pop())

    print(''.join(map(lambda x: x[len(x)-1], stack.values())))
