from pathlib import Path
file_path = Path(__file__, '..', '..', 'input.txt').resolve()

with open(file_path) as f:
    data = f.read().splitlines()

    overlaps = 0

    for line in data:
        elf1 = list(map(int, line.split(',')[0].split('-')))
        elf2 = list(map(int, line.split(',')[1].split('-')))

        if elf2[1] >= elf1[0] >= elf2[0] or elf2[0] <= elf1[1] <= elf2[1]:
            overlaps += 1
            print(line)

        elif elf1[0] <= elf2[0] <= elf2[1] and elf1[1] >= elf2[1] >= elf1[0]:
            overlaps += 1
            print(line)

    print(overlaps)
