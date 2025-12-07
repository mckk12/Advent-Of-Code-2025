def read_input(file_path):
    splitters_idx = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            curr_splitter_idx = []
            for idx, char in enumerate(line):
                if char == 'S':
                    start_idx = idx
                if char == '^':
                    curr_splitter_idx.append(idx)
            if curr_splitter_idx:
                splitters_idx.append(curr_splitter_idx)
    return start_idx, splitters_idx

def count_splits(start_idx, splitters_idx):
    splits = 0
    current_beams = set()
    current_beams.add(start_idx)
    for splitters in splitters_idx:
        for splitter in splitters:
            if splitter in current_beams:
                current_beams.remove(splitter)
                current_beams.add(splitter - 1)
                current_beams.add(splitter + 1)
                splits += 1

    return splits

if __name__ == "__main__":
    input_file = 'Day-7/input.txt'
    start_idx, splitters_idx = read_input(input_file)
    result = count_splits(start_idx, splitters_idx)
    print(result)