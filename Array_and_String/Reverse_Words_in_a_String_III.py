class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = ""
        word_list = []
        for c in s:
            if c != " ":
                word += c
            
            else:
                word_list.append(word[::-1])
                word = ""

        if word:
            word_list.append(word[::-1])
        
        return " ".join([word for word in word_list if word])

print(Solution().reverseWords("the"))