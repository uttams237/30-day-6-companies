class Solution:
    def subArraySum(self,arr, n, s): 
        i,j=0,0
        
        summ= arr[0]
        
        while j<n:
            
            while summ>s and i<j :
                summ-= arr[i]
                i+=1
                
            if summ==s:
                return [i+1,j+1]
                
            j+=1
            if j<n:
                summ+=arr[j]
            
        return [-1]
