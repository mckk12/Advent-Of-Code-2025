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

def count_timelines(start_idx, splitters_idx):
    current_beams = {start_idx: 1}
    for splitters in splitters_idx:
        new_beams = {}
        for splitter in splitters:
            if splitter in current_beams:
                timelines_count = current_beams[splitter]
                del current_beams[splitter]
                left_beam = splitter - 1
                right_beam = splitter + 1
                new_beams[left_beam] = new_beams.get(left_beam, 0) + timelines_count
                new_beams[right_beam] = new_beams.get(right_beam, 0) + timelines_count
        for beam, count in current_beams.items():
            new_beams[beam] = new_beams.get(beam, 0) + count
        current_beams.clear()
        current_beams.update(new_beams)

    total_timelines = sum(current_beams.values())
    return total_timelines

if __name__ == "__main__":
    input_file = 'Day-7/input.txt'
    start_idx, splitters_idx = read_input(input_file)
    result = count_timelines(start_idx, splitters_idx)
    print(result)