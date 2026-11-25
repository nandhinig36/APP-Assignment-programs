from collections import defaultdict, Counter

def euler_path(edges):
    graph = defaultdict(list); degree = Counter(); vertices = set()
    for a,b in edges:
        graph[a].append(b); graph[b].append(a)
        degree[a] += 1; degree[b] += 1
        vertices.update((a,b))
    odd = [v for v in vertices if degree[v] % 2]
    if len(odd) not in (0,2): return None
    if not vertices: return []
    start = odd[0] if odd else next(iter(vertices))
    # Hierholzer's algorithm; remove each undirected edge once.
    stack, path = [start], []
    while stack:
        v = stack[-1]
        while graph[v] and not graph[v][-1]: graph[v].pop()
        if graph[v]:
            u = graph[v].pop()
            try: graph[u].remove(v)
            except ValueError: pass
            stack.append(u)
        else: path.append(stack.pop())
    return path[::-1] if len(path) == len(edges)+1 else None

if __name__ == "__main__":
    edges = [(0,1),(1,2),(2,0),(0,3)]
    path = euler_path(edges)
    print("Euler Path exists:", path is not None)
    if path: print("Path:", " -> ".join(map(str,path)))
