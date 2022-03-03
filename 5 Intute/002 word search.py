class Solution:
    def north(self,grid,i,j,word):
        for alp in word:
            if i>=0 and grid[i][j]==alp:
                i-=1
            else:
                return 0
        return 1
        
    def east(self,grid,i,j,word):
        for alp in word:
            if j<len(grid[0]) and grid[i][j]==alp:
                j+=1
            else:
                return 0
        return 1
        
    def south(self,grid,i,j,word):
        for alp in word:
            if i<len(grid) and grid[i][j]==alp:
                i+=1
            else:
                return 0
        return 1
        
    def west(self,grid,i,j,word):
        for alp in word:
            if j>=0 and grid[i][j]==alp:
                j-=1
            else:
                return 0
        return 1
        
    def ne(self,grid,i,j,word):
        for alp in word:
            if (i>=0 and j<len(grid[0])) and grid[i][j]==alp:
                j+=1
                i-=1
            else:
                return 0
        return 1
        
    def es(self,grid,i,j,word):
        for alp in word:
            if (i<len(grid) and j<len(grid[0])) and grid[i][j]==alp:
                j+=1
                i+=1
            else:
                return 0
        return 1
        
    def sw(self,grid,i,j,word):
        for alp in word:
            if (i<len(grid) and j>=0) and grid[i][j]==alp:
                j-=1
                i+=1
            else:
                return 0
        return 1
        
    def wn(self,grid,i,j,word):
        for alp in word:
            if (i>=0 and j>=0) and grid[i][j]==alp:
                j-=1
                i-=1
            else:
                return 0
        return 1
    
        
	def searchWord(self, grid, word):
	    c=[]
	    
	    for i in range(len(grid)):
	        for j in range(len(grid[0])):
	            if Solution.north(self,grid,i,j,word):
	                c.append([i,j])
	            if Solution.ne(self,grid,i,j,word):
	                c.append([i,j])
	            if Solution.east(self,grid,i,j,word):
	                c.append([i,j])
	            if Solution.es(self,grid,i,j,word):
	                c.append([i,j])
	            if Solution.south(self,grid,i,j,word):
	                c.append([i,j])
	            if Solution.sw(self,grid,i,j,word):
	                c.append([i,j])
	            if Solution.west(self,grid,i,j,word):
	                c.append([i,j])
	            if Solution.wn(self,grid,i,j,word):
	                c.append([i,j])
	            
        return c
