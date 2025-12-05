def get_batteries_banks(filepath):
    batteries_banks = []
    with open(filepath, 'r') as file:
        for line in file:
            batteries_banks.append(line.strip())           
    return batteries_banks

def highest_joltage_bank(bank):
    number = ""
    idx = 0
    for i in range(12):
        safeindex = len(bank)-(11-i)
        high = max(bank[:safeindex])
        number += high
        idx = bank.index(high)
        bank = bank[idx+1:]
    return number

def calc_sum_jolatages(batteries_banks):
    s = 0
    for bank in batteries_banks:
        highest = highest_joltage_bank(bank)
        s += int(highest)
    return s

if __name__ == "__main__":
    batteries_banks = get_batteries_banks("Day-3/input.txt")
    s = calc_sum_jolatages(batteries_banks)
    print(f"Sum: {s}")