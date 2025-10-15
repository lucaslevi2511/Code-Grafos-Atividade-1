# validacao/carregar_grafos.py

def carregar_grafo_do_documento(caminho_arquivo):

    try:
        with open(caminho_arquivo, 'r') as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"ERRO CRÍTICO: O arquivo em '{caminho_arquivo}' não foi encontrado.")
        return 0, []

    # Mapeamento de letras para números
    mapa_nos = {chr(ord('A') + i): i for i in range(26)}

    # Linha 1: Pega o número de vértices e arestas do conteúdo lido.
    num_vertices, _ = map(int, linhas[0].split())
    
    # Linhas seguintes: Pega as arestas no formato "XYW"
    arestas = []
    for linha in linhas[1:]:
        linha_limpa = linha.strip() 
        if not linha_limpa:
            continue

        u_char = linha_limpa[0]
        v_char = linha_limpa[1]
        peso_str = linha_limpa[2:]
        
        u = mapa_nos[u_char]
        v = mapa_nos[v_char]
        peso = int(peso_str)
        arestas.append((u, v, peso))
        
    return num_vertices, arestas