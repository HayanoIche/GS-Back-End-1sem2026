import desenho
import random

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#               FUNÇÕES/PROCEDIMENTOS DO SISTEMA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~ CLIENTE ~~~~~~~~~

cliente_cadastrado = False

nome = ""
idade = 0
condicao = ""
cor = ""

def cadastrar_cliente() -> None:
    global cliente_cadastrado, nome, idade, condicao, cor

    desenho.titulo("CADASTRO DE CLIENTE")

    if cliente_cadastrado == True:
        print("Cliente já cadastrado!")
        print("Deseja cadastrar de novo? (S/N)")
        validador = input("")
        
        if validador.strip().lower() == "s":
            cliente_cadastrado = False
    
    if cliente_cadastrado == False:
        print("\nCadastre suas informações pessoais\n")

        # Nome
        nome = input("Nome: ")

        # Idade
        idade = input("Idade: ")

        # Validação da idade
        while True:
            if not idade.isnumeric():
                print("Idade inválida!")
                idade = input("Idade: ")
            else:
                idade = int(idade)

                if idade < 0 or idade > 100:
                    print("Idade inválida!")
                    idade = input("Idade: ")
                else:
                    break

        # Condicao
        validador = input("Você tem alguma condição especial? (S/N)")

        if validador.strip().lower() == "s":
            condicao = input("Digite o nome dela: ")

        # Cor da pele
        cores = ["branco", "pardo", "preto"]
        print("Qual o tom mais perto do tom da sua pele? (branco/pardo/preto)")
        cor = input("").lower().strip()

        while cor not in cores:
            print("Tom inválido!")
            print("Qual o tom mais perto do tom da sua pele? (branco/pardo/preto)")
            cor = input("").lower().strip()
        
        cliente_cadastrado = True
        print("Cadastrando Usuario...")
    
    desenho.esperar(1)


# ~~~~~~~~~ LOCALIZAÇÃO ~~~~~~~~~

localizacao_cadastrada = False

pais = ""
estado = ""
cidade = ""

def cadastrar_localizacao() -> None:
    desenho.titulo("CADASTRO DE LOCALIZAÇÃO")

    print("\nCadastre sua localização atual\n")

    pais = input("País: ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")

    localizacao_cadastrada = True


# ~~~~~~~~~ UV ~~~~~~~~~

def calcular_uv() -> int:
    uv = random.randint(0, 16)
    return uv


def mostrar_grau_uv():
    print('''0 a 2 (Baixo): Risco mínimo. Seguro para exposição ao ar livre.
3 a 5 (Moderado): Risco moderado. Requer o uso de óculos de sol e proteção caso fique exposto ao sol.
6 a 7 (Alto): Risco alto. Proteção é essencial; procure sombra durante o meio do dia e use chapéu e protetor solar.
8 a 10 (Muito Alto): Risco muito alto. Requer proteção redobrada, pois queimaduras podem ocorrer rapidamente. Evite o sol entre 10h e 16h.
11 ou mais (Extremamente Alto): Risco extremo. A exposição desprotegida pode causar queimaduras em poucos minutos. Proteção total obrigatória.''')


def risco_uv_usuario(uv):
    if uv <= 2:
        risco = "Risco mínimo"
    
    elif uv <= 5:
        risco = "Risco moderado"
    
    elif uv <= 7:
        risco = "Risco alto"
    
    elif uv <= 10:
        risco = "Risco muito alto"
    
    else: 
        risco = "Risco extremo"

    print(f"O UV atual da sua localização é {uv}, {risco}")

# ~~~~~~~~~ DESCRIÇÃO ~~~~~~~~~

def mostra_descricao() -> None:
    desenho.titulo("DESCRIÇÃO DO PROJETO")
    print(f"DESCRICAO")
    desenho.linha()
    desenho.espera_entrada()

# ~~~~~~~~~ MENU PRINCIPAL ~~~~~~~~~

def mostrar_menu_principal() -> None:
    desenho.limpar_tela()
    desenho.titulo("HELION HEALTH")

    print('''
1 - Descrição do projeto
2 - Cadastrar dados pessoais
3 - Cadastrar localização
4 - Índice UV atual
5 - Recomendações de proteção
6 - Informações sobre grupos de risco
0 - Sair
''')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       PROGRAMA PRINCIPAL                       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

desenho.limpar_tela()
desenho.titulo("BEM VINDO AO HELION HEALTH")
desenho.esperar(1.5)

while True:
    mostrar_menu_principal()

    opcao = input("Escolha: ")
    desenho.limpar_tela()

    match opcao:
        case "1":
            mostra_descricao()
        
        case "2":
            cadastrar_cliente()

        case "3":
            cadastrar_localizacao()

        case "4":
            desenho.linha(120)
            mostrar_grau_uv()
            desenho.linha(120)
            input("[ENTER] para Calcular UV")  
            calcular_uv()
            print(f"Calculando UV, da região de {cidade}...")
            desenho.esperar() 
            risco_uv_usuario(calcular_uv())
            desenho.espera_entrada()

        case "5":
            print()
        
        case "6":
            print()
        
        case "0":
            desenho.limpar_tela()
            desenho.titulo("HELION HEALTH")
            print("\nSaindo. . .\n")
            desenho.esperar(1)
            desenho.limpar_tela()
            break
        
        case _:
            desenho.limpar_tela()
            desenho.titulo("HELION HEALTH")
            print("\nDigite um valor válido!\n")
            desenho.esperar(1)
            desenho.limpar_tela()

# POSSIVEIS APIS:
#
# Open Street maps
# Google api
#


