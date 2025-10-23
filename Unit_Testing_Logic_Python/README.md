# 🧪 Projeto de Testes Unitários e Mocks (Back-end)

Este projeto demonstra a aplicação de **Testes Unitários** em Python, que são a base da qualidade de código, garantindo que módulos e funções individuais funcionem corretamente.

## 🛠️ Tecnologias
* **Python**
* **Pytest** (Framework de Testes)
* **unittest.mock** (Biblioteca para simular dependências)

## 🎯 Conceitos Chave

Este projeto ilustra dois pilares dos testes Unitários:

### 1. Testes de Lógica Pura (Isolamento)

* **Onde:** `tests/test_calculos.py`
* **Função:** Garante que a lógica de negócio (como a função `calcular_frete`) retorne o valor esperado para entradas válidas e lide com erros (`ValueError`) para entradas inválidas. O teste é completamente isolado, sem dependências externas.

### 2. Mocking (Simulação de Dependências) - [Avançado]

* **Onde:** (Será implementado no próximo passo, no arquivo `tests/test_mocks.py`)
* **Função:** Demonstra como usar **Mocks** para simular chamadas a sistemas externos (como um banco de dados ou um serviço de log). Isso permite que o teste unitário se concentre **apenas** na lógica da função que está sendo testada, sem fazer chamadas lentas ou custosas à infraestrutura.

## ⚙️ Estrutura do Módulo

Unit_Testing_Logic_Python/ ├── app/ <-- Contém o código de produção (código a ser testado) │ └── calculos.py └── tests/ <-- Contém o código de teste └── test_calculos.py <-- Testes Unitários simples


---

## 🚀 Guia de Execução

1.  **Pré-requisito:** Estar com o ambiente virtual (`venv`) ativo.
2.  **Instale a dependência:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute os testes (a partir da pasta Unit_Testing_Logic_Python):**
    ```bash
    pytest -v
    ```
    **Resultado Esperado:** `2 passed` (Testes de lógica de frete).