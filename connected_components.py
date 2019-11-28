class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        
        #Stack 
        dfs = []
        
        #Adjacency
        adj_dict = dict()
        
        count = 0
        ans = 0
        
        for edge in edges:
            from_edge = edge[0]
            to_edge = edge[1]
            
            if from_edge in adj_dict:
                adj_dict[from_edge].append(to_edge)
            
            if from_edge not in adj_dict:
                adj_dict[from_edge] = [to_edge]
                
            if to_edge in adj_dict:
                adj_dict[to_edge].append(from_edge)
            
            if to_edge not in adj_dict:
                adj_dict[to_edge] = [from_edge]
            
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs.append(i)
            
            while len(dfs) > 0:
                current = dfs.pop()
                visited[current] = True
                
                if current in adj_dict:
                    for neighbor in adj_dict[current]:
                        if not visited[neighbor]:
                            dfs.append(neighbor)
                        
        return ans
    
