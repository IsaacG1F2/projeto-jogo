def iniciarJogo():
    print("nada")
    
#Como jogar
def mostrarInstrucoes():
    print("====================================================================================================================================")
#Título
    print("\n\n{~{AQUI ESTÃO ALGUMAS INSTRUÇÕES DE COMO JOGAR}~}\n")

#Instruções
    print("[§] No jogo você é o líder de um grupo de sobreviventes que luta para manter-se vivos a todo momento\n") 
    print("[§] O jogo é baseado em escolhas, aparecerão perguntas e dilemas que você deverá escolher uma resposta ou solução para resolvê-los\n")
    print("[§] Você tem algumas nescessidades básicas como saúde, fome ,sede ,radiação e stamina\n")
    print("[§] Você também possúi outras nescessidades não tão essenciais assim, como dinheiro, armas e relações com o seu grupo\n")
    print("[§] Como dito antes, você pode obter dinheiro no jogo para comprar armas para a sua equipe e outras coisas como edifícios para seu acampamento\n")
    print("[§] Você pode escolher comer ou beber alguma coisa a qualquer momento, mas saiba que isso afetará o evento que está acontecendo no momento\n")
    print("[§] Caso você morra durante o jogo você não poderá renascer a menos que você encontre um certo evento em específico que só ocorre durante o 10° turno\n")
    print("[§] Você poderá coletar recursos também para poder criar itens úteis que podem ajudar você e seu time a sobreviver\n")

#Voltar
    print("{~{VOLTAR PARA O MENU? (S/N)}~}")

#Variáveis
    voltar = input(">")
    
    if voltar == "S" or voltar == "s":
        mostrarMenu()

    elif voltar == "N" or voltar == "n":
        print("")

    else:
        print("{~{Resposta inválida}~}")
        mostrarInstrucoes()
        
#Mostrar história
def mostrarHistoria():
    print("====================================================================================================================================")
    print("{~{HISTÓRIA}~}\n\n")
    print("")

def mostrarOpcoes():
    print("nada")

