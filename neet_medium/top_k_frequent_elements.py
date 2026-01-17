import heapq
from collections import defaultdict, Counter
from typing import List

class TopKFrequentSortSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        sorted_elements = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)

        return sorted_elements[:k]
class TopKFreqHeapSolution:
    def topKFreq(self, nums: List[int], k: int) -> List[int]:
        heapList = []
        count_map = Counter(nums)

        for num, freq in count_map.items():
            heapq.heappush(heapList, (freq, num))

            if len(heapList) > k:
                heapq.heappop(heapList)

        return [pair[1] for pair in heapList]


class TopKFreqBucketSortSolution:
    def topKFreq(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        bucket_list = [[] for _ in range(len(nums) + 1)]

        for num, count in count_map.items():
            bucket_list[count].append(num)

        top_k_list = []
        for i in range(len(bucket_list) - 1, 0, -1):
            for n in bucket_list[i]:
                top_k_list.append(n)
                if len(top_k_list) == k:
                    return top_k_list
        return top_k_list


if __name__ == '__main__':
    # numbers = [1, 2, 2, 3, 3, 3]
    numbers = [1,2]
    frequency = 2
    # solution = TopKFrequentSortSolution()
    # print(solution.topKFrequent(numbers, frequency))
    # heapSolution = TopKFreqHeapSolution()
    # print(heapSolution.topKFreq(numbers, frequency))
    bucketSolution = TopKFreqBucketSortSolution()
    print(bucketSolution.topKFreq(numbers, frequency))