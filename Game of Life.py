def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        flag = [[0 for _ in range(m)] for _ in range(n)]
        d = {0:1, 1:0}
        
        def get_neigh(i,j):
            neigh = []
            if i+1 > 0 and i+1 < n:
                if j+1 > 0 and j+1 < m:
                    if flag[i+1][j+1] == 0:
                        neigh.append(board[i+1][j+1])
                    else:
                        neigh.append(d[board[i+1][j+1]])
                        
                if flag[i+1][j] == 0:
                    neigh.append(board[i+1][j])
                else:
                    neigh.append(d[board[i+1][j]])
                    
                if j-1 >= 0 and j-1 < m:
                    if flag[i+1][j-1] == 0:
                        neigh.append(board[i+1][j-1])
                    else:
                        neigh.append(d[board[i+1][j-1]])
                        
            if i-1 >= 0 and i-1 < n:
                if j+1 > 0 and j+1 < m:
                    if flag[i-1][j+1] == 0:
                        neigh.append(board[i-1][j+1])
                    else:
                        neigh.append(d[board[i-1][j+1]])
                        
                if flag[i-1][j] == 0:
                    neigh.append(board[i-1][j])
                else:
                    neigh.append(d[board[i-1][j]])
                    
                if j-1 >= 0 and j-1 < m:
                    if flag[i-1][j-1] == 0:
                        neigh.append(board[i-1][j-1])
                    else:
                        neigh.append(d[board[i-1][j-1]])
            
            if j+1 > 0 and j+1 < m:
                if flag[i][j+1] == 0:
                    neigh.append(board[i][j+1])
                else:
                    neigh.append(d[board[i][j+1]])
            
            if j-1 >= 0 and j-1 < m:
                if flag[i][j-1] == 0:
                    neigh.append(board[i][j-1])
                else:
                    neigh.append(d[board[i][j-1]])
                    
            return neigh
                
                       
        for i in range(n):
            for j in range(m):
                neigh = get_neigh(i,j)
                
                if board[i][j] == 1:
                    f = neigh.count(1)
                    
                    if f < 2:
                        board[i][j] = 0
                        flag[i][j] = 1
                        
                    elif f == 2 or f == 3:
                        board[i][j] = 1
                        
                    else:
                        board[i][j] = 0
                        flag[i][j] = 1
                else:
                    f = neigh.count(1)
                    
                    if f == 3:
                        board[i][j] = 1
                        flag[i][j] = 1
                    else:
                        board[i][j] = 0
