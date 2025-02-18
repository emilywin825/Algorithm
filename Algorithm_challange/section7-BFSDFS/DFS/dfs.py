graph={
    'v1' : ['v2','v3']
    ,'v2' : ['v1','v4','v5']
    ,'v3' : ['v1','v6','v7']
    ,'v4' : ['v2','v8']
    ,'v5':  ['v2','v8']
    ,'v6' : ['v3','v8']
    ,'v7' : ['v3','v8']
    ,'v8' : ['v4','v5','v6','v7']
}

def dfs(start_node):
    visited = []
    stack  = [start_node]

    while stack:
        print(stack)
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])  
    return visited

print(dfs('v1'))
