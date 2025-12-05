def get_batteries_banks(filepath):
    batteries_banks = []
    with open(filepath, 'r') as file:
        for line in file:
            batteries_banks.append(line.strip())           
    return batteries_banks

def highest_joltage_bank(bank):
    highest = [0,0]
    for i in range(len(bank)):
        joltage = int(bank[i])
        if joltage > highest[1]:
            if joltage > highest[0] and i != len(bank) - 1:
                highest[1] = 0
                highest[0] = joltage
                continue
            highest[1] = joltage
    return highest

def calc_sum_jolatages(batteries_banks):
    s = 0
    for bank in batteries_banks:
        highest = highest_joltage_bank(bank)
        s += highest[0] * 10 + highest[1]
    return s

if __name__ == "__main__":
    batteries_banks = get_batteries_banks("Day-3/input.txt")
    s = calc_sum_jolatages(batteries_banks)
    print(f"Sum: {s}")