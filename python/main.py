import os
import random

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#               FUNÇÕES/PROCEDIMENTOS DE "DESENHO"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def desenhar_linha(tam: int = 30) -> None:
    print("~" * tam)


def desenhar_titulo(titulo: str) -> None:
    desenhar_linha()
    print(f"{titulo.upper():^30}")
    desenhar_linha()


def menu_principal() -> None:
    os.system("cls")
    print('''OPÇÕES DO MENU:
1 - Descrição do projeto
2 - Cadastrar localização
3 - Índice UV atual
4 - Recomendações de proteção
5 - Dados Históricos
6 - Informações sobre grupos de risco
0 - Sair''')
    
    while True:
        opcao = input("Escolha: ")
        match opcao:
            case "1":
                print()
            
            case "2":
                print()
            
            case "3":
                print()
            
            case "4":
                print()
            
            case "5":
                print()
            
            case "6":
                print()
            
            case "0":
                print()
           
            case _:
                print()


def cadastrar_localizacao() -> None:
    bairro = input("Bairro: ")
    cidade = input("Cidade")
    rua = input("Rua: ")
    numero = input("Número: ")
        

def calcular_uv() -> int:
    uv = random.randint(0, 16)
    return uv


def mostrar_grau_uv(uv):
    print('''0 a 2 (Baixo): Risco mínimo. Seguro para exposição ao ar livre.
3 a 5 (Moderado): Risco moderado. Requer o uso de óculos de sol e proteção caso fique exposto ao sol.
6 a 7 (Alto): Risco alto. Proteção é essencial; procure sombra durante o meio do dia e use chapéu e protetor solar.
8 a 10 (Muito Alto): Risco muito alto. Requer proteção redobrada, pois queimaduras podem ocorrer rapidamente. Evite o sol entre 10h e 16h.
11 ou mais (Extremamente Alto): Risco extremo. A exposição desprotegida pode causar queimaduras em poucos minutos. Proteção total obrigatória.''')
    
    if uv >= 2:
        risco = "Risco mínimo"
    
    elif uv >= 5:
        risco = "Risco moderado"
    
    elif uv >= 7:
        risco = "Risco alto"
    
    elif uv >= 10:
        risco = "Risco muito alto"
    
    else: 
        risco = "Risco extremo"

    print(f"O UV atual da sua localização é {uv}, {risco}")



# Programa principal
desenhar_titulo("pipi popo")


