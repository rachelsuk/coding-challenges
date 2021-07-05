class Solution(object):
    def findErrorNums(self, nums):
        nums = sorted(nums)
        output = []
        nums_set = set()
        for num in nums:
            if num in nums_set:
                output.append(num)
                break
            else:
                nums_set.add(num)
        for i in range(1,len(nums)+1):
            if i not in nums:
                output.append(i)
                break
        return output
            


