#lista para armazenar os contatos da agenda
agenda = []
#variável para marcar se houve alguma alteração na agenda
alterada = False

def pede_nome(padrão=""):
    #solicita ao usuário o nome. Se não for fornecido um nome, usa um valor padrão.
    nome = input("Nome: ")
    if nome == "":
        nome = padrão
    return nome

def pede_telefone(padrão=""):
    #solicita ao usuário o telefone. Se não for fornecido um telefone, usa um valor padrão.

    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrão
    return telefone

def mostra_dados(nome, telefone):
    #Exibe os dados do contato no formato "Nome: [nome] Telefone: [telefone]".

    print(f"Nome: {nome} Telefone: {telefone}")

def pede_nome_arquivo():
    #Solicita ao usuário o nome do arquivo e retorna o valor fornecido.
    return input("Nome do arquivo: ")

def pesquisa(nome):
   #rocura um contato pelo nome na agenda (case insensitive).
    #retorna o índice do contato se encontrado, caso contrário, retorna None.

    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
   #Adiciona um novo contato na agenda. Solicita o nome e telefone ao usuário.
    #Marca a agenda como alterada.

    global agenda, alterada
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    alterada = True

def confirma(operação):
    #Solicita confirmação ao usuário para uma operação específica (como gravação ou alteração).
    #Retorna 'S' para sim e 'N' para não.

    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
   #remove um contato da agenda com base no nome fornecido pelo usuário.
    #solicita confirmação antes de remover. Marca a agenda como alterada se o contato for removido.

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
    #altera um contato na agenda com base no nome fornecido pelo usuário.
    #exibe os dados atuais e permite ao usuário modificar o nome e telefone.
    #marca a agenda como alterada se houver uma alteração.

    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor atual
        telefone = pede_telefone(telefone)
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone]
            alterada = True
    else:
        print("Nome não encontrado.")

def lista():
   #lista todos os contatos na agenda, exibindo a posição, nome e telefone de cada um.

    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1])
    print("------\n")

def lê_última_agenda_gravada():
    #lê o nome do último arquivo de agenda gravado e carrega os dados desse arquivo na agenda.

    última = última_agenda()
    if última is not None:
        leia_arquivo(última)

def última_agenda():
    #lê o nome do último arquivo de agenda gravado a partir do arquivo "ultima agenda.dat".
    #Retorna o nome do arquivo se encontrado, caso contrário, retorna None.

    try:
        with open("ultima agenda.dat", "r", encoding="utf-8") as arquivo:
            última = arquivo.readline().strip()
    except FileNotFoundError:
        return None
    return última

def atualiza_última(nome):
   #atualiza o arquivo "ultima agenda.dat" com o nome do arquivo de agenda mais recentemente gravado.

    with open("ultima agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

def leia_arquivo(nome_arquivo):
   #lê os dados de um arquivo especificado e atualiza a agenda com esses dados.
    #Marca a agenda como não alterada após a leitura.

    global agenda, alterada
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split("#")
            agenda.append([nome, telefone])
    alterada = False

def lê():
    #lê os dados de um arquivo de agenda especificado pelo usuário.
    #Pergunta ao usuário se deseja salvar a agenda se houver alterações não salvas.
    #Atualiza o arquivo "ultima agenda.dat" com o nome do arquivo lido.

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
  #ordena a agenda por nome em ordem alfabética e marca a agenda como alterada.

    global alterada
    agenda.sort(key=lambda e: e[0])
    alterada = True

def grava():
    #salva os dados da agenda em um arquivo especificado pelo usuário.
    #pergunta ao usuário se deseja salvar mesmo se a agenda não tiver sido alterada.
    #atualiza o arquivo "ultima agenda.dat" com o nome do arquivo salvo.
    #marca a agenda como não alterada após a gravação.

    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")
    atualiza_última(nome_arquivo)
    alterada = False

def valida_faixa_inteiro(pergunta, inicio, fim):
   #solicita um valor inteiro ao usuário e garante que o valor esteja dentro do intervalo especificado.
    #Repete até que um valor válido seja inserido

    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
   #exibe o menu de opções e solicita ao usuário que escolha uma opção.
    #retorna a opção escolhida após validação.

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

# Lê o nome do último arquivo de agenda gravado e carrega seus dados
lê_última_agenda_gravada()

# Loop principal que exibe o menu e executa a opção escolhida
while True:
    opção = menu()
    if opção == 0:
        break  # Sai do loop e encerra o programa
    elif opção == 1:
        novo()  # Adiciona um novo contato
    elif opção == 2:
        altera()  # Altera um contato existente
    elif opção == 3:
        apaga()  # Remove um contato
    elif opção == 4:
        lista()  # Lista todos os contatos
    elif opção == 5:
        grava()  # Grava a agenda em um arquivo
    elif opção == 6:
        lê()  # Lê uma agenda de um arquivo
    elif opção == 7:
        ordena()  # Ordena os contatos por nome
