APP_NAME=pgespinoza
STACK_FILE=stack.yml

build:
	docker build -t pgespinoza:1.0.1 .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml doraemon

logs:
	docker service logs -f $(APP_NAME)_$(APP_NAME)

rm:
	docker stack rm doraemon

ps:
	docker service ls

restart:
	make rm
	sleep 5
	make build
	make deploy