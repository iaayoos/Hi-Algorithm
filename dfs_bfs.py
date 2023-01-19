from collections import deque
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

node, edge, start=map(int, input().split())
lists=[]
visited = [False]*(node+1)
visited2 = [False]*(node+1)
graph=[[] for _ in range(node+1)]
for i in range(edge):
    c=list(map(int,input().split()))
    lists.append(c)
for a in lists:
    d=int(a[0])
    e=int(a[1])
    graph[d].append(e)
    graph[e].append(d)
for b in graph:
    b.sort()

dfs(graph,start,visited)
print()
bfs(graph,start,visited2)
