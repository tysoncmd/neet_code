from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        raise IndexError("Value provided does not have a compliment within bounds of Index")

# You are working through the list left to right, you know
# that there is only 1 solve and there are no duplicates
# You only need to store values you have viewed because you
# work left to right. You are caching those values NOT for dup
# checking, but to find the right compliment later on.
# Because you always find the second, higher index compliment
# last you put that value last in your return. When you don't find
# the value, you store the num as the key because you are doing an in
# search on the keys, then you can return the value in your return statement


if __name__ == '__main__':
    solver = Solution()
    solution = solver.two_sum(nums=[1, 2, 3, 4, 5, 6, 7], target=7)
    print(solution)
