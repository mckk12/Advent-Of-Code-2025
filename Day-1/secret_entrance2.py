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
        zeros_pointed += steps // (DIAL_MAX+1)
        steps = steps % (DIAL_MAX+1)
        if direction == 'L':
            if steps >= position and position != 0:
                zeros_pointed += 1
            position = turn_left(position, steps)
        elif direction == 'R':
            if steps > (DIAL_MAX - position) and position != 0:
                zeros_pointed += 1
            position = turn_right(position, steps)
    return zeros_pointed

if __name__ == "__main__":
    sequence = get_sequence("Day-1/input.txt")
    password = find_password(sequence)
    print(f"Password: {password}")
