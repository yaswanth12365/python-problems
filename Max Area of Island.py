class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        start_nodes = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1] #get indexes of start nodes
        start_nodes = Counter(start_nodes) #make it a Counter
        area = float('-inf')
        while start_nodes:
            start = next(iter(start_nodes))
            area1, visited = self.bfs(grid, start)
            area = max(area, area1)
            for i in visited:
                start_nodes[i] -= 1
            start_nodes = +start_nodes #get rid of all nodes that are visited
        return max(0, area)
    
    def bfs(self, grid, start):
        queue = [start]
        area = 1
        visited = [start]
        while queue:
            x, y = queue.pop(0)
            directions = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
            for a, b in directions:
                if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                    if grid[a][b] == 1 and (a, b) not in visited:
                        queue.append((a, b))
                        visited.append((a, b))
                        area += 1
        return area, visited
