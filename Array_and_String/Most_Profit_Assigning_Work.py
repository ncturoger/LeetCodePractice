class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        difficulty_tuple = []
        max_profit = 0
        work_profit = dict()

        for idx, dific in enumerate(difficulty):
            difficulty_tuple.append((dific, profit[idx]))
        difficulty_tuple.sort()

        for w in worker:
            if work_profit.get(w):
                max_profit += work_profit.get(w)
            
            else:
                profit_list = [i[1] for i in difficulty_tuple if i[0] <=  w]
                if profit_list:
                    max_p = max(profit_list)
                    max_profit += max_p
                    work_profit[w] = max_p

        return max_profit
            