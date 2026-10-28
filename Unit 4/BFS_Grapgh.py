
# Create graph using Adjacency Matrix
n = int(input("Enter number of vertices: "))

graph = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    graph.append(row)

e = int(input("Enter number of edges: "))

for i in range(e):
    # u = int(input("Enter starting vertex: "))
    # v = int(input("Enter ending vertex: "))
    u,v = map(int,input().split())
    graph[u][v] = 1
    graph[v][u] = 1

# Display Adjacency Matrix
print("Adjacency Matrix:")
for row in graph:
    print(row)

# BFS Traversal
def bfs(graph, visited, source):
    queue = [source]
    visited[source] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for i in range(len(graph)):
            if graph[vertex][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True


source = int(input("Enter source vertex: "))
visited = [False] * n

print("BFS Traversal:")
bfs(graph, visited, source)


# Create graph using Adjacency List
n = int(input("Enter number of vertices: "))

graph = []

for i in range(n):
    graph.append([])

e = int(input("Enter number of edges: "))

for i in range(e):
    # u = int(input("Enter starting vertex: "))
    # v = int(input("Enter ending vertex: "))
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# Display Adjacency List
print("Adjacency List:")
for i in range(n):
    print(i, ":", graph[i])

# BFS Traversal
def bfs(graph, visited, source):
    queue = [source]
    visited[source] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


source = int(input("Enter source vertex: "))
visited = [False] * n

print("BFS Traversal:")
bfs(graph, visited, source)
