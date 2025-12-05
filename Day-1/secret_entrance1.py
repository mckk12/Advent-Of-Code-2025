DIAL_MAX = 99
DIAL_START = 50


def turn_left(position, steps):
    return (position - steps) % (DIAL_MAX + 1)

def turn_right(position, steps):
    return (position + steps) % (DIAL_MAX + 1)

def get_sequence(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [[line[0], int(line[1:])] for line in lines]

def find_password(sequence):
    zeros_pointed = 0
    position = DIAL_START
    for direction, steps in sequence:
        if direction == 'L':
            position = turn_left(position, steps)
        elif direction == 'R':
            position = turn_right(position, steps)
        if position == 0:
            zeros_pointed += 1
    return zeros_pointed

if __name__ == "__main__":
    sequence = get_sequence("Day-1/input.txt")
    password = find_password(sequence)
    print(f"Password: {password}")
