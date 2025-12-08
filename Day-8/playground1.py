def read_input(file_path):
    boxes_cords = []
    with open(file_path, 'r') as file:
        for line in file:
            boxes_cords.append(list(map(int, line.strip().split(','))))
    return boxes_cords

def calc_dist(box1, box2):
    return (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
    

def connect_closest_boxes(boxes_cords, pairs_amount):
    connections = []
    for i in range(len(boxes_cords)):
        for j in range(i + 1, len(boxes_cords)):
            dist = calc_dist(boxes_cords[i], boxes_cords[j])
            pair = (dist, i, j)
            connections.append(pair)
    connections.sort(key=lambda x: x[0])

    circuits = []
    for conn in connections[:pairs_amount]:
        dist, box1_idx, box2_idx = conn
        box1_in_circuit = any(box1_idx in circuit for circuit in circuits)
        box2_in_circuit = any(box2_idx in circuit for circuit in circuits)
        if not box1_in_circuit and not box2_in_circuit:
            circuits.append({box1_idx, box2_idx})
        elif box1_in_circuit and not box2_in_circuit:
            for circuit in circuits:
                if box1_idx in circuit:
                    circuit.add(box2_idx)
                    break   
        elif not box1_in_circuit and box2_in_circuit:
            for circuit in circuits:
                if box2_idx in circuit:
                    circuit.add(box1_idx)
                    break   
        else:
            circuit1 = circuit2 = None
            for circuit in circuits:
                if box1_idx in circuit:
                    circuit1 = circuit
                if box2_idx in circuit:
                    circuit2 = circuit
                if circuit1 is not None and circuit2 is not None:
                    break
            if circuit1 is circuit2:
                continue
            circuit1.update(circuit2)
            circuits.remove(circuit2)
    return circuits

if __name__ == "__main__":
    boxes_cords = read_input('Day-8/input.txt')
    pairs_amount = 1000
    connections = connect_closest_boxes(boxes_cords, pairs_amount)
    biggest_circuits = sorted(connections, key=lambda x: len(x), reverse=True)[:3]
    result = 1
    for circuit in biggest_circuits:
        result *= len(circuit)
    print("Result:", result)
    


