class Solution(object):
    def isBalanced(self, num):
        e = 0  
        o = 0  
        for i in range(len(num)):
            digit = int(num[i]) 
            if i % 2 == 0:
                e += digit  
            else:
                o += digit  
        return e == o

