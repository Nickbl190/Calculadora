#!/bin/bash
# Atualiza o sistema
sudo apt update

# Instala o pacote bc (caso necessário)
sudo apt install -y bc

# Executa a calculadora
python3 calculadora.py
