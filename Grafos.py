import math as math
from collections import deque
#Definindo a Classe Vertice
class Vertice:
    def __init__(self, id, raio, x, y):
        self.id = id
        self.raio = raio
        self.x = x
        self.y = y
        self.locA = False
        self.locB = False
        self.cor = 'branco'
        self.descoberta = -1
        self.menor_valor = -1
        self.pai = None
        self.vizinhos = []  # Lista de vértices conectados (arestas)

    def __repr__(self):
        return (f"V{self.id}(raio={self.raio}, x={self.x}, y={self.y}, "
                f"locA={self.locA}, locB={self.locB})")

#Gerando as arestas
def conectar_vertices(vertices):
    n = len(vertices)
    for i in range(n):
        for j in range(i + 1, n):
            vi = vertices[i]
            vj = vertices[j]
            dx = vi.x - vj.x
            dy = vi.y - vj.y
            distancia = math.hypot(dx, dy)

            if distancia <= (vi.raio + vj.raio):
                # Conecta os dois vertices
                if vj not in vi.vizinhos:
                    vi.vizinhos.append(vj)
                if vi not in vj.vizinhos:
                    vj.vizinhos.append(vi)

#Encontrando os Personagens
def encontrar_figuras(vertices, tupla1, tupla2):
    x1, y1 = map(float, tupla1)
    x2, y2 = map(float, tupla2)

    a, b = None, None

    for v in vertices:
        dist1 = math.hypot(v.x - x1, v.y - y1)
        dist2 = math.hypot(v.x - x2, v.y - y2)

        if dist1 <= v.raio:
            v.locA = True
            a = v.id
        if dist2 <= v.raio:
            v.locB = True
            b = v.id
    return(a,b)

#Pesquisa por largura customizada para encontrar o vertice com a figura x
def bfs(vertices,vertice):
    for v in vertices:
     v.cor = 'branco'
    fila = deque([vertice])
    vertice.cor = 'cinza'
    
    #Variaveis pra guardar o tamanho minimo de caminho entre as figuras e a altura
    altura = -1
    encontrou_caminho = False
    tamanho_caminho = -1
    
    #Inicio da geração do grafo e procura pela figura x
    while fila:
        altura += 1
        tamanho_nivel = len(fila)
        
        for i in range(tamanho_nivel):
            v = fila.popleft()

            for vizinho in v.vizinhos:
                if vizinho.cor == 'branco':
                    vizinho.cor = 'cinza'
                    fila.append(vizinho)

                
                if vizinho.locB == True and not encontrou_caminho and vertice.locA == True:
                    tamanho_caminho = altura+1
                    encontrou_caminho = True

            v.cor = 'preto'

    return tamanho_caminho, altura

#Função para rodar a BFS n vezes, o objetivo e encontrar a altura maxima para a parte 2
def encontrar_altura(vertices):
    max_altura = 0
    for v in vertices:
        _ , altura = bfs(vertices, v)
        if altura > max_altura:
            max_altura = altura
    return max_altura


#Pesquisa por profundidade customizada para encontrar os vertices "ponte"
def dfs(vertice, tempo, ponte):
    filhos = 0
    vertice.descoberta = vertice.menor_valor = tempo[0]
    tempo[0] += 1

    for vizinho in vertice.vizinhos:
        if vizinho.descoberta == -1:
            filhos += 1
            vizinho.pai = vertice
            dfs(vizinho, tempo, ponte)

            vertice.menor_valor = min(vertice.menor_valor, vizinho.menor_valor)

            if (vertice.pai is None and filhos > 1) or (vertice.pai and vizinho.menor_valor >= vertice.descoberta):
                ponte.add(vertice.id+1)

        elif vizinho != vertice.pai:
            vertice.menor_valor = min(vertice.menor_valor, vizinho.descoberta)

#Função para pesquisar em cada componente conexo do grafo
def encontrar_pontes(vertices):
    tempo = [0]
    ponte = set()
    
    for v in vertices:
        if v.descoberta == -1:  # ainda não visitado
            dfs(v, tempo, ponte)
    
    return ponte

#Função para encontrar a altura em cada componente conexo do grafo
def maior_altura_componentes(vertices):
    # Reseta as cores antes de começar
    for v in vertices:
        v.cor = 'branco'

    maior_altura = 1

    for v in vertices:
        if v.cor == 'branco':
            _, altura = bfs(v) 
            maior_altura = max(maior_altura, altura)

    return maior_altura


    

                