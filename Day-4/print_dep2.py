PAPER_ROLL = "@"

def get_paper_grid(filepath):
    paper_grid = []
    with open(filepath, 'r') as file:
        for line in file:
            paper_grid.append(list(line.strip()))
    return paper_grid

def calc_rolls_around(paper_grid):
    rows = len(paper_grid)
    cols = len(paper_grid[0])

    rolls_around = [[-1 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if paper_grid[i][j] == PAPER_ROLL:
                rolls_around[i][j] = 0
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        if paper_grid[x][y] == PAPER_ROLL and (x, y) != (i, j):
                            rolls_around[i][j] += 1
    return rolls_around

def rolls_to_access(paper_grid, max_around):
    rolls_around = calc_rolls_around(paper_grid)
    # print(rolls_around)
    s = 0
    for row in rolls_around:
        for count in row:
            if count < max_around and count > -1:
                s+=1
    return s

def removing_rolls(paper_grid, max_around):
    rows = len(paper_grid)
    cols = len(paper_grid[0])
    rolls_around = calc_rolls_around(paper_grid)
    rta = rolls_to_access(paper_grid, max_around)
    s = rta
    while rta > 0:
        for i in range(rows):
            for j in range(cols):
                if rolls_around[i][j] < max_around:
                    paper_grid[i][j] = "."
        rolls_around = calc_rolls_around(paper_grid)
        rta = rolls_to_access(paper_grid, max_around)
        s += rta
    return s


if __name__ == "__main__":
    paper_grid = get_paper_grid("Day-4/input.txt")
    res = removing_rolls(paper_grid, 4)
    print(f"Accessible rolls: {res}")