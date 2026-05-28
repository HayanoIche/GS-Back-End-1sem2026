import desenho
import random

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#               FUNÇÕES/PROCEDIMENTOS DO SISTEMA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def cadastrar_localizacao() -> None:
    desenho.titulo("CADASTRO DE LOCALIZAÇÃO")
    print("Cadastre sua localização atual para usar\nas funcionalidades do sistema")
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


def mostra_descricao() -> None:
    desenho.titulo("DESCRIÇÃO DO PROJETO")
    print(f"DESCRICAO")
    desenho.linha()


def menu_principal() -> None:
    desenho.limpar_tela()
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
                mostra_descricao()
            
            case "2":
                cadastrar_localizacao()
            
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       PROGRAMA PRINCIPAL                       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# POSSIVEIS APIS:
#
# Open Street maps
# Google api
#


