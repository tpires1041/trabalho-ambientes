import random

print("===============================")
print("          JOGO DA FORCA")
print("===============================\n")

print("Escolha um tema")
print("1 - Profissões")
print("2 - Objetos")
print("3 - Meios de transporte")
print("4 - ")
print("5 - Sair\n")

opcao = input("Escolha uma opção: ")

temaProfissoes = ["ADVOGADO", "PILOTO", "MEDICO", "ENGENHEIRO", "PROFESSOR", "PROGRAMADOR", "ENFERMEIRO", "FARMACEUTICO", "ARQUITETO", "DESIGNER", "MOTORISTA", "VENDEDOR", "GERENTE", "ARTISTA", "PSICOLOGO", "BIOLOGO", "QUIMICO", "FISICO", "ATLETA", "ATENDENTE"]

temaObjetosdia = ["SOFA", "COPO", "TOALHA", "PRATO", "CHAVE", "PASTA",
        "BOLSA", "ESPELHO", "GARRAFA", "TALHER", "CARREGADOR",
        "POTE", "PERFUME"]
        
temaTransporte = ["CARRUAGEM", "CANOA", "BONDE", "TUK-TUK", "BALAO", "CAMELO", "CAVALO", "TELEFERICO", "SUBMARINO", "BALSA", "FOGUETE", "LAMBRETA", "PLANADOR"]

if opcao == "1":
    palavra = random.choice(temaProfissoes)

elif opcao == "2":
    palavra = random.choice(temaObjetosdia)

elif opcao == "3":
    palavra = random.choice(temaTransporte)

print("\nTema selecionado! Vamos jogar!\n")

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

print("Palavra:\n")
for letra in palavraUsuario:
    print(letra, end=" ")
print("\n")

acertos = 0    
erros = 0
letrasTentadas = []

while acertos != len(palavra) and erros < 4:

    tentativa = input("Digite uma letra: ")

    if tentativa == "" or tentativa == " ":
        continue

    letraTentativa = tentativa[0]
    letraTentativa = letraTentativa.upper()

    if letraTentativa in letrasTentadas:
        print("Você já tentou a letra", letraTentativa)
        continue
            
    letrasTentadas.append(letraTentativa)
        
    acertouNaRodada = False
        
    i = 0
    while i < len(palavra):
        if letraTentativa == palavra[i]:
            palavraUsuario[i] = palavra[i]
            acertouNaRodada = True
        i = i + 1
        
    if acertouNaRodada == True:
        print("Acertou!")
        acertos = 0
        for letra in palavraUsuario:
            if letra != "_":
                acertos = acertos + 1
    else:
        erros = erros + 1
        print("Errou!")
            
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
        print(" |")
        print(" |")
        print(" |")
        print("_|___ \n")
    elif erros == 3:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |")
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

    print("\nPalavra Atual:")
    for letra in palavraUsuario:
        print(letra, end=" ")
    print()
    print("Erros:", erros, "/4. Letras Tentadas:", letrasTentadas)

if acertos == len(palavra):
    print("\nParabéns! Você venceu!")
else:
    print("\nFim de jogo! A palavra era:", palavra)