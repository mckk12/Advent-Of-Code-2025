def read_input(filepath):
    shapes = {}
    regions = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if "x" in line:
                line = line.split(":")
                units = tuple(map(int, line[0].strip().split("x")))
                regions.append((units, line[1].strip().split()))
                i += 1
            else:
                shapes[line.strip(":")] = [l.strip() for l in lines[i+1:i+4]]
                i += 5
    return shapes, regions

# def flip(shape):
#     return [row[::-1] for row in shape]

# def rotate(shape):
#     return [''.join(row[i] for row in reversed(shape)) for i in range(len(shape[0]))]

def check_fit(shapes, region):
    grid_units = region[0][0] * region[0][1]
    shape_amounts = region[1]
    shapes_units = 0
    full_shapes_units = 0
    for i in range(len(shape_amounts)):
        shape_id = str(i)
        shape = shapes[shape_id]
        shape_units = sum(row.count("#") for row in shape)
        shapes_units += shape_units * int(shape_amounts[i])
        full_shape = len(shape) * len(shape[0])
        full_shapes_units += full_shape * int(shape_amounts[i])
    
    return shapes_units <= grid_units and full_shapes_units <= grid_units


if __name__ == "__main__":
    shapes, regions = read_input("Day-12/input.txt")
    count_fits = 0
    for region in regions:
        if check_fit(shapes, region):
            count_fits += 1
    print(count_fits)

