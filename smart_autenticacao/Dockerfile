# Dockerfile localizado em smart_autenticacao/

FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app/smart_autenticacao

# Copia os arquivos do módulo de autenticação e dos utilitários
COPY smart_autenticacao /app/smart_autenticacao
COPY smart_utils /app/smart_utils

# Instala as dependências
RUN pip install --no-cache-dir -r /app/smart_autenticacao/requirements.txt

# Comando padrão (sobrescrito pelo Compose)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

