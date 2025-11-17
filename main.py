import random

print("------------------------------")
print("|        JOGO DA FORCA       |")
print("------------------------------\n")

print("Escolha um tema")
print("1 - Profissões")
print("2 - Objetos")
print("3 - Meios de transporte")
print("4 - Animais")
print("5 - Sair\n")

opcao = input("Escolha uma opção: ")

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

if opcao == "1":
        palavra = random.choice(temaProfissoes)
elif opcao == "2":
        palavra = random.choice(temaObjetosdia)
elif opcao == "3":
    palavra = random.choice(temaTransporte)
elif opcao == "4":
    palavra = random.choice(temaAnimais)
elif opcao == "5":
    print("Saindo...")
    exit()
else:
    print("Opção inválida!")
    exit()

print("\nPalavra selecionada! Vamos jogar!\n")

print("  _______")
print(" |/      |")
print(" | ")
print(" | ")
print(" | ")
print(" | ")
print(" |")
print("_|___ \n")

palavraUsuario = ["_"] * len(palavra)

print("Palavra:")
print(" ".join(palavraUsuario))
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

    # Tentar a palavra inteira
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

    # Tentar uma letra
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

    # Contar acertos
    acertos = 0
    for l in palavraUsuario:
        if l != "_":
            acertos += 1

    # Desenho da forca
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
    print(" ".join(palavraUsuario))
    print("Letras tentadas:", letrasTentadas)
    print(f"Erros: {erros}/4\n")

if acertos == len(palavra):
    print("Parabéns! Você venceu!")
else:
    print("Fim de jogo! A palavra era:", palavra)
