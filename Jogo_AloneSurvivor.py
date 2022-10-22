def mostrarCreditos():
    print("Um jogo feito por: Isaac e Andrei, alunos do Instituto Federal Campus Rio Pomba")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("{~{Pressione 'V' para voltar para o menu principal}~}")
    while True:
        voltar = input("(>)")
        if voltar == "V" or voltar == "v":
            mostrarMenu()
        else:
            print("{~{Resposta inválida}~}")
def sair():
    while True:
        print("{~{Deseja sair do Alone Survivor? (S/N)}~}")
        sair = input("(>)")
        if sair == "S" or sair == "s":
            break
        elif sair == "N" or sair == "n":
            mostrarMenu()
def mostrarMenu():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("////////////////////////////////////////////{~{Bem vindo(a) ao ALONE SURVIVOR!}~}/////////////////////////////////////////////")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("<1>Jogar<1>\n<2>Instruções<2>\n<3>História<3>\n<4>Opções<4>\n<5>Créditos<5>\n<6>Sair<6>")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("{~{Digite aqui a sua resposta}~}")
    escolha = int(input("(>)"))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    if escolha == 1:
        iniciarJogo()
    elif escolha == 2:
        mostrarInstrucoes()
    elif escolha == 3:
        mostrarHistoria()
    elif escolha == 4:
        mostrarOpcoes()
    elif escolha == 5:
        mostrarCreditos()
    elif escolha == 6:
        sair()
    else:
        print("{~{Resposta inválida}~}")
        mostrarMenu()
mostrarMenu()