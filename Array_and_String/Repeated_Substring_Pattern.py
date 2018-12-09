class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = s + s
        d = d[1:-1]
        
        return s in d

            
assert Solution().repeatedSubstringPattern("abab") == True
assert Solution().repeatedSubstringPattern("bb") == True