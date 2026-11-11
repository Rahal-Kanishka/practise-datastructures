
def dfs(self, grid, i,j, visited=None):
    # if j-1, i-1, j+1, i+1 tries to goes out of the boarder
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0
    # print(f"inside dfs i: {i}, j: {j}")
    # check already visited
    if visited[i][j] == True:
        return 0
    # print('veisited in dfs: ', visited)
    visited[i][j] = True
    # when ever found water stop. but warter border will be marked
    if grid[i][j] == "0":
        return 0 
    # travers to neighbours and only mark them
    self.dfs(grid, i, j+1, visited)
    self.dfs(grid, i+1, j, visited)
    self.dfs(grid, i, j-1, visited)
    self.dfs(grid, i-1, j, visited)
    return 1


def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    i = 0
    j = 0
    n = len(grid)
    m = len(grid[0])
    
    visited = [[False] * m for _ in range(n)]  
    # print(f"n: {n}, m: {m}") 
    # print('visited created: ', visited)
    while( i >= 0 and i < n):
        j = 0
        while( j >= 0 and j< m):
            count += self.dfs(grid, i, j, visited)
            # print(f"i: {i} j: {j}, visited: {visited[i][j]}, count: {count}")
            j+=1
        i+=1
    # print('visits done: ', visited)
    return count
    