'''Construa um programa para gerenciar um catálogo de produtos em uma loja. Os 
usuários podem adicionar produtos com informações como nome, preço e quantidade 
em estoque. Use um dicionário onde as chaves são os nomes dos produtos e os valores 
são outros dicionários com informações sobre cada produto.'''

import os
os.system('cls')

cadastro = {}

def get_dados():
    nome = input("Digite o nome do produto: ")

    while True:
        preco = input("Digite o preço: ")
        try:
            preco = int(preco)
            break
        except ValueError:
            print('Valor inválido. Por favor, informe um número.')

    while True:
        quantidade = input("Digite a quantidade: ")
        try:
            quantidade = float(quantidade)
            break
        except ValueError:
            print('Valor inválido. Por favor, informe um número.')

    dados = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }

    return dados

while True:
    dados = get_dados()
    cadastro[dados['nome']] = dados  # Usando o nome como chave do dicionário
    pergunta = input("Deseja adicionar mais um produto? [S/N] ").strip().upper()
    if pergunta == 'N':
        break

print("O catalogo ficou:")
for nome, informacao in cadastro.items():
    print(f'Produto: {informacao["nome"]}, Preço: {informacao["preco"]}, Quantidade: {informacao["quantidade"]},')
