



class Solution:
    # time exceed
    def rob(self, home_list):
        if home_list:
            self.max_mony_list = [None for i in range(len(home_list))]
            for i in range(len(home_list)-1, -1, -1):
                self.get_max_mony(i, home_list)
            return max(self.max_mony_list)
        
        else:
            return 0


    def get_max_mony(self, day, home_list):
        if not self.max_mony_list[day]:
            if day > len(home_list) - 3:
                self.max_mony_list[day] = home_list[day]

            else:
                mony_list = []
                i = 2
                while day + i < len(home_list):
                    if self.get_max_mony(day + i, home_list):
                        mony_list.append(self.get_max_mony(day + i, home_list))
                    i += 1
                if mony_list:
                    self.max_mony_list[day] = home_list[day] + max(mony_list)
                else:
                    self.max_mony_list[day] = home_list[day]

        else:
            return self.max_mony_list[day]
            
        




assert Solution().rob([2,7,9,3,1]) == 12 
assert Solution().rob([1,2,3,1]) == 4 
assert Solution().rob([0,0,0,0,0,0,0,0,0,0]) == 0








