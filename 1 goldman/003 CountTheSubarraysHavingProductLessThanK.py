class Solution:
    
    # SLIDING WINDOW 
    def countSubArrayProductLessThanK(self, a, n, k):
        i,j=0,0
        product=1
        count=0
        
        while j<n:
            product*=a[j]
            
            while product>=k and i<j:
                product= product//a[i]
                i+=1
                
            if product<k:
                count+= ((j-i)+1)
            j+=1
            
        return count
