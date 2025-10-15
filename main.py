from validacao.carregar_grafos import carregar_grafo_do_documento
from algoritmos.rede_inicial import sub_rede_minima
from algoritmos.otimizacao_rede import otimizar_rede
from algoritmos.verificar_conexao import verificar_conexao
from algoritmos.verificar_desconexao import verificar_desconexao_remocao

def executar_testes():
    print("Fazendo os testes:\n")

    try:
        num_v_g1, arestas_g1 = carregar_grafo_do_documento("entradas/grafo1.txt")
        num_v_g2, arestas_g2 = carregar_grafo_do_documento("entradas/grafo2.txt")
    except FileNotFoundError:
        print("Erro: arquivos de entrada não encontrados na pasta 'entradas'.")
        return

    def testar(funcao, nome, esperado_g1, esperado_g2):
        print(nome)
        for i, (n, a, esperado) in enumerate(
            [(num_v_g1, arestas_g1, esperado_g1), (num_v_g2, arestas_g2, esperado_g2)],
            start=1
        ):
            _, custo = funcao(n, a)
            resultado = "correto" if custo == esperado else "incorreto"
            print(f"Grafo {i}:\ncusto = {custo}\nesperado = {esperado}\n{resultado}\n")
        print()


    testar(sub_rede_minima, "Questão 2 - Projeto Inicial (AGM)", 18, 34)

    print("Questão 3 - Análise de Confiabilidade")
    

    resultado_3a = verificar_conexao(num_v_g1, arestas_g1)
    esperado_3a = True
    status_3a = "correto" if resultado_3a == esperado_3a else "incorreto"
    print(f"Grafo 1 (3.a - É conexo?):\nresultado = {resultado_3a}\nesperado = {esperado_3a}\n{status_3a}\n")


    aresta_teste = (2, 4, 2) 
    resultado_3b = verificar_desconexao_remocao(num_v_g1, arestas_g1, aresta_teste)
    esperado_3b = False
    status_3b = "correto" if resultado_3b == esperado_3b else "incorreto"
    print(f"Grafo 1 (3.b - Remoção de C-E desconecta?):\nresultado = {resultado_3b}\nesperado = {esperado_3b}\n{status_3b}\n")
    print()


    testar(otimizar_rede, "Questão 4 - Rede Otimizada", 27, 51)


if __name__ == "__main__":
    executar_testes()