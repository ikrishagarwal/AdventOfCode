from pathlib import Path
file_path = Path(__file__, '..', '..', 'input.txt').resolve()


def checkAdjacent(head, tail):
    if tail[1] == head[1] and tail[0] in [head[0] - 1, head[0], head[0] + 1]:
        return True
    if tail[0] == head[0] and tail[1] in [head[1] - 1, head[1], head[1] + 1]:
        return True
    return False


def isDiagonal(head, tail):
    if head[0] == tail[0] or head[1] == tail[1]:
        return False
    return True


def moveDiagonal(head, tail):
    tailX, tailY = tail
    headX, headY = head

    if tailX - 2 == headX and tailY + 1 == headY:
        tail = (tailX - 1, tailY + 1)
    elif tailX + 2 == headX and tailY + 1 == headY:
        tail = (tailX + 1, tailY + 1)
    elif tailX - 2 == headX and tailY - 1 == headY:
        tail = (tailX - 1, tailY - 1)
    elif tailX + 2 == headX and tailY - 1 == headY:
        tail = (tailX + 1, tailY - 1)

    elif tailX - 1 == headX and tailY + 2 == headY:
        tail = (tailX - 1, tailY + 1)
    elif tailX + 1 == headX and tailY + 2 == headY:
        tail = (tailX + 1, tailY + 1)
    elif tailX - 1 == headX and tailY - 2 == headY:
        tail = (tailX - 1, tailY - 1)
    elif tailX + 1 == headX and tailY - 2 == headY:
        tail = (tailX + 1, tailY - 1)
    return tail


with open(file_path, 'r') as f:
    data = f.read().splitlines()

    head = (0, 0)
    tail = (0, 0)
    visited = set([(0, 0)])

    for line in data:
        direction, steps = line.split(' ')

        for i in range(int(steps)):
            if direction == 'R':
                head = (head[0] + 1, head[1])
                if not checkAdjacent(head, tail):
                    if isDiagonal(head, tail):
                        tail = moveDiagonal(head, tail)
                    else:
                        tail = (tail[0] + 1, tail[1])

            elif direction == 'L':
                head = (head[0] - 1, head[1])
                if not checkAdjacent(head, tail):
                    if isDiagonal(head, tail):
                        tail = moveDiagonal(head, tail)
                    else:
                        tail = (tail[0] - 1, tail[1])

            elif direction == 'U':
                head = (head[0], head[1] + 1)
                if not checkAdjacent(head, tail):
                    if isDiagonal(head, tail):
                        tail = moveDiagonal(head, tail)
                    else:
                        tail = (tail[0], tail[1] + 1)

            elif direction == 'D':
                head = (head[0], head[1] - 1)
                if not checkAdjacent(head, tail):
                    if isDiagonal(head, tail):
                        tail = moveDiagonal(head, tail)
                    else:
                        tail = (tail[0], tail[1] - 1)

            visited.add(tail)

    print(len(visited))
