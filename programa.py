from funcoes import *

cartela = {
    'regra_simples': {},
    'regra_avancada': {}
}

for i in range(1, 7):
    cartela['regra_simples'][i] = -1

cartela['regra_avancada']['sem_combinacao'] = -1
cartela['regra_avancada']['quadra'] = -1
cartela['regra_avancada']['full_house'] = -1
cartela['regra_avancada']['sequencia_baixa'] = -1
cartela['regra_avancada']['sequencia_alta'] = -1
cartela['regra_avancada']['cinco_iguais'] = -1


for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print("Dados rolados:", dados_rolados)
        print("Dados guardados:", dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if indice < len(dados_rolados):
                guardar_dado(dados_rolados, dados_guardados, indice)

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if indice < len(dados_guardados):
                remover_dado(dados_rolados, dados_guardados, indice)

        elif opcao == '3':
            if rerrolagens < 2:
                quantidade = 5 - len(dados_guardados)
                dados_rolados = rolar_dados(quantidade)
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            print("Digite a combinação desejada:")
            combinacao = input()

            todos_dados = dados_rolados + dados_guardados

            valido = False
            for i in range(1, 7):
                if combinacao == str(i):
                    valido = True

                    if cartela['regra_simples'][i] == -1:
                        pontos = calcula_pontos_regra_simples(todos_dados)
                        cartela['regra_simples'][i] = pontos[i]
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                        break

            if not valido:
                if combinacao in cartela['regra_avancada']:
                    if cartela['regra_avancada'][combinacao] == -1:
                        pontos = calcula_pontos_regra_avancada(todos_dados)
                        cartela['regra_avancada'][combinacao] = pontos[combinacao]
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")


total = 0

soma_simples = 0
for i in range(1, 7):
    total += cartela['regra_simples'][i]
    soma_simples += cartela['regra_simples'][i]

for chave in cartela['regra_avancada']:
    total += cartela['regra_avancada'][chave]

if soma_simples >= 63:
    total += 35

imprime_cartela(cartela)
print("Pontuação total:", total)