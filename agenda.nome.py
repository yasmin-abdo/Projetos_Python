agenda = []  # lista para armazenar os contatos da agenda
alterada = False  # variável para marcar se houve alguma alteração na agenda

def pede_nome(padrão=""):
    # solicita o nome ao usuário, usa valor padrão se não fornecido
    nome = input("Nome: ")
    if nome == "":
        nome = padrão
    return nome

def pede_telefone(padrão=""):
    # solicita o telefone ao usuário, usa valor padrão se não fornecido
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrão
    return telefone

def pede_endereco(padrão=""):
    # solicita o endereço ao usuário, usa valor padrão se não fornecido
    endereco = input("Endereço: ")
    if endereco == "":
        endereco = padrão
    return endereco

def pede_cidade(padrão=""):
    # solicita a cidade ao usuário, usa valor padrão se não fornecido
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrão
    return cidade

def pede_uf(padrão=""):
    # solicita a UF ao usuário, usa valor padrão se não fornecido
    uf = input("UF (ex: SP): ")
    if uf == "":
        uf = padrão
    return uf

def mostra_dados(nome, telefone, endereco, cidade, uf):
    # exibe os dados do contato
    print(f"Nome: {nome} Telefone: {telefone} Endereço: {endereco} Cidade: {cidade} UF: {uf}")

def pede_nome_arquivo():
    # solicita o nome do arquivo ao usuário
    return input("Nome do arquivo: ")

def pesquisa(nome):
    # procura um contato pelo nome na agenda (case insensitive)
    # retorna o índice do contato se encontrado, caso contrário, retorna None
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    # adiciona um novo contato na agenda
    # solicita nome, telefone, endereço, cidade e uf ao usuário
    # VERIFICA SE O NOME JÁ EXISTE E EXIBE A MENSAGEM DE ERRO CASO NECESSÁRIO
    global agenda, alterada
    nome = pede_nome()
    if pesquisa(nome) is not None:
        print("ERRO: Já existe um contato com esse nome.")
        return
    telefone = pede_telefone()
    endereco = pede_endereco()
    cidade = pede_cidade()
    uf = pede_uf()
    agenda.append([nome, telefone, endereco, cidade, uf])
    alterada = True

def confirma(operação):
    # solicita confirmação ao usuário para uma operação específica (como gravação ou alteração)
    # retorna 'S' para sim e 'N' para não
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
    # remove um contato da agenda com base no nome fornecido pelo usuário
    # solicita confirmação antes de remover
    # marca a agenda como alterada se o contato for removido
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
    # altera um contato na agenda com base no nome fornecido pelo usuário
    # exibe os dados atuais e permite ao usuário modificar nome, telefone, endereço, cidade e uf
    # marca a agenda como alterada se houver uma alteração
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
        nome = pede_nome(nome)  # se nada for digitado, mantém o valor atual
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
    # lista todos os contatos na agenda, exibindo a posição, nome, telefone, endereço, cidade e uf de cada um
    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("------\n")

def lê_última_agenda_gravada():
    # lê o nome do último arquivo de agenda gravado e carrega os dados desse arquivo na agenda
    última = última_agenda()
    if última is not None:
        leia_arquivo(última)

def última_agenda():
    # lê o nome do último arquivo de agenda gravado a partir do arquivo "ultima agenda.dat"
    # retorna o nome do arquivo se encontrado, caso contrário, retorna None
    try:
        with open("ultima agenda.dat", "r", encoding="utf-8") as arquivo:
            última = arquivo.readline().strip()
    except FileNotFoundError:
        return None
    return última

def atualiza_última(nome):
    # atualiza o arquivo "ultima agenda.dat" com o nome do arquivo de agenda mais recentemente gravado
    with open("ultima agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

def leia_arquivo(nome_arquivo):
    # lê os dados de um arquivo especificado e atualiza a agenda com esses dados
    # marca a agenda como não alterada após a leitura
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
    # lê os dados de um arquivo de agenda especificado pelo usuário
    # pergunta ao usuário se deseja salvar a agenda se houver alterações não salvas
    # atualiza o arquivo "ultima agenda.dat" com o nome do arquivo lido
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
    # ordena a agenda por nome em ordem alfabética e marca a agenda como alterada
    global alterada
    agenda.sort(key=lambda e: e[0])
    alterada = True

def grava():
    # salva os dados da agenda em um arquivo especificado pelo usuário
    # pergunta ao usuário se deseja salvar mesmo se a agenda não tiver sido alterada
    # atualiza o arquivo "ultima agenda.dat" com o nome do arquivo salvo
    # marca a agenda como não alterada após a gravação
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
    # solicita um valor inteiro ao usuário e garante que o valor esteja dentro do intervalo especificado
    # repete até que um valor válido seja inserido
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
    # exibe o menu com opções para o usuário e retorna a opção escolhida
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

# lê o nome do último arquivo de agenda gravado e carrega os dados desse arquivo na agenda
lê_última_agenda_gravada()

# loop principal do programa, exibe o menu e executa a opção escolhida pelo usuário
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
