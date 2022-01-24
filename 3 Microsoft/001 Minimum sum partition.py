#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
	    if n==1:
	        return arr[0]
        if n==2:
            return min(abs(arr[0]-arr[1])  ,abs(arr[0]+arr[1]))
            
	    total= sum(arr)
	    half= total//2
	    dp=[[False for i in range(n+1)] for j in range(half+1)]
	    
	    for i in range(n+1):
	        dp[0][i]=True
	        
        for i in range(1,n+1):
            if arr[i-1]==1:
                dp[1][i]=True
            else:
                dp[1][i]=dp[1][i-1]
	        
        for j in range(2,half+1):
            for i in range(1,n+1):
                if j==arr[i-1]:
                    dp[j][i]=True
                else:
                    if j-arr[i-1]>=0:
                        dp[j][i]= ((  dp[j-arr[i-1]]  [i-1]) | (dp[j][i-1]))
                    else:
                        dp[j][i]= (dp[j][i-1])
                        
                    
        # for ele in dp:
        #     print(ele)
            
        for j in range(half,-1,-1):
            if dp[j][-1]:
                return abs(total-j-j)
                
                
                
                
                
                
