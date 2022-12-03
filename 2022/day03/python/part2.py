from pathlib import Path
file_path = Path(__file__, '..', '..', 'input.txt').resolve()


def getPoints(letter):
    point = ord(letter)
    if point < 91:
        return point - 64 + 26
    else:
        return point - 96


score = 0

with open(file_path) as f:
    data = f.read().splitlines()

    for i in range(0, len(data), 3):
        elf1 = data[i]
        elf2 = data[i+1]
        elf3 = data[i+2]

        for item in elf1:
            if item in elf2 and item in elf3:
                score += getPoints(item)
                break

    print(score)
