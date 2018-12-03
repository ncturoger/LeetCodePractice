class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, 1+n):
            word = ""
            if i % 3 == 0:
                word += "Fizz"
            
            if i % 5 == 0:
                word += "Buzz"
            
            if word:
                result.append(word)
            
            else:
                result.append(str(i))
        
        return result