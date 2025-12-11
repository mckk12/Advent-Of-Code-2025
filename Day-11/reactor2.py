from functools import cache


def read_input(file_path):
    devices = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            device_id = parts[0].rstrip(':')
            outputs = parts[1:]
            devices[device_id] = outputs
    return devices

devices = {}

@cache
def find_paths(current_device="svr", end_device="out"):
    if current_device == end_device:
        return 1
    paths = 0
    for neighbor in devices.get(current_device, []):
        paths += find_paths( neighbor, end_device)
    return paths

def find_waypoints_paths():
    paths = find_paths( current_device="svr", end_device="fft") * \
            find_paths( current_device="fft", end_device="dac") * \
            find_paths( current_device="dac", end_device="out")
    paths += find_paths( current_device="svr", end_device="dac")* \
            find_paths( current_device="dac", end_device="fft") * \
            find_paths( current_device="fft", end_device="out")
    return paths

if __name__ == "__main__":
    input_file = 'Day-11/input.txt'
    devices = read_input(input_file)
    total_paths = find_waypoints_paths()
    print(f"Total distinct paths: {total_paths}")