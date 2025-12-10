import numpy as np
import pulp

def read_input(file_path):
    machines = []
    with open(file_path, 'r') as file:
        for line in file:
            machines.append(line.strip().split())
    return machines

def calculate_buttons_seq(machine):
    buttons, joltage_req = machine[1:-1], machine[-1]
    buttons = [tuple(map(int, button.strip("()").split(","))) for button in buttons]
    joltage_req = list(map(int, joltage_req.strip("{}").split(",")))

    A = np.transpose(np.array([[1 if j in buttons[i] else 0 for j in range(len(joltage_req))] for i in range(len(buttons))]))
    b = np.array(joltage_req)

    prob = pulp.LpProblem("AoC_Day10_Part2", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(buttons))]

    prob += pulp.lpSum(x)

    for j in range(len(b)):
        prob += pulp.lpSum(A[j][i] * x[i] for i in range(len(x))) == b[j]

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    return pulp.value(prob.objective)


def configure_machines(machines):
    results = []
    for machine in machines:
        result = calculate_buttons_seq(machine)
        results.append(result)
    return sum(results)
    


if __name__ == "__main__":
    machines = read_input("Day-10/input.txt")
    total_buttons = configure_machines(machines)
    print(total_buttons) #19574