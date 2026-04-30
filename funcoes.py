import random

def rolar_dados(n):
    resultado = []
    for i in range(n):
        dado = random.randint(1,6)
        resultado.append(dado)
    return resultado

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    valor = dados_rolados.pop(dado_para_guardar)
    dados_no_estoque.append(valor)
    
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    valor = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(valor)
    
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):
    resultado = {}
    
    for numero in range(1, 7):
        quantidade = dados.count(numero)
        resultado[numero] = quantidade * numero
    
    return resultado

def calcula_pontos_soma(dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma

def calcula_pontos_sequencia_baixa(dados):
    sequencias = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    
    for seq in sequencias:
        encontrou = 0
        for num in seq:
            if num not in dados:
                encontrou += 1
                break
        if encontrou == 0:
            return 15
    
    return 0

def calcula_pontos_sequencia_alta(dados):
    sequencias = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]
    ]
    
    for seq in sequencias:
        encontrou = 0
        for num in seq:
            if num not in dados:
                encontrou += 1
                break
        if encontrou == 0:
            return 30
    
    return 0
    
def calcula_pontos_full_house(dados):
    for i in dados:
        if dados.count(i) == 3:
            for j in dados:
                if j != i and dados.count(j) == 2:
                    soma = 0
                    for x in dados:
                        soma += x
                    return soma
    return 0

def calcula_pontos_quadra(dados):
    contagem = {}
    
    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1
    
    for valor in contagem:
        if contagem[valor] >= 4:
            soma = 0
            for x in dados:
                soma += x
            return soma
    
    return 0

def calcula_pontos_quina(dados):
    contagem = {}
    
    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1
    
    for quantidade in contagem.values():
        if quantidade >= 5:
            return 50
    
    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados), 
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)