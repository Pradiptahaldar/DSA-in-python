class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True
        provinces = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    if union(i, j):
                        provinces -= 1
        return provinces