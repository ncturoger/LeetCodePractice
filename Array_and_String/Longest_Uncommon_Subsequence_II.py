class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_length = -1
        i = 0
        while i < len(strs):
            j = 0
            while j < len(strs):
                if i != j:
                    max_length = max(max_length, self.check_length_for_sub(strs[i], strs[j]))
                j += 1
            i += 1 

        return max_length
    
    def check_length_for_sub(self, sub, string):
        print("sub:{} strinng:{}".format(sub, string))
        if len(sub) > len(string):
            return -1
        
        else:
            isSub = False
            string = list(string)
            for i in sub:
                if i in string:
                    string.remove(i)
                else:
                    return len(sub)

            return -1
    
assert Solution().findLUSlength(["aba", "cdc", "eae"]) == 3
assert Solution().findLUSlength(["aaa","acb"]) == 3
assert Solution().findLUSlength(["aabbcc", "aabbcc","bc"]) == 2
