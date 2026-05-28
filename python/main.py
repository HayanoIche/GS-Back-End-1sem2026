"""
OPÇÕES DO MENU:

1 - Descrição do projeto
2 - Cadastrar localização
3 - Índice UV atual
4 - Recomendações de proteção
5 - Dados Históricos
6 - Informações sobre grupos de risco
0 - Sair
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#               FUNÇÕES/PROCEDIMENTOS DE "DESENHO"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def desenhar_linha(tam: int = 30) -> None:
    print("~" * tam)

def desenhar_titulo(titulo: str) -> None:
    desenhar_linha()
    print(f"{titulo.upper():^30}")
    desenhar_linha()


# Programa principal
desenhar_titulo("pipi popo")


