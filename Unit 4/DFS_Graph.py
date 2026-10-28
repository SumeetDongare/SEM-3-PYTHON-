#create a graph using an Adjacency Matrix and perform Depth First Search (DFS)

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
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))

    graph[u][v] = 1
    graph[v][u] = 1

# Display Adjacency Matrix
print("Adjacency Matrix:")
for row in graph:
    print(row)

# Depth First Search
def dfs(graph, visited, vertex):
    print(vertex, end=" ")
    visited[vertex] = True

    for i in range(len(graph)):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(graph, visited, i)


source = int(input("Enter source vertex: "))

visited = [False] * n

print("DFS Traversal:")
dfs(graph, visited, source)

#Python program: Adjacency List + DFS

# Create graph using Adjacency List
n = int(input("Enter number of vertices: "))

graph = []

for i in range(n):
    graph.append([])

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))

    graph[u].append(v)
    graph[v].append(u)

# Display Adjacency List
print("Adjacency List:")
for i in range(n):
    print(i, ":", graph[i])

# Depth First Search
def dfs(graph, visited, vertex):
    print(vertex, end=" ")
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)


source = int(input("Enter source vertex: "))
visited = [False] * n

print("DFS Traversal:")
dfs(graph, visited, source)
