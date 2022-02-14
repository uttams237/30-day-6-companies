import sys
sys.setrecursionlimit(10**7)

class Solution:
    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, g):
	    n=len(g)
	    vis=[[False for i in range(len(g[0]))] for j in range(len(g))]
	    
	    def iss(i,j):
	        if i<0 or i>=len(g):
	            return False
            if j<0 or j>=len(g[0]):
                return False
            
            return True

	    
	    def dfs(g,vis,i,j):
	        count=1
	        vis[i][j]=True
	        
	        ti,tj=i-1,j-1
	        if iss(ti,tj) and g[ti][tj]==1 and vis[ti][tj] is False :
	            count+= dfs(g,vis,ti,tj)
	            
            ti,tj=i-1,j
	        if iss(ti,tj) and g[ti][tj]==1 and vis[ti][tj] is False :
	            count+= dfs(g,vis,ti,tj)
	            
            ti,tj=i-1,j+1
	        if iss(ti,tj) and g[ti][tj]==1 and vis[ti][tj] is False :
	            count+= dfs(g,vis,ti,tj)
	            
            ti,tj=i,j+1
	        if iss(ti,tj) and g[ti][tj]==1 and vis[ti][tj] is False :
	            count+= dfs(g,vis,ti,tj)
	            
            ti,tj=i+1,j+1
	        if iss(ti,tj) and g[ti][tj]==1 and vis[ti][tj] is False :
	            count+= dfs(g,vis,ti,tj)
	            
            ti,tj=i+1,j
	        if iss(ti,tj) and g[ti][tj]==1 and vis[ti][tj] is False :
	            count+= dfs(g,vis,ti,tj)
	            
            ti,tj=i+1,j-1
	        if iss(ti,tj) and g[ti][tj]==1 and vis[ti][tj] is False :
	            count+= dfs(g,vis,ti,tj)
	            
            ti,tj=i,j-1
	        if iss(ti,tj) and g[ti][tj]==1 and vis[ti][tj] is False :
	            count+= dfs(g,vis,ti,tj)
	            
            return count
            
            
        ans= sys.maxsize*(-1)
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]==1 and vis[i][j] is False:
                    ans= max(ans, dfs(g,vis,i,j))
                    
        return ans
