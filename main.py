
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num2 + num == target:
                    print(i)
                    print(j)
                    return [i, j]


if __name__ == '__main__':
    s = Solution
    s.twoSum(s, [2, 4], 6)
