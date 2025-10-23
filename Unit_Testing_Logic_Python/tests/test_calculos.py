import pytest
from app.calculos import calcular_frete

# Teste 1: Caminho feliz (Happy Path)
def test_calcular_frete_para_10kg():
    # Esperado: (10 * 1.50) + 5.00 = 20.00
    resultado = calcular_frete(10)
    assert resultado == 20.00

# Teste 2: Cenário de falha (Exception Handling)
def test_calcular_frete_para_peso_negativo():
    with pytest.raises(ValueError) as excinfo:
        calcular_frete(-5)
    assert str(excinfo.value) == "O peso não pode ser negativo."