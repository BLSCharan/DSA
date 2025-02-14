class Solution(object):
    def isValid(self, s):
        st=[]
        m={')':'(','}':'{',']':'['}
        for char in s:
            if char in m:
                te=st.pop() if st else '#'
                if m[char]!=te:
                    return False
            else:
                st.append(char)
        return not st
