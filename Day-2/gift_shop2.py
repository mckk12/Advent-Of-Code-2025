def get_id_ranges(filepath):
    id_ranges = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            for part in parts:
                start, end = map(int, part.split('-'))
                id_ranges.append((start, end))
    return id_ranges

def add_invalid_ids(id_ranges):
    s = 0
    for start, end in id_ranges:
        for id_num in range(start, end + 1):
            id_str = str(id_num)
            l = len(id_str)
            m = l//2
            for i in range(1, m + 1):
                new_str = id_str[:i] * (l//i)
                if new_str == id_str:
                    s += id_num
                    break
    return s

if __name__ == "__main__":
    id_ranges = get_id_ranges("Day-2/input.txt")
    s = add_invalid_ids(id_ranges)
    print(f"Sum: {s}")
