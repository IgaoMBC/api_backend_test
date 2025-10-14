import requests
import pytest

# URL base da API que vamos testar
BASE_URL = "https://jsonplaceholder.typicode.com"

# --- Testes GET (Leitura) ---
def test_buscar_post_existente():
    """Verifica se a busca por um post específico (ID 1) retorna status 200 e dados corretos."""
    response = requests.get(f"{BASE_URL}/posts/1")
    
    # 1. Verifica Status Code HTTP
    assert response.status_code == 200
    
    # 2. Verifica Dados
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert len(data["body"]) > 0

def test_buscar_post_inexistente():
    """Verifica se a busca por um ID que não existe retorna 404 Not Found."""
    response = requests.get(f"{BASE_URL}/posts/99999") 
    assert response.status_code == 404

# --- Teste POST (Criação) ---
def test_criar_novo_post():
    """Verifica se a criação de um novo post retorna status 201 e o conteúdo criado."""
    
    novo_post = {
        "title": "Post Criado no Teste Automatizado",
        "body": "Corpo do post de teste.",
        "userId": 99
    }
    
    response = requests.post(f"{BASE_URL}/posts", json=novo_post)
    
    # 1. Verifica Status Code HTTP (201 Created)
    assert response.status_code == 201
    
    # 2. Verifica Dados
    data = response.json()
    assert "id" in data 
    assert data["title"] == novo_post["title"]
    assert data["userId"] == novo_post["userId"]