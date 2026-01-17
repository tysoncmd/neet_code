

class HasDuplicateSolution:
    def has_duplicate(self, nums: List[int]) -> bool:
        num_hash = set()
        for num in nums:
            if num in num_hash:
                return True
            num_hash.add(num)

        return False



if __name__ == '__main__':
    solver = HasDuplicateSolution()
    solution = solver.has_duplicate(nums=[1, 2, 3, 4, 5, 5])
    print(solution)