#!/bin/bash

echo "🔧 Bem-vindo ao instalador do projeto SmartAuditor20"
echo "==============================================="
echo "Módulos disponíveis:"
echo "1. smart_autenticacao"
echo "2. Todos os módulos (por enquanto, só smart_autenticacao está disponível)"
echo "==============================================="
read -p "Digite o número da opção desejada (1 ou 2): " opcao

# Caminho do módulo
MODULO_AUTH="smart_autenticacao"

# Função para clonar o repositório (se quiser automatizar)
clonar_repositorio() {
    if [ ! -d "$1" ]; then
        echo "📥 Clonando módulo $1..."
        git clone "https://github.com/seu-usuario/$1.git" "$1"
    else
        echo "✅ Módulo $1 já está presente."
    fi
}

# Função para executar o setup de um módulo
executar_setup_modulo() {
    echo "🚀 Executando setup de $1"
    bash "$1/setup.sh"
}

case $opcao in
  1)
    executar_setup_modulo $MODULO_AUTH
    ;;
  2)
    executar_setup_modulo $MODULO_AUTH
    ;;
  *)
    echo "❌ Opção inválida. Encerrando."
    exit 1
    ;;
esac

echo "✅ Instalação finalizada."
