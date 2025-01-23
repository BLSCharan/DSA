class Solution:
    def reverseBits(self, n):
        binary = format(n, '032b')  
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)
