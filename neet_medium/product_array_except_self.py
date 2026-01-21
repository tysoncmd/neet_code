from typing import List
from itertools import accumulate
import operator

class BruteSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        calc_list = []
        for i in range(len(nums)):
            list_wo_num = [num for index, num in enumerate(nums) if index != i]

            calc = 0
            for index, num in enumerate(list_wo_num):
                if index == 0:
                    calc = num
                else:
                    calc = calc * num
            calc_list.append(calc)

        return calc_list

class PrefixSuffixSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = list(accumulate(nums, operator.mul))
        suffix_prod = list(accumulate(reversed(nums), operator.mul))
        print(prefix_prod)
        print(suffix_prod)



if __name__ == "__main__":
    test1 = [1, 2, 4, 6]
    test2 = [-1,0,1,2,3]
    test3 = [2, 2, 3, 4]

    bruteSolution = BruteSolution()
    # prefixSuffixSolution = PrefixSuffixSolution()
    result = bruteSolution.productExceptSelf(test3)

    print(result)