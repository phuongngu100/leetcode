class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        for start in range(len(graph)):
            if color[start] != -1:
                continue
            color[start] = 0 # color the first 0
            q = deque([start]) # add the first node to the queue


            while q:
                node = q.popleft()
                
                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        q.append(nei)
                    elif color[nei] == color[node]:
                        return False
        return True






















        # parent = list(range(len(graph)))

        # def find(x):
        #     if x != parent[x]:
        #         parent[x] = find(parent[x])
        #     return parent[x]
        # def union(a,b):
        #     root_a, root_b = find(a), find(b)
        #     if root_a == root_b:
        #         return False
        #     parent[root_a] = root_b
        #     return True
        # neighbors = {}
        # #build the graph
        # for node, nei in enumerate(graph):
        #     neighbors[node] = nei
        
        # for node in range(len(graph)):
        #     # Get the neighbors of the current node.
        #     node_neighbors = neighbors[node]
        #     # If this node has no neighbors,
        #     # there is nothing to check.
        #     if not node_neighbors:
        #         continue
        #     # Pick the first neighbor as the
        #     # representative of the "opposite group".
        #     # All neighbors of node must be
        #     # in the same group.
        #     first_neighbor = node_neighbors[0]
        #      # Put every other neighbor into the
        #     # same group as first_neighbor.
        #     for other_neighbor in node_neighbors[1:]:

        #         union(first_neighbor, other_neighbor)
                    
        #     # The current node and its neighbors
        #     # MUST belong to different groups.
        #     #
        #     # If they have the same root, they are
        #     # in the same group -> NOT bipartite.
        #     if find(node) == find(first_neighbor):
        #         return False


        # Every node passed the bipartite check.
        return True




        


        