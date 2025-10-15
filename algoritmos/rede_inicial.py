#Função auxiliar para extrair a aresta de menor peso da fila de prioridade
def extrair_sub_rede_minima(fila_de_arestas):
    if not fila_de_arestas:
        return None
    indice_min = -1
    peso_min = float('inf')

    for i, (peso,_,_) in enumerate(fila_de_arestas):
        if peso < peso_min:
            peso_min = peso
            indice_min = i

    return fila_de_arestas.pop(indice_min)

def sub_rede_minima(num_vertices, arestas):
    if num_vertices == 0:
        return [], 0
    
    #1. Criar uma lista de adjacência para representar um grafo
    adjacencia = [[] for _ in range(num_vertices)]
    for u,v, peso in arestas:
        adjacencia[u].append((v, peso))
        adjacencia[v].append((u, peso))
    
    #2. Incializar a fila de prioridade e o conjunto de vértices visitados
    sub_rede_minima_arestas = []
    visitados = [False] * num_vertices
    fila_prioridade = []

    #3. Definir o vértice inicial
    vertice_inicial = 0
    visitados[vertice_inicial] = True
    for vizinho, peso in adjacencia[vertice_inicial]:
        fila_prioridade.append((peso, vertice_inicial, vizinho))
    
    #4. Loop principal do algoritmo de Prima
    while fila_prioridade and len(sub_rede_minima_arestas) < num_vertices - 1:
        peso, origem, destino = extrair_sub_rede_minima(fila_prioridade)

        if visitados[destino]:
            continue

        visitados[destino] = True

        sub_rede_minima_arestas.append((origem, destino, peso))

        for vizinho, peso in adjacencia[destino]:
            if not visitados[vizinho]:
                fila_prioridade.append((peso, destino, vizinho))

    #5. Calcular custo total da sub-rede mínima
    custo_total = sum(peso for _, _, peso in sub_rede_minima_arestas)

    return sub_rede_minima_arestas, custo_total
        