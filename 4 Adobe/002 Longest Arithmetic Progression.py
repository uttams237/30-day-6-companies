class Solution:
    def lengthOfLongestAP(self, A, n):
        
        if n<=2:
            return n
            
            
        arr= [[0 for i in range(n)] for j in range(n)]
        
        for ele in arr:
            ele[-1]=2
            
        lap=2  #length of longest arthematic progression
        
        # if a,b,c are in AP ,ie a+c= 2b
        
        for b in range(n-2,0,-1):
            a,c= b-1,b+1
            
            while a>=0 and c<n:
                if A[a]+A[c] < 2*(A[b]) :
                    c+=1
                
                
                elif A[a]+A[c] > 2*(A[b]) :
                    arr[a][b]=2
                    a-=1
                
                # if A[a]+A[c]== 2*(A[b]):
                else:
                    arr[a][b]= 1+arr[b][c]
                    lap=max(lap, arr[a][b])
                    a-=1
                    c+=1
                    
            while a>=0 and c>=n:
                arr[a][b]=2
                a-=1
                    
        return lap
