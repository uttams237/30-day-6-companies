'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to count number of subtrees having sum equal to given sum.
def countSubtreesWithSumX(root, x):
    global count
    count=0
    
    def summ(root):
        global count
        if root is None:
            return 0
            
        temp= root.data+summ(root.left)+summ(root.right)
        
        if temp==x:
            count+=1
            
        return temp
        
    overallSum= summ(root)
    
    return count
