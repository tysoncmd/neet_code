from collections import defaultdict
from typing import List

class GroupAnagramSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group_hash = defaultdict(list) # don't have to handle non-existent key
        # anagram_group_hash = {} # must handle non-existent key
        for strg in strs:
            count = [0] * 26
            for ltr in strg:
                count[ord(ltr) - ord("a")] += 1

            # if tuple(count) in anagram_group_hash:
            anagram_group_hash[tuple(count)].append(strg)
            # else:
            #     anagram_group_hash[tuple(count)] = [strg]


        return list(anagram_group_hash.values())

    # O (m * n) Optimal
    # m = the number of strings
    # n = the average string length



if __name__ == '__main__':
    strs = ["", "act", "pots", "tops", "cat", "stop", "hat", "klajshdflhakuseku"]
    solve_optimal = GroupAnagramSolution()
    result_optimal = solve_optimal.groupAnagrams(strs)

    # solve_non_optimal = GroupAnagramSolution()
    # result_non_optimal = solve_non_optimal.groupAnagramsBrute(strs)
    # print(result_optimal)
    print(result_optimal)