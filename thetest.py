from collections import defaultdict 
class Solution:
    def findLength(self, A, B):
        
        #def checkLv(Aa,Bb,L):
            
            
        def rbk_ini(ar,L):
            s=0
            f = 1
            for i in range(0,L):
                s = s + ar[i]*5**i
            return s
          

        def rbk(AA,BB,L):
            v = rbk_ini(AA,L)
            D = defaultdict(list)
            D[v].append(0)
            
            n = L
            
            while (n<len(AA)):
                v = (v - AA[n-L])/5
                v += AA[n] * 5**(L-1)
                n+=1
                D[v].append(n-L)
                
            v = rbk_ini(BB,L)
            n = L
            if vb in D: 
                return True
            
            while (n<len(BB)):
                v = (v - BB[n-L])/5
                v += AA[n] * 5**(L-1)
                n+=1
                if v in D:
                    for i in D[v]:
                        if AA[i:i+L] == BB[n-L:n]: return True
                        
                    
                    
            return False
            

        
        if len(A)>len(B):
            A, B = B, A
        
        La = len(A)
        
        lo, hi = 0, La+1
        
        while (hi-lo>1):
            c = (hi+lo)//2
            
        
        
        
        
        
        
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
