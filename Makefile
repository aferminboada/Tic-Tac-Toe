build:
	docker build -t vieja .

create:
	docker run -itd --name cont_vieja -v pwd:/vieja vieja

start:
	docker container start cont_vieja

stop:
	docker container stop cont_vieja

restart:
	docker container restart cont_vieja

bash:
	docker exec -it cont_vieja bash

rm:
	docker rm cont_vieja
