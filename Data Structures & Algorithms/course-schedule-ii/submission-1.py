class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for i, j in prerequisites:
            adj[i].append(j)
            indegree[j] += 1
        
        q = collections.deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        res = []

        while q:
            finish += 1
            vertex = q.popleft()
            res.append(vertex)
            for nei in adj[vertex]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if finish != numCourses:
            return []
        
        return res[::-1]