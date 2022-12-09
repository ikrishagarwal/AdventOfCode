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

    elif tailX - 2 == headX and tailY - 2 == headY:
        tail = (tailX - 1, tailY - 1)
    elif tailX + 2 == headX and tailY + 2 == headY:
        tail = (tailX + 1, tailY + 1)
    elif tailX - 2 == headX and tailY + 2 == headY:
        tail = (tailX - 1, tailY + 1)
    elif tailX + 2 == headX and tailY - 2 == headY:
        tail = (tailX + 1, tailY - 1)

    return tail


def moveRope(head, tail):
    if not checkAdjacent(head, tail):
        if isDiagonal(head, tail):
            tail = moveDiagonal(head, tail)
        else:
            headX, headY = head
            tailX, tailY = tail

            if tailX == headX:
                if tailY - 2 == headY:
                    tail = (tailX, tailY - 1)
                elif tailY + 2 == headY:
                    tail = (tailX, tailY + 1)
            elif tailY == headY:
                if tailX - 2 == headX:
                    tail = (tailX - 1, tailY)
                elif tailX + 2 == headX:
                    tail = (tailX + 1, tailY)
    return tail


with open(file_path, 'r') as f:
    data = f.read().splitlines()

    rope = [(0, 0) for _ in range(10)]
    visited = set([(0, 0)])

    for line in data:
        direction, steps = line.split(' ')

        for i in range(int(steps)):
            if direction == 'R':
                rope[0] = (rope[0][0] + 1, rope[0][1])
            elif direction == 'L':
                rope[0] = (rope[0][0] - 1, rope[0][1])
            elif direction == 'U':
                rope[0] = (rope[0][0], rope[0][1] + 1)
            elif direction == 'D':
                rope[0] = (rope[0][0], rope[0][1] - 1)

            for j in range(9):
                tail = moveRope(rope[j], rope[j+1])
                rope[j+1] = tail

            visited.add(rope[-1])

    print(len(visited))
