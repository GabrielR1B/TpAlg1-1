import Grafos as gf
import sys
#Leitura do Arquivo de Input
linhas = sys.stdin.read().strip().split('\n')

#Atribuindo as cordenadas, tamanho do grafo, e inicializando outras variaveis
cordA = tuple(linhas[0].strip().split(' '))
cordB = tuple(linhas[1].strip().split(' '))
quantidadeAbrigos = int(linhas[2].strip())
vertices = []
tempo = [0]
ponte = set()

# Criando vértices
for i in range(quantidadeAbrigos):
    raio, x, y = map(float, linhas[3 + i].strip().split(' '))
    vertice = gf.Vertice(i, raio, x, y)
    vertices.append(vertice)

#Criando Arestas
gf.conectar_vertices(vertices)

#Descobrindo em qual vertice estão Ana e Bernardo
a,b = gf.encontrar_figuras(vertices, cordA, cordB)
# Parte 1: caminho mínimo de A até B com BFS
parte1, _ = gf.bfs(vertices,vertices[a])
# Parte 2: altura máxima de componentes conexos
parte2 = gf.encontrar_altura(vertices)
# Parte 3: pontes de vertices (vértices críticos)
ponte = gf.encontrar_pontes(vertices)
print("Parte 1:", parte1)
print("Parte 2:", parte2)
print(f"Parte 3: {len(ponte)}", ' '.join(str(id) for id in sorted(ponte)))