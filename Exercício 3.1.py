def main():
    palavra = input('Palavra: ')
    right_justify(palavra)

def right_justify(s):
    tamanho_palavra = len(s)
    quantidade_de_espaços = 70 - tamanho_palavra
    espaços = quantidade_de_espaços * ' '
    linha = espaços + s
    print(linha)

main()