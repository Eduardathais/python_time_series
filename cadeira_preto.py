#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Eduarda Thais
# Created Date: 31/08/2025
# version ='1.0'
# ---------------------------------------------------------------------------


def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    totais = {}
    for nome, valor in vendas:
        if nome in totais:
            totais[nome] += valor
        else:
            totais[nome] = valor
    return totais

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    if not totais:
        raise ValueError("Dicionário vazio")
    
    primeiro_item = list(totais.items())[0]
    melhor_nome, melhor_total = primeiro_item
    
    for nome, total in totais.items():
        if total > melhor_total:
            melhor_total = total
            melhor_nome = nome
    
    return (melhor_nome, melhor_total)

vendas = [
    ("Emerson", 100),
    ("Liliane", 200),
    ("Emerson", 50),
    ("Hugo", 300),
    ("Eduarda", 50),
    ("Emerson", 31),
    ("Hugo", 20),
    ("Eduarda", 54),
    ("Liliane", 60)
]

totais = total_por_vendedor(vendas)
print(totais)
print(melhor_vendedor(totais))

import time
from functools import wraps

#  Crie um decorator simples de tempo de execução 
# Requisitos:
# - Use @wraps para preservar __name__ e __doc__
# - Meça o tempo com time.perf_counter()
# - Printee: "func <nome> levou <segundos:.3f>s"
def tempo_execucao(func):
    # TODO: implementar
    raise NotImplementedError


# Crie um decorator com parâmetro: @repete(n) 
# Requisitos:
# - Executa a função "n" vezes
# - Retorna o resultado da última execução
# - Use @wraps na função interna
def repete(n):
    # TODO: implementar
    raise NotImplementedError


#  Funções-alvo para decorar 
def soma_lenta(a, b):
    """Soma após meio segundo"""
    time.sleep(0.5)
    return a + b

def diga_oi(nome):
    return f"Oi, {nome}!"


#  Aplique seus decorators (após implementar) 
# Ex.: @tempo_execucao
#      def soma_lenta(...):
#          ...

# Ex.: @repete(3)
#      def diga_oi(...):
#          ...
