class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = []
        word = ""
        for c in s:
            if c != ' ':
                word += c
            
            else:
                word_list.append(word)
                word = ""
        if word:
            word_list.append(word)
        
        return " ".join([word_list[i] for i in range(len(word_list)-1, -1, -1) if word_list[i]])

print(Solution().reverseWords("the sky is blue"))