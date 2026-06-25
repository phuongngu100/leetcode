class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        1. Using hashset. Time is O(n)
        '''

        # seen, res = set(), set()

        # for l in range(len(s)-9):
        #     cur = s[l : l+10]
        #     if cur in seen:
        #         res.add(cur)
        #     seen.add(cur)
        # return list(res)

        '''
        2. Using hashmap
        '''

        if len(s) < 10:
            return []
        #initiate the hashmap
        hashmap = defaultdict(int)
        res = []
        for l in range(len(s)-9):
            cur = s[l : l+10]
            hashmap[cur] += 1
            if hashmap[cur] == 2:
                res.append(cur)
        return res        