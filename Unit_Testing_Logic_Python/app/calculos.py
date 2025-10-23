def calcular_frete(peso_kg):
    #Calcula o custo do frete baseado no peso em kg.
    if peso_kg < 0:
        raise ValueError("O peso não pode ser negativo.")

    taxa_por_kg =  1.50  # taxa fixa por kg
    taxa_base = 5.00   # taxa base fixa

    custo_total = taxa_base + (peso_kg * taxa_por_kg) + taxa_base
    return round(custo_total, 2)

def salvar_log(mensagem):
# Simula a gravação de logs em um banco de dados ou API externa.   
    # Esta função será usada para testes Mocking na próxima etapa.     
    print(f'LOG: {mensagem}')
    return True