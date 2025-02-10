class Solution(object):
    def clearDigits(self, s):
        r=""
        for c in s:
            if c.isdigit():
                if r:
                    r=r[:-1]
            else:
                r+=c
        return r
