import csv

def agendar_consulta(paciente, data, hora):
    with open('consultas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([paciente, data, hora])
    print(f"Consulta agendada para {paciente} em {data} às {hora}.")

def listar_consultas():
    try:
        with open('consultas.csv', mode='r') as file:
            reader = csv.reader(file)
            print("Consultas agendadas:")
            for row in reader:
                paciente, data, hora = row
                print(f"Paciente: {paciente}, Data: {data}, Hora: {hora}")
    except FileNotFoundError:
        print("Nenhuma consulta agendada ainda.")

def adicionar_paciente(nome, idade, genero):
    with open('pacientes.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, idade, genero])
    print(f"Paciente {nome} adicionado com sucesso.")

def listar_pacientes():
    try:
        with open('pacientes.csv', mode='r') as file:
            reader = csv.reader(file)
            print("Pacientes cadastrados:")
            for row in reader:
                nome, idade, genero = row
                print(f"Nome: {nome}, Idade: {idade}, Gênero: {genero}")
    except FileNotFoundError:
        print("Nenhum paciente cadastrado ainda.")

def menu():
    while True:
        print("\nSistema de Gerenciamento de Consultas")
        print("1. Agendar Consulta")
        print("2. Listar Consultas")
        print("3. Adicionar Paciente")
        print("4. Listar Pacientes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            paciente = input("Nome do paciente: ")
            data = input("Data da consulta (dd/mm/aaaa): ")
            hora = input("Hora da consulta (hh:mm): ")
            agendar_consulta(paciente, data, hora)
        elif opcao == '2':
            listar_consultas()
        elif opcao == '3':
            nome = input("Nome do paciente: ")
            idade = input("Idade do paciente: ")
            genero = input("Gênero do paciente: ")
            adicionar_paciente(nome, idade, genero)
        elif opcao == '4':
            listar_pacientes()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
