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
    
    if cliente_cadastrado == True:
        desenho.limpar_tela()
        desenho.titulo("CADASTRO DE CLIENTE")
        print("Cliente já cadastrado!")
        print("Deseja cadastrar de novo? (S/N)")
        validador = input("")
        validador = validador.strip().lower()

        while validador != "s" and validador != "n":
            print("Valor inválido!")
            print("Deseja cadastrar de novo? (S/N)")
            validador = input("")
            validador = validador.strip().lower()
        
        if validador == "s":
            cliente_cadastrado = False
        else:
            print("saindo. . .")
    
    if cliente_cadastrado == False:
        desenho.limpar_tela()
        desenho.titulo("CADASTRO DE CLIENTE")
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
        validador = input("Você tem alguma condição especial? (S/N)").strip().lower()
        
        while validador != "s" and validador != "n":
            print("Valor inválido!")
            validador = input("Você tem alguma condição especial? (S/N) ").strip().lower()
        
        if validador.strip().lower() == "s":
            condicao = input("Digite o nome dela: ")
        
        else:
            condicao = "Nenhuma"

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
        desenho.esperar()
        print("Usuario cadastrado...")
    
    desenho.esperar(1)


# ~~~~~~~~~ LOCALIZAÇÃO ~~~~~~~~~

localizacao_cadastrada = False

pais = ""
estado = ""
cidade = ""

def cadastrar_localizacao() -> None:
    global localizacao_cadastrada, pais, estado, cidade

    if localizacao_cadastrada == True:
        desenho.limpar_tela()
        desenho.titulo("CADASTRO DE LOCALIZAÇÃO")
        print("Localização já cadastrada!")
        print("Deseja cadastrar de novo? (S/N)")
        validador = input("")
        validador = validador.strip().lower()

        while validador != "s" and validador != "n":
            print("Valor inválido!")
            print("Deseja cadastrar de novo? (S/N)")
            validador = input("")
            validador = validador.strip().lower()
        
        if validador == "s":
            localizacao_cadastrada = False
        else:
            print("saindo. . .")
    
    if localizacao_cadastrada == False:
        desenho.limpar_tela()
        desenho.titulo("CADASTRO DE LOCALIZAÇÃO")
        print("\nCadastre sua localização atual\n")

        pais = input("País: ")
        estado = input("Estado: ")
        cidade = input("Cidade: ")

        localizacao_cadastrada = True
        print("Cadastrando Localização...")
        desenho.esperar()
        print("Localização Registrada...")

    desenho.esperar()


# ~~~~~~~~~ UV ~~~~~~~~~

uv_calculado = False
uv_atual = 0

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


def recomendacoes_protecao() -> None:
    desenho.titulo("RECOMENDAÇÕES DE PROTEÇÃO")

    if cliente_cadastrado == False:
        print("Cadastre seus dados pessoais antes de ver recomendações.")
        desenho.espera_entrada()
        return

    if localizacao_cadastrada == False:
        print("Cadastre sua localização antes de ver recomendações.")
        desenho.espera_entrada()
        return
    
    if uv_calculado == False:   
        print("Consulte o índice UV atual antes de ver recomendações.")
        desenho.espera_entrada()
        return    
    
    print(f"Índice UV atual em {cidade}: {uv_atual}")

    if uv_atual <= 2:
        print("Risco baixo. Use proteção básica se ficar muito tempo ao ar livre.")
    elif uv_atual <= 5:
        print("Risco moderado. Use protetor solar, óculos escuros e evite exposição prolongada.")
    elif uv_atual <= 7:
        print("Risco alto. Use protetor solar, boné/chapéu e procure sombra.")
    elif uv_atual <= 10:
        print("Risco muito alto. Evite sol forte entre 10h e 16h.")
    else:
        print("Risco extremo. Evite exposição direta e use proteção completa.")


# ~~~~~~~~~ DESCRIÇÃO ~~~~~~~~~

def mostra_descricao() -> None:
    desenho.titulo("DESCRIÇÃO DO PROJETO")
    print(f'''
A plataforma usa dados da NASA para proteger a saúde humana contra efeitos do Sol.
Ela monitora a radiação UV diária e alerta sobre tempestades solares.
O sistema considera localização e perfil do usuário para gerar recomendações.
Também informa riscos para grupos sensíveis, como cardíacos e pessoas com pele sensível.
A solução une saúde, tecnologia espacial e prevenção em uma única plataforma.
''')
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
            if localizacao_cadastrada == False:
                print("Cadastre uma localização antes de consultar o índice UV.")
                desenho.espera_entrada()
           
            else:
                desenho.linha(120)
                mostrar_grau_uv()
                desenho.linha(120)
                
                input("[ENTER] para calcular UV")
                
                uv_atual = calcular_uv()  
                uv_calculado = True

                print(f"Calculando UV da região de {cidade}...")
                desenho.esperar()
                risco_uv_usuario(uv_atual)
                desenho.espera_entrada()

        case "5":
            recomendacoes_protecao()
            
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


