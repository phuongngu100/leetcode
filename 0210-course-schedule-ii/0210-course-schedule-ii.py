class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # if not prerequisites:
        #     return [0]
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        state = [0] * numCourses
        res = []
        
        def dfs(course):
            if state[course] == 1:
                return False # detect cycle
            if state[course] == 2:
                return True # complete the process
            # mark the current as visiting
            state[course] = 1
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            # finish this course
            state[course] = 2
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res[::-1]
            
            

        