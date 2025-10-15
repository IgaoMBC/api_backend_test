# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

# Projeto de Testes Automatizados de Back-end (API Testing)

Este projeto demonstra a criação e execução de testes automatizados para uma API REST, utilizando Python e o framework Pytest. O foco está na validação de funcionalidades de manipulação de dados (CRUD) no lado do servidor.

## 🛠️ Tecnologias e Ferramentas

| Tecnologia | Função |
| :--- | :--- |
| **Python** | Linguagem de programação principal. |
| **`pytest`** | Framework utilizado para estruturar e executar os testes. |
| **`requests`** | Biblioteca HTTP para envio de requisições GET/POST. |
| **JSONPlaceholder** | API pública (simulada) utilizada como alvo dos testes. |

## 🎯 Funcionalidades Testadas

O arquivo `tests/test_api_posts.py` valida os seguintes cenários:

1.  **GET /posts/{id}:**
    * Verifica se a busca por um recurso existente retorna o status `200 OK` e dados corretos.
    * Verifica se a busca por um recurso inexistente retorna o status `404 Not Found`.
2.  **POST /posts:**
    * Verifica se a criação de um novo recurso retorna o status `201 Created` e se os dados do novo recurso (incluindo o ID gerado) são retornados corretamente.

## 🚀 Guia de Execução Local

Siga os passos para configurar e executar os testes em sua máquina:

### 1. Pré-requisitos
* Python 3.x instalado.

### 2. Configuração do Ambiente

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente (Exemplo Windows PowerShell)
.\venv\Scripts\activate 

# Instala as dependências listadas no requirements.txt
pip install -r requirements.txt