import timeit

GRID_LEN = 20

def grid_builder(i):
    GRID = []
    def constructor(i):
        
        if i < 1:
            GRID.insert(0, [i + GRID_LEN, 1])
            return GRID
        if i == GRID_LEN ** 2 - 1:
            GRID.insert(0, i)
        else:
            if i + GRID_LEN > GRID_LEN ** 2 -1:
                GRID.insert(0, i + 1)
            elif (i + 1) % GRID_LEN == 0:
                GRID.insert(0, i + GRID_LEN)
            else:
                GRID.insert(0, [i + 1, i + GRID_LEN])
            
        return constructor(i - 1)
    return constructor(i - 1)

def calc_paths(grid):
    def dfs(path):
        if type(path) is int:
            if path == GRID_LEN ** 2 - 1:
                return 1
            return dfs(grid[path])
        return dfs(path[0]) + dfs(path[1])
        
    return dfs(grid[0])
        

print(timeit.timeit('print(calc_paths(grid_builder(GRID_LEN ** 2)))', globals=globals(), number=1))

