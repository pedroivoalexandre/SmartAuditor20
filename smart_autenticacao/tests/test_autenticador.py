# test_autenticador.py

import os
import pytest
from smart_autenticacao.autenticador import Autenticador

def test_carrega_token_com_sucesso(tmp_path):
    # Cria um arquivo .env temporário com um token
    env_file = tmp_path / ".env.teste"
    env_file.write_text("API_TOKEN=token-teste")

    # Testa se o token é carregado corretamente
    auth = Autenticador(str(env_file))
    credenciais = auth.carregar_credenciais()

    assert credenciais["API_TOKEN"] == "token-teste"
    assert auth.validar_token("token-teste") is True
    assert auth.validar_token("invalido") is False

def test_erro_quando_token_ausente(tmp_path):
    
    os.environ.pop("API_TOKEN", None)

    # Cria .env vazio
    env_file = tmp_path / ".env.vazio"
    env_file.write_text("")  # Nenhuma variável

    # Espera erro de valor ao tentar carregar sem token
    with pytest.raises(ValueError) as excinfo:
        auth = Autenticador(str(env_file))

    assert "API_TOKEN" in str(excinfo.value)


