#!/bin/bash

echo "🔧 Setup do módulo smart_autenticacao"

# Verifica se Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "⚠️ Docker não encontrado. Deseja instalar via apt? (s/n)"
    read instalar_docker
    if [[ "$instalar_docker" == "s" ]]; then
        sudo apt update
        sudo apt install -y docker.io
        sudo systemctl start docker
        sudo systemctl enable docker
    else
        echo "❌ Docker é necessário. Abortando setup."
        exit 1
    fi
fi

# Verifica se Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "⚠️ Docker Compose não encontrado. Deseja instalar? (s/n)"
    read instalar_compose
    if [[ "$instalar_compose" == "s" ]]; then
        sudo apt update
        sudo apt install -y docker-compose
    else
        echo "❌ Docker Compose é necessário. Abortando setup."
        exit 1
    fi
fi

echo "📁 Verificando arquivo .env..."
if [ ! -f "../.env" ]; then
    echo "❌ Arquivo .env não encontrado na raiz. Por favor, crie um .env em SmartAuditor20/.env antes de prosseguir."
    exit 1
fi

echo "✅ Ambiente verificado. Agora você pode rodar:"
echo "    cd smart_autenticacao"
echo "    docker-compose up --build"
