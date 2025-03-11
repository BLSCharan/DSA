class Solution(object):
    def numberOfSubstrings(self, s):
        count = {'a': 0, 'b': 0, 'c': 0}  # Dictionary to store character counts
        left = 0  # Left pointer
        result = 0  # Store the number of valid substrings

        for right in range(len(s)):
            count[s[right]] += 1  # Expand the window by including s[right]

            # When all three characters are present, move left to count valid substrings
            while all(count.values()):
                result += len(s) - right  # All substrings from (left, right) to (left, end) are valid
                count[s[left]] -= 1  # Shrink the window from the left
                left += 1  # Move left pointer

        return result
