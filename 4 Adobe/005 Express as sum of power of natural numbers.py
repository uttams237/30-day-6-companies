def numHelper(i,n,x,dp):
    if i**x>n:
        return 0
        
    if i**x==n:
        return 1
        
    if dp[n-(i**x)][i+1]==-1:
        tempAns= numHelper(i+1,n-(i**x),x,dp)
        dp[n-(i**x)][i+1]= tempAns
    else:
        tempAns=dp[n-(i**x)][i+1]
        
    if dp[n][i+1]== -1:
        tempAns2= numHelper(i+1,n,x,dp)
        dp[n][i+1]= tempAns2
    else:
        tempAns2= dp[n][i+1]
        
    return tempAns+tempAns2
    
    
    
class Solution:
	def numOfWays(self, n, x):
	    ii = int(n**(1/x))+1
	    dp= [[-1 for i in range(ii+10)] for j in range(n+10)]
	    count= numHelper(1,n,x,dp)
        return count% (7+ 10**9)
