from collections import deque

def read_input(file_path):
    machines = []
    with open(file_path, 'r') as file:
        for line in file:
            machines.append(line.strip().split())
    return machines

def calculate_buttons_seq(machine):
    lights, buttons = machine[0], machine[1:-1]
    buttons = [list(map(int, button.strip("()").split(","))) for button in buttons]
    lights = list(map(lambda x: 0 if x=="." else 1, lights.strip("[]")))

    start = tuple(lights)
    target = tuple(0 for _ in lights)

    if start == target:
        return []

    queue = deque()
    queue.append((start, []))
    visited = {start}

    while queue:
        state, path = queue.popleft()
        for button in buttons:
            next_state = list(state)
            for idx in button:
                next_state[idx] = 1 - next_state[idx]
            next_state = tuple(next_state)
            if next_state in visited:
                continue
            next_path = path + [button]
            if next_state == target:
                return next_path
            visited.add(next_state)
            queue.append((next_state, next_path))

    return None

def configure_machines(machines):
    results = []
    for machine in machines:
        result = calculate_buttons_seq(machine)
        results.append(len(result))
    return sum(results)
    


if __name__ == "__main__":
    machines = read_input("Day-10/input.txt")
    total_buttons = configure_machines(machines)
    print(total_buttons)