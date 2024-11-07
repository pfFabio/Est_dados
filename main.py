import matplotlib.pyplot as plt
import json



def CarregaDados(caminho):
    arquivo = open(caminho, "r")
    conteudo = json.load(arquivo)
    return sorted(conteudo["vetor"]), conteudo["alvo"]

def DesenhaArvore(vetor, nivel = 0, x = 0, d=1):
    if not vetor:
        return 
    mediana = len(vetor) // 2 
    #pega os valores a esquerda
    DesenhaArvore(vetor[:mediana], nivel-1, x-d, d/2)


    DesenhaNo(vetor[mediana], x, nivel)
    pontos.append({
        "valor": vetor[mediana],
        "x": x,
        "y": nivel
    })

    #se tem 2 ou mais nós abaixo, ele desenha 2 pernas
    if len(vetor) > 2:
        plt.plot([x, x-d], [nivel, nivel-1], 'k-')
        plt.plot([x, x+d], [nivel, nivel-1], 'k-')
    #se só tem 1 nó abaixo ele desenha 1 perna pra esquerda
    elif len(vetor) == 2:
        plt.plot([x, x-d], [nivel, nivel-1], 'k-')

    #pega os valores a direita
    DesenhaArvore(vetor[mediana+1:], nivel-1, x+d, d/2)

def DesenhaNo(valor, x, y):
    plt.plot(x, y, 'o', markersize = 20, color = 'black')
    plt.text(x,y, valor, ha = 'center', va = "center", color = 'white')

def AchaValor(alvo,vetor):
    mediana = len(vetor) // 2

    for ponto in pontos:
        if ponto["valor"] == vetor[mediana]:
            px = ponto['x']
            py = ponto['y']
            plt.plot(px,py , 'o', markersize = 20, color = 'blue')
            plt.pause(0.5)
            plt.plot(px, py, 'o', markersize = 20, color = 'black')
            plt.pause(0.5)
              
    if vetor[mediana] == alvo:
        plt.plot(px, py, 'o', markersize = 20, color = 'green')
        return 1
    
    if vetor[mediana] > alvo:
        return AchaValor(alvo,vetor[:mediana])
        
    if vetor[mediana] < alvo:
        return AchaValor(alvo,vetor[mediana+1:])
    
fig, ax = plt.subplots()
ax.axis("off")

caminho = "teste.txt"
vetor, alvo = CarregaDados(caminho)
pontos = []

DesenhaArvore(vetor)

AchaValor(alvo, vetor)
plt.show()
