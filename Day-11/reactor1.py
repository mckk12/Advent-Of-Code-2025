


def read_input(file_path):
    devices = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            device_id = parts[0].rstrip(':')
            outputs = parts[1:]
            devices[device_id] = outputs
    return devices

def find_paths(devices):
    paths = 0
    start_device = "you"
    end_device = "out"
    stack = [(start_device, {start_device})]

    while stack:
        current_device, visited = stack.pop()
        if current_device == end_device:
            paths += 1
            continue
        for neighbor in devices.get(current_device, []):
            if neighbor not in visited:
                stack.append((neighbor, visited | {neighbor}))
    return paths


if __name__ == "__main__":
    input_file = 'Day-11/input.txt'
    devices = read_input(input_file)
    total_paths = find_paths(devices)
    print(f"Total distinct paths from 'you' to 'out': {total_paths}")