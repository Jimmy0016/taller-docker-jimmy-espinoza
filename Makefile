APP_NAME=espinoza
STACK_NAME=espinoza-stack
IMAGE_NAME=ghcr.io/jimmy0016/espinoza:1.0.5
STACK_FILE=stack.yml

# Construir imagen localmente
build:
	docker build -t $(IMAGE_NAME) .

# Ejecutar tests
test:
	python -m pytest test_app.py -v

# Ejecutar aplicación localmente
run:
	docker run -p 8080:80 $(IMAGE_NAME)

# Desplegar stack en Docker Swarm
deploy:
	docker stack deploy --with-registry-auth -c $(STACK_FILE) $(STACK_NAME)

# Ver logs del servicio
logs:
	docker service logs -f $(STACK_NAME)_$(APP_NAME)-app

# Remover stack
rm:
	docker stack rm $(STACK_NAME)

# Ver servicios activos
ps:
	docker service ls

# Reiniciar completamente
restart:
	make rm
	sleep 30
	make deploy

# Login a GHCR
login:
	echo "$(GITHUB_TOKEN)" | docker login ghcr.io -u $(GITHUB_USER) --password-stdin

# Push imagen a GHCR
push: build
	docker push $(IMAGE_NAME)

# Desarrollo completo: test, build, push, deploy
dev: test build push deploy

.PHONY: build test run deploy logs rm ps restart login push dev