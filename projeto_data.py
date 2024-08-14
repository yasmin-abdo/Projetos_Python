from datetime import datetime

def mes_por_extenso(mes):
    meses_lista = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses_lista[mes - 1]

def dia_por_extenso(dia):
    dias_lista = [
        "Um", "Dois", "Três", "Quatro", "Cinco", "Seis",
        "Sete", "Oito", "Nove", "Dez", "Onze", "Doze",
        "Treze", "Quatorze", "Quinze", "Dezesseis",
        "Dezessete", "Dezoito", "Dezenove", "Vinte",
        "Vinte e um", "Vinte e dois", "Vinte e três",
        "Vinte e quatro", "Vinte e cinco", "Vinte e seis",
        "Vinte e sete", "Vinte e oito", "Vinte e nove", "Trinta",
        "Trinta e um"
    ]
    return dias_lista[dia - 1]

def data_por_extenso(data):
    dia = dia_por_extenso(data.day)
    mes = mes_por_extenso(data.month)
    ano = data.year
    return f"{dia} de {mes} de {ano}"

def ler_data():
    while True:
        data_str = input("Digite a data no formato DD/MM/AAAA: ")
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida. Certifique-se de usar o formato DD/MM/AAAA.")

def converter_e_salvar_datas(datas_convertidas):
    with open("datas_convertidas.txt", "a", encoding="utf-8") as arquivo:
        for data_extenso in datas_convertidas:
            arquivo.write(f"{data_extenso}\n")

def main():
    datas_convertidas = []

    while True:
        print("\nMenu:")
        print("1 – Converter Data")
        print("2 – Listar Datas por extenso")
        print("3 – Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = ler_data()
            data_extenso = data_por_extenso(data)
            datas_convertidas.append(data_extenso)
            print(f"A data por extenso é: {data_extenso}")
        elif opcao == "2":
            if datas_convertidas:
                print("\nDatas convertidas:")
                for data_extenso in datas_convertidas:
                    print(data_extenso)
            else:
                print("Nenhuma data convertida ainda.")
        elif opcao == "3":
            converter_e_salvar_datas(datas_convertidas)
            print("Datas convertidas foram salvas em 'datas_convertidas.txt'.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
