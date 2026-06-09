# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#       Biblioteca para desenhos formatados no terminal
#        desenvolvida por Matheus Vidal e Igor Hayano
# 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import time

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           DESENHOS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Função que desenha uma linha no terminal
# O parametro Tam é o tamanho da linha em caracteres "~"
def linha(tam: int = 80) -> None:
    print("~" * tam)


# Função que desenha como se fosse um título
def titulo(titulo: str) -> None:
    linha()
    print(f"{titulo.upper():^80}")
    linha()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                     OUTRAS FUNCIONALIDADES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def limpar_tela():
    os.system("cls")


def espera_entrada() -> None:
    print("")
    input("APERTE [ENTER] PARA CONTINUAR. . .")

