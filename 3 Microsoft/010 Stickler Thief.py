class Solution:  
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        if n<=2:
            return max(a)
            
        dp=[0 for i in range(n)]
        dp[-1]= a[-1]
        dp[-2]= max(a[-2],a[-1])
        
        for i in range(n-3,-1,-1):
            dp[i]= max(a[i]+dp[i+2]  , dp[i+1])
            
        return dp[0]
