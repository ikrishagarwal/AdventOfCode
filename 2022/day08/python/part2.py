from pathlib import Path
from math import prod
file_path = Path(__file__, '..', '..', 'input.txt').resolve()


with open(file_path) as f:
    data = f.read().splitlines()

    score_list = []
    tree_map = [list(map(int, x)) for x in data]

    for i in range(1, len(tree_map) - 1):
        for j in range(1, len(tree_map[i]) - 1):
            tree = tree_map[i][j]
            scores = [0, 0, 0, 0]

            for k in range(i - 1, -1, -1):
                scores[0] += 1
                if tree_map[k][j] >= tree:
                    break

            for k in range(i + 1, len(tree_map)):
                scores[1] += 1
                if tree_map[k][j] >= tree:
                    break

            for k in tree_map[i][:j][::-1]:
                scores[2] += 1
                if k >= tree:
                    break

            for k in tree_map[i][j + 1:]:
                scores[3] += 1
                if k >= tree:
                    break

            score_list.append(prod(scores))

    print(max(score_list))
