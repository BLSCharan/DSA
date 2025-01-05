class Solution(object):
    def reverseVowels(self, s):
        v="aeiouAEIOU"
        li=list(s)
        l,r=0,len(s)-1
        while l<r:
            if li[l] not in v:
                l+=1
                continue
            if li[r] not in v:
                r-=1
                continue    
            li[l],li[r]=li[r],li[l]
            l+=1
            r-=1
        return ''.join(li)
