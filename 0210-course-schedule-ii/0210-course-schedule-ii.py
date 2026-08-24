class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        state = [0] * numCourses
        res = []
        
        def dfs(course):
            '''
            denote 0 as unvisited
            1 as is visiting right now
            2 as done with this course
            after done put it to the result
            '''        
            if state[course] == 1:
                return False # we detect a cycle
            if state[course] == 2:
                return True # we done with this course
            state[course] =1
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            state[course] = 2 #done after dfs 
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return [ ]
        return res[::-1]

        
            
            

        