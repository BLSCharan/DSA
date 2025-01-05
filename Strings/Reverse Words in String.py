class Solution(object):
    def reverseWords(self, s):
        w=s.strip().split()
        return ' '.join(w[::-1])
