#User function Template for python3
class TrieNode():
    def __init__(self):
        self.children=[None for i in range(26)]
        self.wordEnd=False
        
class Trie():
    def __init__(self):
        self.root= TrieNode()
        
    def insert(self,word):
        curr=self.root
        for alpha in word:
            ind= ord(alpha)-odr("a")
            if curr.children[ind] is None:
                curr.children[ind]=TrieNode()
            curr=curr.children[ind]
        curr.wordEnd=True
        
    def searchPrefix(self,word):
        
        
                
        
        
    



class Solution:
    def displayContacts(self, n, contact, s):
        
        
        
