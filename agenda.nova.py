agenda = []
alterada = False

def pede_nome(padrão=""):
    nome = input("Nome: ")
    if nome == "":
        nome = padrão
    return nome

def pede_telefone(padrão=""):
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrão
    return telefone

def pede_endereco(padrão=""):
    endereco = input("Endereço: ")
    if endereco == "":
        endereco = padrão
    return endereco

def pede_cidade(padrão=""):
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrão
    return cidade

def pede_uf(padrão=""):
    uf = input("UF (ex: SP): ")
    if uf == "":
        uf = padrão
    return uf

def mostra_dados(nome, telefone, endereco, cidade, uf):
    print(f"Nome: {nome} Telefone: {telefone} Endereço: {endereco} Cidade: {cidade} UF: {uf}")

def pede_nome_arquivo():
    return input("Nome do arquivo: ")

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    global agenda, alterada
    nome = pede_nome()
    telefone = pede_telefone()
    endereco = pede_endereco()
    cidade = pede_cidade()
    uf = pede_uf()
    agenda.append([nome, telefone, endereco, cidade, uf])
    alterada = True

def confirma(operação):
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        endereco = agenda[p][2]
        cidade = agenda[p][3]
        uf = agenda[p][4]
        print("Encontrado:")
        mostra_dados(nome, telefone, endereco, cidade, uf)
        nome = pede_nome(nome)
        telefone = pede_telefone(telefone)
        endereco = pede_endereco(endereco)
        cidade = pede_cidade(cidade)
        uf = pede_uf(uf)
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone, endereco, cidade, uf]
            alterada = True
    else:
        print("Nome não encontrado.")

def lista():
    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("------\n")

def lê_última_agenda_gravada():
    última = última_agenda()
    if última is not None:
        leia_arquivo(última)

def última_agenda():
    try:
        with open("ultima agenda.dat", "r", encoding="utf-8") as arquivo:
            última = arquivo.readline().strip()
    except FileNotFoundError:
        return None
    return última

def atualiza_última(nome):
    with open("ultima agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

def leia_arquivo(nome_arquivo):
    global agenda, alterada
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for l in arquivo.readlines():
            dados = l.strip().split("#")
            if len(dados) == 5:
                nome, telefone, endereco, cidade, uf = dados
                agenda.append([nome, telefone, endereco, cidade, uf])
    alterada = False

def lê():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_última(nome_arquivo)

def ordena():
    global alterada
    agenda.sort(key=lambda e: e[0])
    alterada = True

def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")
    atualiza_última(nome_arquivo)
    alterada = False

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

lê_última_agenda_gravada()

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
    elif opção == 7:
        ordena()
