SHELL := /bin/bash

start:
	./projctl.sh --start

stop:
	./projctl.sh --end

restart:
	./projctl.sh --end
	./projctl.sh --start

install:
	@echo "Instalando dependencias"
	python -m venv backend/venv
	source backend/venv/bin/activate
	pip install -r backend/requeriments.txt

	cd frontend
	npm install

clean:
	@echo "Eliminando archivos temporales"
	rm -f *.pid
	rm -rf backend/__pycache__ frontend/node_modules

help:
	@echo "Uso del Makefile"
	@echo "  make start		- Inicia el proyecto"
	@echo "  make stop		- Detiene el proyecto"
	@echo "  make restart	- Reinicia el proyecto"
	@echo "  make install	- Instala dependencias"
	@echo "  make clean		- Elimina archivos temporales"