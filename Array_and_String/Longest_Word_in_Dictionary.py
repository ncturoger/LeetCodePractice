class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        words.sort()
        words.sort(key=len)
        
        seen = set()
        seen.add('')
        longest = ''
        for word in words:
            if word[:-1:] in seen:
                seen.add(word)
                longest = longest if len(longest) >= len(word) else word
        
        return longest



assert Solution().longestWord(["w","wo","wor","worl", "world"]) == "world"
assert Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple"