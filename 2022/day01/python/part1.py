from pathlib import Path
file_path = Path(__file__, '..', '..', 'input.txt').resolve()

with open(file_path) as f:
    data = f.read().splitlines()

    cal = []
    current = 0
    for i in data:
        if i != '':
            current += int(i)
        else:
            cal.append(current)
            current = 0

    highest = max(cal)
    print(highest)
