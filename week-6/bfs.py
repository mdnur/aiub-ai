def bfs(graph, start, path=[]):
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:
            path = path + [vertex]
            queue = queue + graph[vertex]
    return path


def bfs_reverse(graph, start, path=[]):
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:
            path = path + [vertex]
            queue = graph[vertex][::-1] + queue
    return path

def dfs(graph, start, path=[]):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in path:
            path.append(vertex)
            stack.extend(reversed(graph[vertex]))
    return path


def dfs_reverse(graph, start, path=[]):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in path:
            path = [vertex] + path  
            stack.extend(graph[vertex][::-1])
    return path



if __name__ == '__main__':
    
    graph = {'A': ['B', 'C'],
             'B': ['D','E'],
             'C': ['F', 'G'],
             'D': [],
             'E': [],
             'F': [],
             'G': []}
    
print('bfs: ', bfs(graph, 'A'))
print('bfs reverse: ', bfs_reverse(graph, 'A'))
print('dfs: ', dfs(graph, 'A'))
print('dfs reverse: ', dfs_reverse(graph, 'A'))
