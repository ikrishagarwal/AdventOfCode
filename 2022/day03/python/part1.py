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

    for line in data:
        part1 = line[:round(len(line)/2)]
        part2 = line[round(len(line)/2):]

        for item in part1:
            if item in part2:
                score += getPoints(item)
                break

    print(score)
