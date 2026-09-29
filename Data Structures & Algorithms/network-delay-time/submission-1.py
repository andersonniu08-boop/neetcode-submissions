class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        shortest = {}
        for src, dst, weight in times:
            adj[src].append([weight, dst])
        
        minheap = [[0, k]]

        while minheap:
            w1, v1 = heapq.heappop(minheap)
            if v1 in shortest:
                continue
            shortest[v1] = w1
            for w2, v2 in adj[v1]:
                if v2 not in shortest:
                    heapq.heappush(minheap, [w1 + w2, v2])
        
        if n > len(shortest):
            return -1
        else:
            return max(shortest.values())
                