import heapq
from lerTXT import ler_grafo_txt

grafo = ler_grafo_txt("entrada.txt")

def dijkstra(grafo, origem):
    distancias = {vertice: float('inf') for vertice in grafo}
    pai = {vertice: None for vertice in grafo}
    distancias[origem] = 0

    fila = [(0, origem)]

    while fila:
        distancia_atual, atual = heapq.heappop(fila)

        if distancia_atual > distancias[atual]:
            continue

        for vizinho, peso in grafo[atual]["vizinhos"]:
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                pai[vizinho] = atual
                heapq.heappush(fila, (distancia, vizinho))

    return distancias, pai

def reconstroi(pai, origem):
    caminhos = {}

    for destino in pai:
        if destino == origem:
            caminhos[destino] = [origem]
            continue

        if pai[destino] is None:
            caminhos[destino] = None 
            continue

        caminho = []
        atual = destino
        while atual is not None:
            caminho.insert(0, atual)
            atual = pai[atual]
        caminhos[destino] = caminho

    return caminhos

print("=== Testando o Dijkstra ===")
# testando 
resultado, predecessores = dijkstra(grafo, 'A')
caminhos = reconstroi(predecessores, 'A')

print("Distâncias a partir do vértice 'A':")
for vertice, distancia in resultado.items():
    print(f"{vertice}: {distancia}")

print("\nCaminhos mínimos a partir de 'A':")
for destino, caminho in caminhos.items():
    print(f"A → {destino}: {caminho}")




