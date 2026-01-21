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
        result = []
        prefix_prod = list(accumulate(nums, operator.mul))
        suffix_prod = list(reversed(list(accumulate(reversed(nums), operator.mul))))
        for index, num in enumerate(nums):
            if index == 0:
                result.append(suffix_prod[index +1])
            elif index == len(nums) -1:
                result.append(prefix_prod[index -1])
            else:
                result.append(prefix_prod[index -1] * suffix_prod[index +1])

        return result



if __name__ == "__main__":
    test1 = [1, 2, 4, 6]
    test2 = [-1,0,1,2,3]
    test3 = [2, 2, 3, 4]
    test4 = [1, 2, 3, 4]

    bruteSolution = BruteSolution()
    prefixSuffixSolution = PrefixSuffixSolution()
    result_b = bruteSolution.productExceptSelf(test4)
    result_p = prefixSuffixSolution.productExceptSelf(test4)

    print(result_b)
    print(result_p)