from pathlib import Path
file_path = Path(__file__, '..', '..', 'input.txt').resolve()


with open(file_path) as f:
    data = f.read().splitlines()

    visible = len(data[0]) * 2 + len(data) * 2 - 4
    tree_map = [list(map(int, x)) for x in data]

    for i in range(1, len(tree_map) - 1):
        for j in range(1, len(tree_map[i]) - 1):
            tree = tree_map[i][j]
            left_row = tree_map[i][:j]
            right_row = tree_map[i][j + 1:]

            if max(left_row) < tree or max(right_row) < tree:
                visible += 1

            else:
                top_list = []
                bottom_list = []

                for k in range(0, i):
                    top_list.append(tree_map[k][j])

                for k in range(i + 1, len(tree_map)):
                    bottom_list.append(tree_map[k][j])

                if max(top_list) < tree or max(bottom_list) < tree:
                    visible += 1

    print(visible)
