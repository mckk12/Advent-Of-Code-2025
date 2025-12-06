def read_input(file_path):
    numbers = []
    operations = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split()
            for i in range(len(line)):
                if len(numbers) <= i:
                    numbers.append([])
                if line[i].isdigit():
                    numbers[i].append(int(line[i]))
                else:
                    operations.append(line[i])
    return numbers, operations

def eval_problems(numbers, operations):
    results = []
    for i in range(len(operations)):
        if operations[i] == '+':
            result = sum(numbers[i])
        elif operations[i] == '*':
            result = 1
            for num in numbers[i]:
                result *= num
        else:
            result = None
        results.append(result)
    return results


if __name__ == "__main__":
    numbers, operations = read_input("Day-6/input.txt")
    problems_results = eval_problems(numbers, operations)
    res = sum(problems_results)
    print(res) 