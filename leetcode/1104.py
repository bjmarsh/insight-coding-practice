class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        # the level of the tree, starting counting at 1
        level = label.bit_length()
        if level % 2 == 1:
            ipos = label - (1<<(level-1))
        else:
            ipos = (1<<level)-1 - label
        
        
        path = []
        while level > 0:
            
            if level % 2 == 1:
                label = (1<<(level-1)) + ipos
            else:
                label = (1<<level) - 1 - ipos
            path.append(label)
            
            ipos //= 2
            level -= 1
        
        return path[::-1]
