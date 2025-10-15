def dfs(v, adjacencia, visitados):
    visitados[v] = True
    for vizinho in adjacencia[v]:
        if not visitados[vizinho]:
            dfs(vizinho, adjacencia, visitados)

def verificar_conexao(num_vertices, arestas):
    if num_vertices <= 1:
        return True
    
    #1. Criar a lista de adjacência
    adjacencia = [[] for _ in range(num_vertices)]
    for u, v, _ in arestas:
        adjacencia[u].append(v)
        adjacencia[v].append(u)

    #2. Inicializar array de controle
    visitados = [False] * num_vertices

    #3. Iniciar DFS a partir do primeiro vértice
    dfs(0, adjacencia, visitados)

    #4. Verificar se todos os vértices foram visitados
    return all(visitados)