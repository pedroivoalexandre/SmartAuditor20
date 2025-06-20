# autenticador.py

"""
Módulo responsável por carregar e validar credenciais de autenticação
usando variáveis de ambiente definidas em um arquivo .env.
"""

#importando a biblioteca de acesso ao arquivo .env
from dotenv import load_dotenv
#importando as variáveis de ambiente
import os

class Autenticador:
    """
    Classe responsável por carregar as credenciais do ambiente (.env)
    e validar tokens recebidos.
    """
    _token: str  # atributo protegido de instância esperado para armazenar o token

    def __init__(self, caminho_env: str | None = ".env"):
        """
        Inicializa o autenticador carregando o arquivo .env especificado
        e validando se a variável API_TOKEN está presente.
        """
        
        load_dotenv(dotenv_path=caminho_env, override=True) # Carrega as variáveis de ambiente do arquivo .env
        self._token = os.getenv("API_TOKEN") # Obtém o valor da variável API_TOKEN do ambiente

        if self._token is None or self._token.strip() == "": # Verifica se a variável API_TOKEN está definida
            raise ValueError(
                "Erro ao carregar a variável API_TOKEN. Verifique se ela está definida no .env."
            )
    
    # Método de acesso somente leitura para o token
    def carregar_credenciais(self) -> dict:
        """
        Retorna as credenciais carregadas. Útil para debug ou auditoria controlada.
        """
        return {"API_TOKEN": self._token} # Retorna as credenciais carregadas

    # Método para validar um token recebido
    def validar_token(self, token: str) -> bool:
        """
        Compara o token recebido com o carregado do ambiente.
        """
        return token == self._token