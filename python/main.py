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
historico_localizacoes = []

pais = ""
estado = ""
cidade = ""

def consultar_historico() -> None:
    desenho.titulo("HISTÓRICO DE LOCALIZAÇÕES")

    if len(historico_localizacoes) == 0:
        print("Nenhuma localização foi registrada ainda.")
        desenho.espera_entrada()
        return

    for indice, registro in enumerate(historico_localizacoes, start=1):
        print(f"{indice}. {registro[2]} - {registro[1]} - {registro[0]}")
        print(f"   Índice UV: {registro[3]}")
        print(f"   Índice KP: {registro[4]}")
        desenho.linha()

    desenho.espera_entrada()


def salvar_historico_localizacao() -> None:
    registro = [pais, estado, cidade, uv_atual, "Não calculado"]

    historico_localizacoes.append(registro)


def cadastrar_localizacao() -> None:
    global localizacao_cadastrada, pais, estado, cidade, uv_calculado, uv_atual

    if localizacao_cadastrada == True:
        desenho.limpar_tela()
        desenho.titulo("CADASTRO DE LOCALIZAÇÃO")
        print("Já existe uma localização cadastrada")
        print("Deseja cadastrar outra região? (S/N)")
        validador = input("")
        validador = validador.strip().lower()

        while validador != "s" and validador != "n":
            print("Valor inválido!")
            print("Deseja cadastrar outra região? (S/N)")
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
        uv_atual = calcular_uv()  
        uv_calculado = True
        salvar_historico_localizacao()

        print("Cadastrando Localização...")
        desenho.esperar(1)
        print("Localização Cadastrada...")
        desenho.esperar()
        print(f"Calculando UV de {cidade}...")        
        desenho.esperar()
        print("UV Cadastrado...")
        desenho.espera_entrada()

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


def classificar_uv(uv: int) -> str:
    if uv <= 2:
        return "Risco baixo"
    
    elif uv <= 5:
        return "Risco moderado"
    
    elif uv <= 7:
        return "Risco alto"
    
    elif uv <= 10:
        return "Risco muito alto"
    
    else:
        return "Risco extremo"


def recomendacoes_protecao() -> None:
    desenho.titulo("RECOMENDAÇÕES DE PROTEÇÃO")
    print()
    if cliente_cadastrado == False:
        print("Cadastre seus dados pessoais antes de ver recomendações.")
        return

    if localizacao_cadastrada == False:
        print("Cadastre sua localização antes de ver recomendações.")
        return
    
    if uv_calculado == False:   
        print("Consulte o índice UV atual antes de ver recomendações.")
        return    
    
    mostrar_grau_uv()
    print()
    desenho.linha()
    print()
    print(f"Índice UV atual em {cidade}: {uv_atual}")

    risco = classificar_uv(uv_atual)
    print(f"Classificação: {risco}")

    if uv_atual <= 2:
        print("Recomendação: Use proteção básica caso fique muito tempo ao ar livre.")

    elif uv_atual <= 5:
        print("Recomendação: Use protetor solar, óculos escuros e evite exposição prolongada.")

    elif uv_atual <= 7:
        print("Recomendação: Use protetor solar, boné ou chapéu e procure sombra.")

    elif uv_atual <= 10:
        print("Recomendação: Evite o sol forte entre 10h e 16h e use proteção reforçada.")

    else:
        print("Recomendação: Evite exposição direta e use proteção completa.")

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

# ~~~~~~~~~ INDICE KP ~~~~~~~~~

kp_calculado = False
kp_atual = 0

def calcular_kp() -> int:
    return random.randint(0, 9)


def classificar_kp(kp: int) -> str:
    if kp <= 3:
        return "atividade geomagnética baixa"
    
    elif kp <= 5:
        return "atividade geomagnética moderada"
    
    elif kp <= 7:
        return "tempestade geomagnética forte"
    
    else:
        return "tempestade geomagnética severa"


def analisar_kp(kp: int) -> None:
    risco = classificar_kp(kp)

    if kp <= 3:
        recomendacao = "Sem risco relevante para a maioria das pessoas."

    elif kp <= 5:
        recomendacao = "Pessoas sensíveis devem ficar atentas a sintomas e evitar esforço excessivo."

    elif kp <= 7:
        recomendacao = "Recomenda-se atenção para pessoas com problemas cardíacos ou neurológicos."
        
    else:
        recomendacao = "Alerta elevado. Pode afetar sistemas eletrônicos e pessoas sensíveis."

    print(f"Índice KP atual de {cidade}: {kp}")
    print(f"Classificação: {risco}")
    print(f"Recomendação: {recomendacao}")

# ~~~~~~~~~ MENU PRINCIPAL ~~~~~~~~~

def mostrar_menu_principal() -> None:
    desenho.limpar_tela()
    desenho.titulo("HELION HEALTH")

    print('''
1 - Descrição do projeto
2 - Cadastrar dados pessoais
3 - Cadastrar localização
4 - Consultar índice KP / tempestade solar
5 - Recomendações de proteção UV
6 - Histórico de registros de localizações
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
            desenho.titulo("ÍNDICE KP / TEMPESTADE SOLAR")

            if kp_calculado == True:
                print("O índice KP já foi calculado.")
                print("Deseja calcular novamente? (S/N)")
                validador = input("").strip().lower()
                desenho.limpar_tela()
                while validador != "s" and validador != "n":
                    print("Valor inválido!")
                    print("Deseja calcular novamente? (S/N)")
                    validador = input("").strip().lower()
                    
                if validador == "s":
                    kp_atual = calcular_kp()
                    kp_calculado = True
                    analisar_kp(kp_atual)
                    if len(historico_localizacoes) > 0:
                        historico_localizacoes[-1][4] = kp_atual
                
                    
                else:
                    print("Mantendo o índice KP anterior.")
                    analisar_kp(kp_atual)
            else:
                kp_atual = calcular_kp()
                kp_calculado = True
                if len(historico_localizacoes) > 0:
                    historico_localizacoes[-1][4] = kp_atual
               
                analisar_kp(kp_atual)

            desenho.espera_entrada()

        case "5":
            recomendacoes_protecao()
            desenho.espera_entrada()
            
        case "6":
            consultar_historico()

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


