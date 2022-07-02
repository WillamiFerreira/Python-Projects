#algoritimo que cria matriz.
#usei a função randint do módulo random.

from random import randint
def criar_matriz(l, c):
    matriz = []
    for lin in range(l):
        linha = []
        for col in range(c):
            linha.append(randint(1, 101))
        matriz.append(linha)
    print(matriz)

def main():
	linhas = int(input('Digite a quantidade de linhas: '))
	colunas = int(input('Digite a quantidade de colunas: '))
	criar_matriz(linhas, colunas)
	
if __name__ == "__main__":
	main()