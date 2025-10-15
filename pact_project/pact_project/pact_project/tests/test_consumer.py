import pytest
import requests
from pact import Pact # Biblioteca do Pact para Python

# 1. DEFINIÇÃO DOS ATORES
# O Consumidor (seu serviço) e o Provedor (a API externa)
CONSUMER = "MyFrontendConsumer"
PROVIDER = "ProductService"

# 2. FIXTURE PYTEST PARA INICIAR O MOCK DO PACT
@pytest.fixture(scope='session')
def pact():
    # Padrão moderno (usado em 99% dos ambientes)
    pact = Pact(consumer=CONSUMER, provider=PROVIDER)
    with pact: # O 'with' inicia e para o Mock Service automaticamente
        yield pact
    # 3. Teardown (Parar o Mock com o comando Python puro)
    pact.teardown()
    
# O teste de contrato agora se chama test_get_all_products(pact)

# 3. O TESTE DE CONTRATO REAL (Escrito pelo Consumidor)
# A fixture agora se chama 'pact' (note a mudança de nome aqui e acima)
def test_get_all_products(pact):
    # ... o restante do código que usa a fixture 'pact'
    MOCK_URL = pact.mock_service_base_uri 

    # 3a. DEFINIÇÃO DA INTERAÇÃO (O CORAÇÃO DO TESTE)
    pact \
        .given("Products data exists") \
        .upon_receiving("A request for all products") \
        .with_request('get', '/products') \
        .will_respond_with(200, body=[
            # ...
        ])

    # 3b. A EXECUÇÃO DO CONSUMIDOR (Testando contra o Mock)
    response = requests.get(f"{MOCK_URL}/products")

    # 3c. VERIFICAÇÕES
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]['name'] == "Widget A"

    # 3d. GERAÇÃO DO ARQUIVO DE CONTRATO (.json)
    pact.verify()