# em python o que é um cabeçalho de um arquivo python e pra que serve? qual a diferença pra dockstring e pra que serve a dockstring

# Um cabeçalho de um arquivo Python geralmente inclui informações como o nome do arquivo, a descrição do que o arquivo faz, o autor, 
# a data de criação e outras informações relevantes. Ele serve para fornecer 
# contexto sobre o arquivo e facilitar a compreensão do seu propósito para outros desenvolvedores que possam ler ou usar o código no futuro.
# Em requisições web, são dados adicionais que acompanham o pedido ou a resposta, 
# transmitindo informações sobre a conexão, o conteúdo e o cliente. 

# Uma docstring, por outro lado, é uma string de documentação que aparece logo após a definição de um módulo, classe ou função. 
# Ela é usada para descrever o que o módulo, classe ou função faz, quais são seus parâmetros,
# o que ela retorna, entre outras informações úteis. As docstrings são acessíveis em tempo de execução através do atributo __doc__.
# A principal diferença entre um cabeçalho de arquivo e uma docstring é que o cabeçalho é mais geral e fornece informações sobre o arquivo como um todo,
# enquanto a docstring é específica para o módulo, classe ou função e fornece detalhes sobre seu funcionamento 

# docstrings são armazenadas no atributo doc do objeto e são acessíveis a partir do código em tempo de execução. 
# Isso significa que você pode acessar a documentação de uma função, por exemplo, diretamente do código.


#coloque o cabeçalho padrão neste arquivo, e resolva o exercício abaixo:


def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...

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
