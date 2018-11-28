class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle:
            needle_len = len(needle)

            for i in range(len(haystack) - needle_len + 1):
                if self.check_same(haystack[i:i+needle_len], needle):
                    return i
                
            return -1

        else:
            return 0

    def check_same(self, a_string, b_string):
        for i in range(len(a_string)):
            if a_string[i] != b_string[i]:
                return False
        return True

print(Solution().strStr("hello", "ll"))