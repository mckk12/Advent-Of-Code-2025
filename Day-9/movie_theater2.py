def read_input(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split(','))
            points.append((x, y))
    return points

def calculate_area(point1, point2): #from points in matrix
    x1, y1 = point1
    x2, y2 = point2 
    return (abs(x2 - x1)+1) * (abs(y2 - y1)+1)

def is_outside_poly(pair, points):
    (x1, y1), (x2, y2) = pair
    left = min(x1, x2)
    right = max(x1, x2)
    bottom = min(y1, y2)
    top = max(y1, y2)

    away = True
    for i in range(len(points)):
        lx, ly = points[i-1]
        lx2, ly2 = points[i]
        if not (max(lx, lx2) <= left or\
            min(lx, lx2) >= right or\
            max(ly, ly2) <= bottom or\
            min(ly, ly2) >= top):
            away = False
            break
    return not away
    

def find_largest_rect(points):
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pair = (points[i], points[j])
            if not is_outside_poly(pair, points):
                area = calculate_area(pair[0], pair[1])
                max_area = max(max_area, area)

    return max_area

if __name__ == "__main__":
    input_file = 'Day-9/input.txt'
    points = read_input(input_file)
    largest_area = find_largest_rect(points)
    print(f"Largest rectangle area: {largest_area}")