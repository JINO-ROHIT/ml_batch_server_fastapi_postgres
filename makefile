ABSOLUTE_PATH := ${shell pwd}

.PHONY: start
serve:
	docker compose up --build

.PHONY: stop
stop:
	docker compose down