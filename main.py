print("===============================")
print("          JOGO DA FORCA")
print("===============================\n")

print("1 - Jogar")
print("2 - Selecionar dificuldade")
print("3 - Sair\n")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    
    palavra = "TESTE"
    
    print("  _______")
    print(" |/      |")
    print(" |      (_)")
    print(" |      \|/")
    print(" |       |")
    print(" |      / \\")
    print(" |")
    print("_|___ \n")
    
    palavraUsuario = []
    
    for i in range(0, len(palavra)):
        palavraUsuario.append("_")
    
    print("Palavra:\n")
    print(" ".join(palavraUsuario))
    print("\n")
    
    acertos = 0    
    erros = 0
    letrasTentadas = []
    
    while(acertos != len(palavra) and erros < 4):
        
        tentativa = input("Digite uma letra: ").strip()
            
        letraTentativa = tentativa[0].upper()
        
        if letraTentativa in letrasTentadas:
            print(f"Você já tentou a letra '{letraTentativa}'.")
            continue
            
        letrasTentadas.append(letraTentativa)
        
        acertouNaRodada = False
        
        for i in range(0, len(palavra)):
            if(letraTentativa == palavra[i]):
                palavraUsuario[i] = palavra[i]
                acertouNaRodada = True
        
        if acertouNaRodada:
            print("Acertou!")
            acertos = 0
            for letra in palavraUsuario:
                if letra != '_':
                    acertos += 1
        else:
            erros += 1
            print("Errou!")
            
        if(erros == 1):
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |     ")
            print(" |")
            print("_|___ \n")
        elif(erros == 2):
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |     ")
            print(" |     ")
            print(" |")
            print("_|___ \n")
        elif(erros == 3):
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |     ")
            print(" |     ")
            print(" |     ")
            print(" |")
            print("_|___ \n")
        elif(erros == 4):
            print("  _______")
            print(" |/      |")
            print(" |     ")
            print(" |     ")
            print(" |     ")
            print(" |     ")
            print(" |")
            print("_|___ \n")


        
        print("\nPalavra Atual:")
        print(" ".join(palavraUsuario))
        print(f"\nErros: {erros}/4. Letras Tentadas: {letrasTentadas}")
        
    if acertos == len(palavra):
        print("\nParabéns! Você venceu!")
    else:
        print(f"\nFim de jogo! A palavra era: {palavra}")

###------------------------------- 
# Maria:
# Tema: objetos do dia a dia
palavras = ["sofa", "copo", "toalha", "prato", "chave", "pasta","bolsa","espelho", "garrafa", "talher", "carregador", "pote", "perfume"]

print("Digite um número de 0 a", len(palavras)-1, "para sortear a palavra:")
num = int(input("Número: "))


palavra = palavras[num]

forca = [
    """
     _______
    |/      |
    |
    |
    |
    |
    |_____
    """,

    """
     _______
    |/      |
    |      ( )
    |
    |
    |
    |_____
    """,

    """
     _______
    |/      |
    |      ( )
    |       |
    |
    |
    |_____
    """,

    """
     _______
    |/      |
    |      ( )
    |      \\|
    |
    |
    |_____
    """,

    """
     _______
    |/      |
    |      ( )
    |      \\|/
    |
    |
    |_____
    """,

    """
     _______
    |/      |
    |      ( )
    |      \\|/
    |       |
    |
    |_____
    """,

    """
     _______
    |/      |
    |      ( )
    |      \\|/
    |       |
    |      / \\
    |_____
    """
]

letras_certas = []
letras_erradas = []
erros = 0
limite_erros = len(forca) - 1

print("💡 Dica: É um objeto que utilizamos no dia a dia.")

while erros < limite_erros:
    print(forca[erros])

    exibicao = ""
    for letra in palavra:
        if letra in letras_certas:
            exibicao +=  " " 
        else:
            exibicao += "_ "

    print("\nPalavra:", exibicao)
    print("Letras erradas:", ", ".join(letras_erradas))

    if "_" not in exibicao:
        print("\n✨ Parabéns! Você acertou a palavra:", palavra, "!")
        break

    palpite = input("\nDigite uma letra: ").lower()

    
    if len(palpite) != 1 or not palpite.isalpha():
        print("Digite apenas UMA letra válida!")
        continue

    
    if len(palpite) != 1 or palpite < "a" or palpite > "z":
        letras_certas.append(palpite)
        print("✔️ Boa! A letra está na palavra.")

    
    elif palpite in letras_certas or palpite in letras_erradas:
        print("Você já tentou essa letra!")

    
    else:
        erros += 1
        letras_erradas.append(palpite)
        print("❌ Letra incorreta!" )


if erros == limite_erros:
    print(forca[erros])
    print("\n💀 Você perdeu! A palavra era:" , palavra)
