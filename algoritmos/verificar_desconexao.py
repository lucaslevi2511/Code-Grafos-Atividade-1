from .verificar_conexao import verificar_conexao

def verificar_desconexao_remocao(num_vertices, arestas, aresta_a_remover):
    
    #1. Desempacotar a aresta a ser removida para obter seus vértices
    u_rem, v_rem, _ = aresta_a_remover
    
    #2. Criar uma nova lista de arestas que não contém a aresta removida
    arestas_modificadas = []
    for u, v, p in arestas:
        if not ((u == u_rem and v == v_rem) or (u == v_rem and v == u_rem)):
            arestas_modificadas.append((u, v, p))
            
    #3. Verificar a conectividade da rede já modificada (sem a aresta)
    rede_ainda_conexa = verificar_conexao(num_vertices, arestas_modificadas)
    
    return not rede_ainda_conexa