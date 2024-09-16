# nutritional-management-system
import pandas as pd
from datetime import datetime

# Função para agendar uma consulta
def agendar_consulta(paciente, data, hora):
    try:
        consultas = pd.read_csv('consultas.csv')
    except FileNotFoundError:
        consultas = pd.DataFrame(columns=['id', 'paciente', 'data', 'hora'])
    
    novo_id = len(consultas) + 1
    nova_consulta = pd.DataFrame([[novo_id, paciente, data, hora]], columns=['id', 'paciente', 'data', 'hora'])
    consultas = pd.concat([consultas, nova_consulta], ignore_index=True)
    consultas.to_csv('consultas.csv', index=False)
    print(f'Consulta agendada para {paciente} em {data} às {hora}.')

# Função para listar consultas
def listar_consultas():
    try:
        consultas = pd.read_csv('consultas.csv')
        print(consultas)
    except FileNotFoundError:
        print("Nenhuma consulta agendada.")

# Exemplo de uso
agendar_consulta('Ana Costa', '2024-09-22', '16:00')
listar_consultas()
