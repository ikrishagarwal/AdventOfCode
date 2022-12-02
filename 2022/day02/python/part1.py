from pathlib import Path
file_path = Path(__file__, '..', '..', 'input.txt').resolve()

with open(file_path) as f:
    data = f.read().splitlines()

    score = 0

    score_board = {
        "A": {
            "X": 4,
            "Y": 8,
            "Z": 3
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9
        },
        "C": {
            "X": 7,
            "Y": 2,
            "Z": 6
        }
    }

    for line in data:
        opponent, player = line.split(' ')
        score += score_board[opponent][player]

    print(score)
