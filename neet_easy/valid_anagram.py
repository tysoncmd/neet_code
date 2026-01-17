
class Solution_Anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for ltr in s:
            if ltr in s_hash:
                s_hash[ltr] += 1
            else:
                s_hash[ltr] = 1
        for ltr in t:
            if ltr in t_hash:
                t_hash[ltr] += 1
            else:
                t_hash[ltr] = 1
        return s_hash == t_hash


if __name__ == '__main__':
    solver = Solution_Anagram()
    solution = solver.isAnagram(s="racecar", t="carrace")
    print(solution)