# tests/test_autenticador.py

"""
Testes unitários para a classe Autenticador.
Utiliza pytest para verificar o carregamento e validação de tokens a partir do arquivo .env.
"""

import os
import pytest
from smart_autenticacao.autenticador import Autenticador

class TestAutenticador:
    """
    Classe de testes para validar o comportamento do Autenticador.
    """

    def test_carrega_token_com_sucesso(self, tmp_path):
        """
        Testa se o token é corretamente carregado de um arquivo .env válido.
        Também verifica a resposta do método validar_token.
        """
        # Cria um arquivo temporário .env com o token de teste
        env_file = tmp_path / ".env.sucesso"
        env_file.write_text("API_TOKEN=meu-token-secreto")

        # Inicializa o autenticador usando o .env temporário
        auth = Autenticador(str(env_file))
        credenciais = auth.carregar_credenciais()

        # Verifica se o token foi carregado corretamente
        assert credenciais["API_TOKEN"] == "meu-token-secreto"

        # Verifica se a validação do token funciona
        assert auth.validar_token("meu-token-secreto") is True
        assert auth.validar_token("token-incorreto") is False

    def test_erro_quando_token_ausente(self, tmp_path):
        """
        Testa se um erro é lançado quando o arquivo .env não contém a variável API_TOKEN.
        """
        # Remove a variável de ambiente para evitar interferência
        os.environ.pop("API_TOKEN", None)

        # Cria um .env temporário vazio
        env_file = tmp_path / ".env.vazio"
        env_file.write_text("")

        # Espera que o Autenticador lance um ValueError ao não encontrar API_TOKEN
        with pytest.raises(ValueError) as excinfo:
            Autenticador(str(env_file))

        # Verifica se a mensagem de erro contém a variável esperada
        assert "API_TOKEN" in str(excinfo.value)
