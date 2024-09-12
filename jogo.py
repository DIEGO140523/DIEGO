import random

palavras = ["arthur", "mouse", "sao paulo", "cadeira", "carro", "ze raimundo", "computador", "php", "javascript"]
palavraEscolhida = random.choice(palavras)

erro = len(palavraEscolhida) - 1 
erros = 0

print("A palavras sorteada tem " + str(len(palavraEscolhida))+ " letras")

l = input("INFORME UMA LETRA: ")


while erros < 6:
    for letra in palavraEscolhida:
        if(l == letra):
            print("A letra " + str(l) + " estar na posicao " + str(palavraEscolhida.find(l)))
            print("A letra " + str(l) + " estar na posicao " + str(palavraEscolhida.index(l) + 1))
        else:
            erros += 1
        
print(palavraEscolhida)