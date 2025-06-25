# main.py

from fastapi import FastAPI
from autenticador import Autenticador

class ServicoAutenticacao:
    """
    Classe responsável por encapsular as rotas e regras da API de autenticação.
    """
    def __init__(self):
        self.autenticador = Autenticador()

    def verificar_autenticacao(self) -> dict:
        try:
            return self.autenticador.carregar_credenciais()
        except Exception as e:
            return {"erro": str(e)}

# Instância da aplicação FastAPI
app = FastAPI()

# Instância da classe de serviço
servico = ServicoAutenticacao()

@app.get("/")
def hello():
    return {"mensagem": "Executando com sucesso"}

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/autenticar")
def autenticar():
    return servico.verificar_autenticacao()
