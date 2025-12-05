def load_ingridients_db(filepath):
    fresh_ing_ranges = []
    available_ings = []
    with open(filepath, 'r') as file:
        for line in file:
            if ("-" in line.strip()):
                fresh_ing_ranges.append(tuple(map(int, line.strip().split("-"))))
            elif (line.strip().isdigit()):
                available_ings.append(int(line.strip()))
            
    return fresh_ing_ranges, available_ings

def fresh_amount(fresh_ing_ranges, available_ings):
    fresh_count = 0
    for ing in available_ings:
        for r in fresh_ing_ranges:
            if r[0] <= ing <= r[1]:
                fresh_count += 1
                break
    return fresh_count

if __name__ == "__main__":
    fresh_ing_ranges, available_ings = load_ingridients_db("Day-5/input.txt")
    res = fresh_amount(fresh_ing_ranges, available_ings)
    print(f"Fresh ingredients available: {res}")
