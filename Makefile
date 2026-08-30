# ──────────────────────────────────────────────────────────────────────
# G14_Busca_EDA2-2026.2 - automacao do ambiente Python
# ──────────────────────────────────────────────────────────────────────

VENV        = .venv
REQ         = requirements.txt
SCRIPTS_DIR = scripts
SRC_DIR     = src
DATA_DIR    = data

# Deteccao de Sistema Operacional (Windows vs Unix).
# No Windows a variavel de ambiente OS ja vale "Windows_NT" e e importada
# pelo make; no Unix ela fica vazia e usamos `uname`.
ifneq ($(OS),Windows_NT)
OS := $(shell uname)
endif

ifeq ($(OS),Windows_NT)
    PYTHON      = python
    PYTHON_VENV = $(VENV)\Scripts\python.exe
    PIP         = $(VENV)\Scripts\pip.exe
    CHECK_VENV  = call $(SCRIPTS_DIR)\check_venv.bat
    CHECK_REQ   = $(PYTHON_VENV) $(SCRIPTS_DIR)\check_requirements.py
    CHCP_CMD    = chcp 65001 >NUL
    DEVNULL     = NUL
    UI_BOLD     =
    UI_RESET    =
    PRINT       = @echo
else
    PYTHON      = python3
    PYTHON_VENV = $(VENV)/bin/python3
    PIP         = $(VENV)/bin/pip
    CHECK_VENV  = sh $(SCRIPTS_DIR)/check_venv.sh
    CHECK_REQ   = $(PYTHON_VENV) $(SCRIPTS_DIR)/check_requirements.py
    CHCP_CMD    = true
    DEVNULL     = /dev/null
    UI_BOLD     = \033[1;36m
    UI_RESET    = \033[0m
    PRINT       = @printf '%b\n'
endif

.PHONY: help setup build-up venv install verify run test lint clean

# help: Lista os comandos disponiveis
help:
	@$(CHCP_CMD) || true
	$(PRINT) "Comandos disponiveis:"
	$(PRINT) "  make setup    - Cria o ambiente virtual e instala as dependencias."
	$(PRINT) "  make run      - Executa a aplicacao de busca."
	$(PRINT) "  make test     - Roda os testes (pytest)."
	$(PRINT) "  make lint     - Verifica o estilo do codigo (ruff)."
	$(PRINT) "  make clean    - Remove o ambiente virtual e arquivos temporarios."

# setup: Fluxo completo de inicializacao do ambiente
setup: build-up

build-up:
	@$(CHCP_CMD) || true
	$(PRINT) "$(UI_BOLD)Iniciando instalacao do ambiente...$(UI_RESET)"
	@$(MAKE) venv
	@$(MAKE) install
	@$(MAKE) verify
	$(PRINT) "$(UI_BOLD)Sucesso! Use 'make run' para iniciar o projeto.$(UI_RESET)"

venv:
	@$(PRINT) "[1/3] Verificando interpretador Python e Venv..."
	@$(CHECK_VENV)

install:
	@$(PRINT) "[2/3] Sincronizando dependencias Python..."
	@$(CHECK_REQ)

verify:
	@$(PRINT) "[3/3] Validando configuracao..."
	@$(PYTHON_VENV) --version >$(DEVNULL) 2>&1 || (echo "Erro no ambiente virtual." && exit 1)

# run: Executa a aplicacao
run:
	@$(CHCP_CMD) || true
	@$(PYTHON_VENV) -m $(SRC_DIR).main

# test: Roda a suite de testes
test:
	@$(PRINT) "$(UI_BOLD)Rodando testes (pytest)...$(UI_RESET)"
	@$(PYTHON_VENV) -m pytest

# lint: Verifica o estilo do codigo
lint:
	@$(PYTHON_VENV) -m ruff check $(SRC_DIR) tests

# clean: Remove o venv e arquivos temporarios
clean:
	@$(PRINT) "Limpando ambiente..."
ifeq ($(OS),Windows_NT)
	@if exist $(VENV) rmdir /s /q $(VENV)
	@if exist .pytest_cache rmdir /s /q .pytest_cache
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
else
	@rm -rf $(VENV) .pytest_cache
	@find . -type d -name __pycache__ -exec rm -rf {} +
endif
	@$(PRINT) "Limpeza concluida."
