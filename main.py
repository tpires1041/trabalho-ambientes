import random

print("------------------------------")
print("|        JOGO DA FORCA       |")
print("------------------------------\n")

temaProfissoes = ["ADVOGADO", "PILOTO", "MEDICO", "ENGENHEIRO", "PROFESSOR", "PROGRAMADOR",
                  "ENFERMEIRO", "FARMACEUTICO", "ARQUITETO", "DESIGNER", "MOTORISTA",
                  "VENDEDOR", "GERENTE", "ARTISTA", "PSICOLOGO", "BIOLOGO", "QUIMICO",
                  "FISICO", "ATLETA", "ATENDENTE"]

temaObjetosdia = ["SOFA", "COPO", "TOALHA", "PRATO", "CHAVE", "PASTA",
                  "BOLSA", "ESPELHO", "GARRAFA", "TALHER", "CARREGADOR",
                  "POTE", "PERFUME"]

temaTransporte = ["CARRUAGEM", "CANOA", "BONDE", "TUKTUK", "BALAO", "CAMELO", "CAVALO",
                  "TELEFERICO", "SUBMARINO", "BALSA", "FOGUETE", "LAMBRETA", "PLANADOR"]

temaAnimais = ["CACHORRO", "GATO", "ELEFANTE", "TARTARUGA", "PATO", "ARARA", "MACACO",
               "GIRAFA", "TIGRE", "LEAO", "PANTERA"]

print("\nEscolha um tema")
print("1 - Profissões")
print("2 - Objetos")
print("3 - Meios de transporte")
print("4 - Animais")
print("5 - Sair\n")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    lista = temaProfissoes
elif opcao == "2":
    lista = temaObjetosdia
elif opcao == "3":
    lista = temaTransporte
elif opcao == "4":
    lista = temaAnimais
elif opcao == "5":
    print("Saindo...")
    exit()
else:
    print("Opção inválida!")
    exit()

for fase in range(1, 5):

    palavra = random.choice(lista)
    lista.remove(palavra)

    print(f"\n------------ FASE {fase} ------------\n")
    print("Palavra selecionada! Vamos jogar!\n")

    print("  _______")
    print(" |/      |")
    print(" | ")
    print(" | ")
    print(" | ")
    print(" | ")
    print(" |")
    print("_|___ \n")

    palavraUsuario = []
    for i in range(len(palavra)):
        palavraUsuario.append("_")

    print("Palavra:")
    for letra in palavraUsuario:
        print(letra, end=" ")
    print()

    print("\n")

    acertos = 0
    erros = 0
    letrasTentadas = []

    while acertos != len(palavra) and erros < 4:

        print("\nO que você deseja fazer?")
        print("1 - Tentar uma letra")
        print("2 - Tentar adivinhar a palavra inteira")

        escolha = input("Escolha 1 ou 2: ").strip()

        if escolha != "1" and escolha != "2":
            print("Opção inválida! Escolha 1 ou 2.\n")
            continue

        if escolha == "2":
            palpite = input("Digite a palavra completa: ").strip().upper()

            invalido = False
            for caractere in palpite:
                if caractere < "A" or caractere > "Z":
                    invalido = True

            if invalido:
                print("Entrada inválida! Use apenas letras sem acento.\n")
                continue

            if palpite == palavra:
                palavraUsuario = list(palavra)
                acertos = len(palavra)
                break
            else:
                print("Palpite errado!")
                erros += 1

        else:
            tentativa = input("Digite uma letra: ").strip().upper()

            if len(tentativa) == 0:
                continue

            letraTentativa = tentativa[0]

            if letraTentativa < "A" or letraTentativa > "Z":
                print("Entrada inválida! Use apenas letras sem acento.\n")
                continue

            if letraTentativa in letrasTentadas:
                print("Você já tentou essa letra!")
                continue

            letrasTentadas.append(letraTentativa)

            acertou = False
            for i in range(len(palavra)):
                if palavra[i] == letraTentativa:
                    palavraUsuario[i] = letraTentativa
                    acertou = True

            if acertou:
                print("Acertou!")
            else:
                print("Errou!")
                erros += 1

        acertos = 0
        for l in palavraUsuario:
            if l != "_":
                acertos += 1

        if erros == 1:
            print("  _______")
            print(" |/      |")
            print(" |      (_)") 
            print(" | ")
            print(" | ")
            print(" | ")
            print(" |")
            print("_|___ \n")
        elif erros == 2:
            print("  _______")
            print(" |/      |")
            print(" |      (_)") 
            print(" |      \\|/")
            print(" | ")
            print(" | ")
            print(" |")
            print("_|___ \n")
        elif erros == 3:
            print("  _______")
            print(" |/      |")
            print(" |      (_)") 
            print(" |      \\|/")
            print(" |       |")
            print(" | ")
            print(" |")
            print("_|___ \n")
        elif erros == 4:
            print("  _______")
            print(" |/      |")
            print(" |      (_)") 
            print(" |      \\|/")
            print(" |       |")
            print(" |      / \\")
            print(" |")
            print("_|___ \n")

        print("Palavra Atual:")
        for letra in palavraUsuario:
            print(letra, end=" ")
        print()

        print("Letras tentadas:", letrasTentadas)
        print(f"Erros: {erros}/4\n")

    if acertos == len(palavra):
        print("Parabéns! Você venceu a fase", fase)
    else:
        print("Fim de jogo! A palavra era:", palavra)
        print("Você perdeu na fase", fase)
        exit()

print("Parabéns! Você passou por todas as fases!")
