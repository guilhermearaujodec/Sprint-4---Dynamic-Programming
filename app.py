import time
from typing import List, Dict, Tuple, Optional

# Constante para representar o infinito
INF = float('inf')

# Variável global para armazenar o estado da pipeline (usada pelo menu)
current_P: List[int] = []

# -----------------------------------------------------
# FUNÇÕES DE INPUT E VALIDAÇÃO
# -----------------------------------------------------

def get_pipeline_complexities() -> Optional[List[int]]:
    """
    Função para receber e validar as complexidades de I/O da pipeline do usuário.
    """
    print("\n--- Definição da Pipeline ---")
    
    # 1. Obter N (Número de etapas de análise)
    N_steps = 0
    while True:
        try:
            N_input = input("Informe o número de ETAPAS de análise (N >= 2): ")
            N_steps = int(N_input)
            if N_steps < 2:
                print("❌ ERRO: O número de etapas deve ser no mínimo 2. Tente novamente.")
            else:
                break
        except ValueError:
            print("❌ ERRO: Por favor, insira um número inteiro para as etapas.")
    
    # Precisamos de N+1 complexidades (P0 a PN)
    P_count = N_steps + 1
    print(f"\nAgora, informe as {P_count} complexidades de I/O (P0 a P{N_steps}).")
    print("Estas complexidades simulam as dimensões dos dados entre as etapas.")
    
    P_list = []
    for i in range(P_count):
        while True:
            try:
                # Solicita P[i]
                p_val_input = input(f"Complexidade P[{i}] (Tamanho, Ex: 10, 20...): ")
                p_val = int(p_val_input)
                # Teste/Validação: Complexidade deve ser positiva
                if p_val <= 0:
                    print("❌ ERRO: O valor da complexidade deve ser um número inteiro positivo. Tente novamente.")
                else:
                    P_list.append(p_val)
                    break
            except ValueError:
                print("❌ ERRO: Por favor, insira um número inteiro positivo.")

    # Teste de Coerência: Garante que a lista final tem o tamanho correto
    if len(P_list) == P_count:
        print("\n✅ Pipeline definida com sucesso!")
        return P_list
    else:
        # Caso de falha inesperada na coleta
        print("\n❌ ERRO FATAL: Falha na coleta de complexidades.")
        return None


# -----------------------------------------------------
# VERSÃO RECURSIVA SIMPLES (Para fins de comparação)
# -----------------------------------------------------

def custo_recursivo_simples(i: int, j: int, P: List[int]) -> int:
    """
    Calcula o custo mínimo da sequência i a j (recursão pura).
    Esta versão é exponencial (O(2^n)) e muito lenta para N grande.
    """
    if i == j:
        return 0

    min_custo = INF

    for k in range(i, j):
        # Custo = Módulo [i, k] + Módulo [k+1, j] + Custo de Interligação (P[i-1] * P[k] * P[j])
        custo_atual = (custo_recursivo_simples(i, k, P) +
                       custo_recursivo_simples(k + 1, j, P) +
                       P[i - 1] * P[k] * P[j])
        min_custo = min(min_custo, custo_atual)

    return min_custo

# -----------------------------------------------------
# VERSÃO RECURSIVA COM MEMOIZAÇÃO (TOP-DOWN)
# -----------------------------------------------------

# Nota: O cache (memo) é passado como argumento e inicializado fora da função.
def custo_recursivo_memoizado(i: int, j: int, P: List[int], memo: Dict[Tuple[int, int], int]) -> int:
    """
    Calcula o custo mínimo da sequência i a j usando memoização.
    Complexidade: O(n^3).
    """
    # Caso Base
    if i == j:
        return 0

    # Lookup de Memoização: Se o estado já foi calculado, retorna o valor.
    if (i, j) in memo:
        return memo[(i, j)]

    min_custo = INF

    # Decisão: Tenta todas as divisões possíveis no ponto k
    for k in range(i, j):
        # Custo = DP[i][k] + DP[k+1][j] + Custo de Interligação
        custo_atual = (custo_recursivo_memoizado(i, k, P, memo) +
                       custo_recursivo_memoizado(k + 1, j, P, memo) +
                       P[i - 1] * P[k] * P[j])
        min_custo = min(min_custo, custo_atual)

    # Armazena o resultado no cache (memoização)
    memo[(i, j)] = min_custo
    return min_custo

# -----------------------------------------------------
# VERSÃO ITERATIVA (BOTTOM-UP)
# -----------------------------------------------------

def custo_iterativo_bottom_up(P: List[int]) -> int:
    """
    Calcula o custo mínimo da sequência usando a abordagem iterativa (Tabulação).
    Complexidade: O(n^3).
    """
    num_etapas = len(P) - 1
    # Tabela DP: dp[i][j] armazena o custo mínimo para o módulo i a j.
    # Inicializada com zeros.
    dp = [[0 for _ in range(num_etapas + 1)] for _ in range(num_etapas + 1)]

    # O 'L' representa o comprimento (length) da sub-cadeia (módulo) sendo calculada
    for L in range(2, num_etapas + 1):
        # 'i' é o ponto inicial da sub-cadeia
        for i in range(1, num_etapas - L + 2):
            # 'j' é o ponto final da sub-cadeia
            j = i + L - 1
            dp[i][j] = INF

            # Decisão: Tenta todas as divisões possíveis no ponto k
            for k in range(i, j):
                # Custo = DP[i][k] + DP[k+1][j] + Custo de Interligação
                custo_interligacao = P[i - 1] * P[k] * P[j]
                custo_atual = dp[i][k] + dp[k + 1][j] + custo_interligacao
                dp[i][j] = min(dp[i][j], custo_atual)

    # O resultado final está no canto superior direito (Módulo 1 até N)
    return dp[1][num_etapas]

# -----------------------------------------------------
# VERIFICAÇÃO E EXECUÇÃO
# -----------------------------------------------------

def verificar_e_executar_dp(P: List[int]):
    """
    Executa as duas versões de DP e verifica a coerência dos resultados.
    """
    if not P or len(P) < 2:
        print("\nERRO: Pipeline não definida ou inválida. Defina as complexidades primeiro (Opção 1).")
        return

    N = len(P) - 1 # Número de etapas de análise
    
    print("\n" + "-" * 70)
    print("--- Otimizador de Pipeline de Visão Computacional (DP) ---")
    print(f"Número de Etapas de Análise (N): {N}")
    print(f"Complexidades de I/O (P): {P}")
    print("-" * 70)

    # 1. Versão Recursiva com Memoização (Top-Down)
    memo = {}
    start_time = time.perf_counter()
    resultado_memo = custo_recursivo_memoizado(1, N, P, memo)
    end_time = time.perf_counter()
    time_memo = (end_time - start_time) * 1000

    print(f"[1] Custo Mínimo (Memoização - Top-Down): {resultado_memo}")
    print(f"Tempo de execução: {time_memo:.4f} ms")


    # 2. Versão Iterativa (Bottom-Up)
    start_time = time.perf_counter()
    resultado_iter = custo_iterativo_bottom_up(P)
    end_time = time.perf_counter()
    time_iter = (end_time - start_time) * 1000

    print(f"[2] Custo Mínimo (Iterativa - Bottom-Up): {resultado_iter}")
    print(f"Tempo de execução: {time_iter:.4f} ms")

    # Verificação de Coerência
    print("\n" + "=" * 70)
    if resultado_memo == resultado_iter:
        print("✅ COERÊNCIA VERIFICADA: As duas abordagens de DP produziram o mesmo resultado.")
    else:
        print("❌ ERRO: Resultados diferentes entre as abordagens!")
    print("=" * 70)

# -----------------------------------------------------
# INTERFACE DO USUÁRIO (MENU)
# -----------------------------------------------------

def main_menu():
    """Menu principal para interação do usuário."""
    global current_P

    while True:
        print("\n" + "=" * 60)
        print("OTIMIZADOR DE PIPELINE DE VISÃO COMPUTACIONAL DASA")
        print("=" * 60)
        
        # Exibe o status atual da pipeline
        if current_P:
            print(f"Status Atual: {len(current_P) - 1} Etapas definidas | Complexidades: {current_P}")
        else:
            print("Status Atual: Nenhuma Pipeline definida.")
        
        print("\n[1] Definir Complexidades da Pipeline (Input)")
        print("[2] Executar Otimização (Programação Dinâmica)")
        print("[3] Sair")
        
        choice = input("\nEscolha uma opção: ")
        
        if choice == '1':
            new_P = get_pipeline_complexities()
            if new_P:
                current_P = new_P
        elif choice == '2':
            if current_P:
                verificar_e_executar_dp(current_P)
            else:
                print("\n⚠️ Por favor, defina a pipeline primeiro (Opção 1) antes de executar.")
        elif choice == '3':
            print("\nEncerrando o otimizador. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    # Remove a execução automática e inicia o menu
    main_menu()