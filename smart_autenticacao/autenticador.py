# smart_autenticacao/autenticador.py

"""
Módulo responsável por carregar e validar credenciais de autenticação
usando variáveis de ambiente definidas em um arquivo .env.
"""

from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente de arquivos .env
import os

class Autenticador:
    """
    Classe que encapsula a lógica de autenticação, incluindo o carregamento
    de variáveis de ambiente e a verificação de tokens.
    """
    def __init__(self, caminho_env: str | None = ".env"):
        """
        Construtor que carrega as variáveis de ambiente de um arquivo .env
        e armazena o token em um atributo protegido.
        """
        load_dotenv(dotenv_path=caminho_env, override=True)  # Carrega o .env
        self._token = os.getenv("API_TOKEN")  # Busca o token

        if self._token is None or self._token.strip() == "":
            raise ValueError("Erro ao carregar a variável API_TOKEN. Verifique se ela está definida no .env.")

    def carregar_credenciais(self) -> dict:
        """
        Método público que retorna o token carregado (por segurança, deve ser usado apenas em ambiente controlado).
        """
        return {"API_TOKEN": self._token}

    def validar_token(self, token: str) -> bool:
        """
        Compara o token recebido com o token carregado.
        """
        return token == self._token

def verificar_autenticacao() -> dict:
    """
    Função auxiliar que tenta carregar o token usando a classe Autenticador
    e retorna as credenciais ou o erro encontrado.
    Útil para chamadas de teste na API.
    """
    try:
        auth = Autenticador()
        return auth.carregar_credenciais()
    except Exception as e:
        return {"erro": str(e)}
