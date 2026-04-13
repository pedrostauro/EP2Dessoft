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
    if (1 in dados and 2 in dados and 3 in dados and 4 in dados):
        return 15
    elif (2 in dados and 3 in dados and 4 in dados and 5 in dados):
        return 15
    elif (3 in dados and 4 in dados and 5 in dados and 6 in dados):
        return 15
    else:
        return 0
    
def calcula_pontos_sequencia_alta(dados):
    if (1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados):
        return 30
    elif (2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados):
        return 30
    else:
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