def load_ingridients_db(filepath):
    fresh_ing_ranges = []
    with open(filepath, 'r') as file:
        for line in file:
            if ("-" in line.strip()):
                fresh_ing_ranges.append(tuple(map(int, line.strip().split("-"))))
            
    return fresh_ing_ranges

def fresh_ids_amount(fresh_ing_ranges):
    new_ranges = []
    fresh_ing_ranges.sort()
    i=0
    while(i < len(fresh_ing_ranges)):
        current_range = fresh_ing_ranges[i]
        start, end = current_range
        j = i + 1
        while (j < len(fresh_ing_ranges)):
            next_range = fresh_ing_ranges[j]
            next_start, next_end = next_range
            if next_start <= end + 1:
                end = max(end, next_end)
                j += 1
            else:
                break
        new_ranges.append((start, end))
        i = j
        
    return sum(end - start + 1 for start, end in new_ranges)

if __name__ == "__main__":
    fresh_ing_ranges = load_ingridients_db("Day-5/input.txt")
    # print(fresh_ing_ranges)
    res = fresh_ids_amount(fresh_ing_ranges)
    print(f"Fresh ingredient IDs amount: {res}")
