class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        jew = dict()
        for c in J:
            jew[c] = True
        
        for item in S:
            if jew.get(item):
                count += 1
        return count
