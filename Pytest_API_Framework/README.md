# 💻 Framework de Testes de API Avançado (Python/Pytest)

Este projeto demonstra a criação de um framework de automação de testes de API RESTful que vai além da validação básica (status code), focando na Garantia de Qualidade (QA) estrutural e lógica.

---

## 🎯 Destaques do Projeto (Foco em QA)

A principal inovação deste framework é a validação de **JSON Schema**, uma técnica essencial em arquiteturas que dependem da integridade do contrato de dados.

### 1. Validação de JSON Schema (Integridade Estrutural)

* **Tecnologia:** Utilização da biblioteca **`jsonschema`** em Python.
* **Função:** O teste garante que o corpo da resposta JSON da API (endpoint `/posts`) sempre retorne **exatamente** os campos esperados (`userId`, `title`, etc.) e nos tipos de dados corretos (`integer`, `string`).
* **Valor para o Negócio:** Previne quebras de código no Frontend ou em outros Microsserviços, que dependem de uma estrutura de dados previsível. O uso de `additionalProperties: false` impede que a API retorne campos não documentados.

### 2. Validação Lógica e Cenários de Falha

* **Cenário Testado:** O projeto inclui validação de cenários negativos e de lógica de negócio (ex.: testar a busca por um ID inexistente).
* **Função:** Garante que a API lide com erros de forma controlada, retornando o status HTTP apropriado (`404 Not Found`).

---

## ⚙️ Arquitetura do Framework

Pytest_API_Framework/ ├── schemas/ │ └── post_schema.json <-- O arquivo de regra que define a estrutura JSON ├── tests/ │ └── test_posts.py <-- Contém as fixtures (pathlib) e a lógica de validação └── requirements.txt


---

## 🚀 Guia de Execução

1.  **Pré-requisito:** Estar com o ambiente virtual (`venv`) ativo.
2.  **Instale as dependências:** (A biblioteca `jsonschema` é crucial aqui)
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute os testes (a partir da pasta Pytest_API_Framework):**
    ```bash
    pytest -v
    ```
    **Resultado Esperado:** `2 passed`, confirmando o sucesso na validação de sucesso e de falha.