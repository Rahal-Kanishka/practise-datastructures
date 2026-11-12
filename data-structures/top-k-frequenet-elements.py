class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # if nums == None or len(nums) == 0:
        #     return []
        count = {}
        # count occurances
        for item in nums:
            # print('item: ', item, 'count: ', count.get(item) )
            if count.get(item):
                count[item] = count.get(item) + 1
            else:
                count[item] = 1
        # sort by the count on decending order
        sorted_items = sorted(count, key=lambda x: count[x], reverse=True)
        return sorted_items[:k]
        