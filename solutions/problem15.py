import timeit
GRID_LEN = 20

def grid_builder(i):
    GRID = []
    def constructor(i):
        
        if i < 1:
            GRID.insert(0, [i + (GRID_LEN + 1), 1])
            return GRID
        if i == (GRID_LEN + 1) ** 2 - 1:
            GRID.insert(0, 0)
        else:
            if i + (GRID_LEN + 1) > (GRID_LEN + 1) ** 2 -1:
                GRID.insert(0, i + 1)
            elif (i + 1) % (GRID_LEN + 1) == 0:
                GRID.insert(0, i + (GRID_LEN + 1))
            else:
                GRID.insert(0, [i + 1, i + (GRID_LEN + 1)])
            
        return constructor(i - 1)
    return constructor(i - 1)

def calc_paths(grid):
    def dfs(path):
        if type(path) is int:
            if path == 0:
                return 1
            return dfs(grid[path])
        return dfs(path[0]) + dfs(path[1])
        
    return dfs(grid[0])

"""
    Answer: 137846528820
    Time Taken: 28.882 Hours
"""        

# print(timeit.timeit('print(calc_paths(grid_builder((GRID_LEN + 1) ** 2)))', globals=globals(), number=1))

def count_routes(m, n):
    if n == 0 or m == 0:
        return 1
    return count_routes(m, n - 1) + count_routes(m - 1, n)

print(count_routes(20, 20))