# Makefile localizado em smart_autenticacao/

# Sobe o container e inicia a API
run:
	docker-compose up

# Reconstrói a imagem do container
build:
	docker-compose build

# Para e remove os containers
down:
	docker-compose down

# Executa os testes dentro do container
test:
	docker-compose run --rm autenticador pytest smart_autenticacao/tests
