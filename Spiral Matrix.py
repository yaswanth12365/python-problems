    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    n = len(matrix)
    m = len(matrix[0])
    r = c= 0
    
    def valid(r,c):
        if r<n and r>=0 and c<m and c>=0 and matrix[r][c]!=None:
            return True
        return False
    
    res = []
    total = n*m
    count =0
    dr,dc = dirs[0]
    curdirs = 0
    while(count<n*m):
        count+=1
        res.append(matrix[r][c])
        matrix[r][c] = None
        if not valid(r+dr,c+dc):
            curdirs+=1
            dr,dc = dirs[curdirs%4]
            
        r = r+dr
        c = c+dc
            
    return res
