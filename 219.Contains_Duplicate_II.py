from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = [i]
            else:
                if i - my_dict[nums[i]][-1] <= k: return True
                else: my_dict[nums[i]].append(i)
        return False