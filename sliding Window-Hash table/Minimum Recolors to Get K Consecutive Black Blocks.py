class Solution(object):
    def minimumRecolors(self, blocks, k):
        count_white = blocks[:k].count('W')
        min_white = count_white
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                count_white += 1 
            if blocks[i - k] == 'W':
                count_white -= 1 
            
            min_white = min(min_white, count_white)

        return min_white  
        
