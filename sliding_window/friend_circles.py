class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        rows = len(M)
        if rows < 1:
            return 0
        cols = len(M[0])
        num_circles = 0
        dfs = []
        
        friend_zoned = [False]*rows
        
        for i in range(rows):
            if not friend_zoned[i]:
                num_circles += 1
                dfs.append(i)
                
                while len(dfs) > 0:
                    current = dfs.pop()
                    friend_zoned[current] = True
                    
                
                    for j in range(cols):
                        if not friend_zoned[j] and M[current][j] == 1:
                            dfs.append(j)
        return num_circles
                
        
        
