class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] *numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        q = collections.deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        visited = 0
        while q:
            visited += 1
            vertex = q.popleft()
            for nei in adj[vertex]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return visited == numCourses
                