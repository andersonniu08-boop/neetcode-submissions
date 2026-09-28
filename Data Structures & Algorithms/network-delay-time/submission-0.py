class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for src, dst, weight in times:
            adj[src].append([dst, weight])
    
        minHeap = [[0, k]]

        shortest = {}
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in shortest:
                continue
            shortest[v1] = w1
            for v2, w2 in adj[v1]:
                if v2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, v2])
        
        if len(shortest) < n:
            return -1
        else:
            return max(shortest.values())
