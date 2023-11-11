def possible_entry(x, y, n, grid):
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve_gen(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible_entry(x, y, n, grid):
                        grid[y][x] = n
                        yield from solve_gen(grid)
                        grid[y][x] = 0
                return
    yield tuple(map(tuple, grid))
