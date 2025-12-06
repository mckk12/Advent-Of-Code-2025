def read_input(file_path):
    numbers = []
    operations = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[:-1]:
            numbers.append(line.strip("\n"))
        operations = lines[-1].strip().split()
    return numbers, operations

def process_correct_numbers(lines, operations):
    current_index = 0
    correct_numbers = [[] for _ in range(len(operations))]
    l = len(lines[0])
    for i in range(l):
        number = ''
        for j in range(len(lines)):
            number += lines[j][i]
        if number.strip() == '':
            current_index += 1
        else:
            correct_numbers[current_index].append(int(number))
    return correct_numbers

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
    lines, operations = read_input("Day-6/input.txt")
    correct_numbers = process_correct_numbers(lines, operations)
    results = eval_problems(correct_numbers, operations)
    res = sum(results)
    print(res)