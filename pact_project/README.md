
# 🚀 Portfólio de Automação e Desenvolvimento Back-end

Este repositório serve como portfólio de projetos práticos em desenvolvimento Back-end e Automação de Testes, demonstrando habilidades essenciais em Python, testes de API, e arquiteturas de Microsserviços.

---

## 🛠️ Habilidades Técnicas em Destaque

| Categoria | Tecnologias e Conceitos |
| :--- | :--- |
| **Linguagens** | Python (Avançado), Java, SQL, JavaScript |
| **Testes e Qualidade** | **Testes de Contrato (Pact CDC)**, Pytest, Testes de API REST, TDD (Test-Driven Development) |
| **APIs e Microsserviços** | Requisições HTTP (Requests), Validação JSON, Arquiteturas Distribuídas |
| **Ferramentas** | Git/GitHub, VIM/VS Code, Ambiente Virtual (venv) |

---

## 💡 Projetos Desenvolvidos

### 1. Testes de Contrato para Microsserviços (Pact CDC)

* **Local:** `pact_project/tests/test_consumer.py`
* **Descrição:** Implementação de uma solução de **Consumer-Driven Contracts (CDC)** usando a biblioteca **Pact** em Python.
    * **Objetivo:** Garantir que o serviço consumidor e o serviço provedor mantenham um contrato de dados compatível, prevenindo falhas de integração em ambientes de **microsserviços**.
    * **Destaque:** Demonstra a habilidade de trabalhar com padrões de arquitetura modernos e isolar testes de integração.

### 2. Automação de Testes de API RESTful

* **Local:** `tests/test_api_posts.py`
* **Descrição:** Suíte de **Testes Automatizados de API** para validação de endpoints REST.
    * **Métodos Validados:** Cobertura de funcionalidades básicas de CRUD (GET, POST, tratamento de erros) utilizando **Pytest** e **Requests**.
    * **Destaque:** Foco na verificação de códigos de status HTTP (`200 OK`, `201 Created`, `404 Not Found`) e na integridade dos dados retornados no *payload*.

---

## ⚙️ Guia de Execução Local

Para rodar todos os testes do projeto em sua máquina:

### 1. Configuração

```bash
# 1. Ative seu ambiente virtual (venv)
.\venv\Scripts\activate   # Windows PowerShell
# source venv/bin/activate  # macOS/Linux

# 2. Instale as dependências para ambos os projetos
pip install pytest requests pact-python