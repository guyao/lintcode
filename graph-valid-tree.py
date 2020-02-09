class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        import collections
        neighbor = collections.defaultdict(list)
        for u, v in edges:
            neighbor[u].append(v)
            neighbor[v].append(u)
        visited = {}
        q = [0]
        visited[0] = True
        while q:
            cur = q.pop(0)
            visited[cur] = True
            for node in neighbor[cur]:
                if node not in visited:
                    visited[node] = True
                    q.append(node)
        return len(visited) == n


n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Solution().validTree(n, edges)
