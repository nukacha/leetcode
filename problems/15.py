from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> Set[Tuple[int]]:
        nums.sort()
        triplet_set = set()
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            if i and nums[i] == nums[i - 1]:
                continue
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    triplet_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1
        return triplet_set
