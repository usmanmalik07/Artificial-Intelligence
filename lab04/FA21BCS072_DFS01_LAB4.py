def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


if __name__ == '__main__':
    print("Recursive DFS")
    
    graph = {     
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],     
    'Zerind': ['Arad', 'Oradea'],     
    'Oradea': ['Zerind', 'Sibiu'],     
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],     
    'Timisoara': ['Arad', 'Lugoj'],     
    'Lugoj': ['Timisoara', 'Mehadia'],     
    'Mehadia': ['Lugoj', 'Drobeta'],     
    'Drobeta': ['Mehadia', 'Craiova'],     
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],     
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],     
    'Fagaras': ['Sibiu', 'Bucharest'],     
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],    
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'], 
    'Giurgiu': ['Bucharest'],     
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],     
    'Hirsova': ['Urziceni', 'Eforie'],     
    'Eforie': ['Hirsova'],     
    'Vaslui': ['Iasi', 'Urziceni'],     
    'Iasi': ['Vaslui', 'Neamt'],     
    'Neamt': ['Iasi']
}   

result = dfs_recursive(graph, 'Arad')
print(result)

        