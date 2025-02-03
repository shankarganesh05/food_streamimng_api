run-dev:
	cp live.env settings.env
	uv run python run.py
run-dev-historical:
	cp historical.env settings.env
	uv run python run.py
build:
	docker build -f DockerFile -t my-fastapi .
run:build
	docker run -it \
		-p 8080:8080 \
		my-fastapi