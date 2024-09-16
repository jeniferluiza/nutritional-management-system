import pandas as pd

def gerar_plano_alimentar(paciente, dieta):
    with open(f'plano_{paciente.replace(" ", "_")}.txt', 'w') as file:
        file.write(f'Plano Alimentar para {paciente}\n\n')
        file.write(f'Dieta: {dieta}\n')
        file.write('Observações: Siga a dieta conforme orientado.')
    print(f'Plano alimentar para {paciente} gerado com sucesso.')

def gerar_relatorio():
    try:
        consultas = pd.read_csv('consultas.csv')
        with open('relatorio_consultas.txt', 'w') as file:
            file.write('Relatório de Consultas\n\n')
            for _, row in consultas.iterrows():
                file.write(f'Paciente: {row["paciente"]}, Data: {row["data"]}, Hora: {row["hora"]}\n')
        print('Relatório de consultas gerado com sucesso.')
    except FileNotFoundError:
        print("Nenhuma consulta para gerar relatório.")

gerar_plano_alimentar('Ana Costa', 'Dieta low-carb')
gerar_relatorio()
