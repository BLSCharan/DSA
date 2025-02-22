class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        arr = []  
        level, index, num = 0, 0, 0

        while index < len(traversal):
            if traversal[index] != '-':
                num = num * 10 + int(traversal[index])
            else:
                if num:
                    arr.append((level, num))
                    num = 0
                    level = 1
                else:
                    level += 1
            index += 1
        
        arr.append((level, num))  

        root = TreeNode(arr[0][1])
        mp = {0: root}

        for i in range(1, len(arr)):
            parent_level = arr[i][0] - 1
            node = TreeNode(arr[i][1])
            mp[arr[i][0]] = node

            if not mp[parent_level].left:
                mp[parent_level].left = node
            else:
                mp[parent_level].right = node

        return root
