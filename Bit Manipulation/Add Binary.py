class Solution(object):
    def addBinary(self, a, b):
       x=int(a,2)
       y=int(b,2)
       z=x+y
       return bin(z)[2:]
        
