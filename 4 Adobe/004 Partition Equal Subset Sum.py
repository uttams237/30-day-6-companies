# modified version of "SUBSEQUENCE SUM TO K"
class Solution:
    def equalPartition(self, N, arr):
        ss= sum(arr)
        if ss%2 :
            return 0
            
        s= ss//2
        
        dp=[[0 for i in range(s+1)] for j in range(N+1)]
        
        for ele in dp:
            ele[0]=1
            
        for j in range(1,N+1):
            for i in range(1,s+1):
                if arr[j-1]== i:
                    dp[j][i]=1
                else:
                    if i-arr[j-1] <0:
                        dp[j][i]=dp[j-1][i]
                    else:
                        dp[j][i]= max(dp[j-1][i] , dp[j-1][i-arr[j-1]])
                    
        return dp[-1][-1]
