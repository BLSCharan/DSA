class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]
o = Solution()
m = input()
print(o.isPalindrome(m))
