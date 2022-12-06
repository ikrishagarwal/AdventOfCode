from pathlib import Path
file_path = Path(__file__, '..', '..', 'input.txt').resolve()

with open(file_path) as f:
    data = f.read().splitlines()[0]
    memory = []

    for i, letter in enumerate(data):
        if letter in memory:
            del memory[:memory.index(letter)+1]
        memory.append(letter)

        if (len(memory) == 4):
            break

    print(i+1)
