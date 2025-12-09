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

def find_largest_rect(points):
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            area = calculate_area(points[i], points[j])
            if area > max_area:
                max_area = area

    return max_area

if __name__ == "__main__":
    input_file = 'Day-9/input.txt'
    points = read_input(input_file)
    largest_area = find_largest_rect(points)
    print(f"Largest rectangle area: {largest_area}")