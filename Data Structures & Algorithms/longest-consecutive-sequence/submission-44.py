from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = defaultdict(int)
        num_set = set(nums)
        global_streak = 0

        if len(nums) == 0:
            return 0

        for num in num_set:
            streak = 0
            cur_num = num
            back_check = True
            forward_check = True

            back_cur_num = num
            while back_check:
                if (back_cur_num - 1) in num_set:
                    streak += 1
                    back_cur_num -= 1
                else:
                    break
            
            for_cur_num = num
            while forward_check:
                if (for_cur_num + 1) in num_set:
                    streak += 1
                    for_cur_num += 1
                else:
                    break
            
            if streak > global_streak:
                global_streak = streak
        
        return global_streak + 1 






