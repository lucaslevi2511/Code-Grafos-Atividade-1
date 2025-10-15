from .rede_inicial import sub_rede_minima
from .verificar_conexao import dfs as dfs_para_componentes
from .verificar_desconexao import verificar_desconexao_remocao

def otimizar_rede(num_vertices, arestas_originais):
    # 1. Iniciar com a AGM (rede de custo mínimo).
    rede_final_arestas, _ = sub_rede_minima(num_vertices, arestas_originais)
    conjunto_rede_final = {tuple(sorted((u, v))) for u, v, _ in rede_final_arestas}

    # 2. Laço para encontrar e reforçar pontes até a rede ser confiável.
    while True:
        # Encontra uma ponte na rede atual.
        ponte_encontrada = None
        for aresta_teste in rede_final_arestas:
            if verificar_desconexao_remocao(num_vertices, rede_final_arestas, aresta_teste):
                ponte_encontrada = aresta_teste
                break

        # Se não houver mais pontes, a rede é confiável.
        if ponte_encontrada is None:
            break

        # Divide o grafo em dois componentes com base na ponte encontrada.
        u_ponte, v_ponte, _ = ponte_encontrada
        adj_sem_ponte = [[] for _ in range(num_vertices)]
        for u, v, _ in rede_final_arestas:
            if not ((u == u_ponte and v == v_ponte) or (u == v_ponte and v == u_ponte)):
                adj_sem_ponte[u].append(v)
                adj_sem_ponte[v].append(u)
        visitados_componente = [False] * num_vertices
        dfs_para_componentes(u_ponte, adj_sem_ponte, visitados_componente)

        # Procura a aresta de reforço mais barata entre os componentes.
        reforco_candidato = None
        peso_min = float('inf')
        for u_orig, v_orig, peso_orig in arestas_originais:
            aresta_ord = tuple(sorted((u_orig, v_orig)))
            if aresta_ord in conjunto_rede_final:
                continue
            if visitados_componente[u_orig] != visitados_componente[v_orig]:
                if peso_orig < peso_min:
                    peso_min = peso_orig
                    reforco_candidato = (u_orig, v_orig, peso_orig)

        # Adiciona o reforço à rede.
        if reforco_candidato:
            rede_final_arestas.append(reforco_candidato)
            u_r, v_r, _ = reforco_candidato
            conjunto_rede_final.add(tuple(sorted((u_r, v_r))))
        else: 
            break

    # 3. Calcular e retornar o custo total do grafo final.
    custo_final = sum(peso for _, _, peso in rede_final_arestas)
    
    return rede_final_arestas, custo_final