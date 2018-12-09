class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        check_dict = dict()
        max_len = 0

        if len(s) == 1:
            return 1
        
        i = 0
        while i < len(s):
            if check_dict.get(s[i]) is None:
                check_dict[s[i]] = i
                i = i + 1
            else:
                max_len = max(len(check_dict.keys()), max_len)
                last_meet = check_dict.get(s[i])
                check_dict.clear()
                i = last_meet + 1

        
        if check_dict:
            max_len = max(len(check_dict.keys()), max_len)
        
        return max_len

assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("dvdf") == 3
assert Solution().lengthOfLongestSubstring("anviaj") == 5