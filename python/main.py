import os

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

# Programa principal
desenhar_titulo("pipi popo")


