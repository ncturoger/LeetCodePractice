class Solution(object):
    # order is wrong
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        print(self.gen_p(n))
        return list(self.gen_p(n))
    
    def gen_p(self, n):
        ans = set([])
        if n == 1:
            ans.add("()")
            return ans

        for i in self.gen_p(n-1):
            
            ans.add(i + "()")
            ans.add("(" + i + ")")
            
            ans.add("()" + i)

           
            
            
        
        return ans


assert Solution().generateParenthesis(3) == [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]