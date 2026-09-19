class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for i, j in prerequisites:
            indegree[j] += 1
            adj[i].append(j)
        
        q = collections.deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        res = []
        finish = 0
        while q:
            node = q.popleft()
            res.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if finish != numCourses:
            return []
        
        return res[::-1]
                