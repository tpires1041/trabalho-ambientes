import random

print("===============================")
print("          JOGO DA FORCA")
print("===============================\n")

print("1 - Jogar")
print("2 - Selecionar um tema")
print("3 - Sair\n")

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

print("Palavra:\n")
print(" ".join(palavraUsuario))
print("\n")

acertos = 0    
erros = 0
letrasTentadas = []

while acertos != len(palavra) and erros < 4:

    tentativa = input("Digite uma letra: ").strip()

    if tentativa == "":
        continue

    letraTentativa = tentativa[0].upper()

    if letraTentativa in letrasTentadas:
        print(f"Você já tentou a letra '{letraTentativa}'.")
        continue
            
    letrasTentadas.append(letraTentativa)
        
    acertouNaRodada = False
        
    for i in range(len(palavra)):
        if letraTentativa == palavra[i]:
            palavraUsuario[i] = palavra[i]
            acertouNaRodada = True
        
    if acertouNaRodada:
        print("Acertou!")
        acertos = palavraUsuario.count("_") ^ len(palavra)  # só para atualizar
        acertos = len([l for l in palavraUsuario if l != "_"])
    else:
        erros += 1
        print("Errou!")
            
    if(erros == 1):
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" | ")
        print(" | ")
        print(" | ")
        print(" |")
        print("_|___ \n")
    elif(erros == 2):
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |     ")
        print(" |     ")
        print(" |")
        print("_|___ \n")
    elif(erros == 3):
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |     ")
        print(" |")
        print("_|___ \n")
    elif(erros == 4):
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |      / \\")
        print(" |")
        print("_|___ \n")

    print("\nPalavra Atual:")
    print(" ".join(palavraUsuario))
    print(f"\nErros: {erros}/4. Letras Tentadas: {letrasTentadas}")

if acertos == len(palavra):
    print("\nParabéns! Você venceu!")
else:
    print(f"\nFim de jogo! A palavra era: {palavra}")





   



    


    




   



    


    
