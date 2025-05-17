import random 
from grafo import grafo
from collections import deque
from dijkstra import dijkstra, reconstroi

def criarfogo(grafo, lago, posto):
    while True:
        try:
            fagulha = random.randint(0, len(grafo) - 1)
            vertice = chr(65 + fagulha)  # A, B, C...

            if vertice in lago or vertice in posto:
                continue
            else:
                grafo[vertice]["info"][3] = 1
                print(f"Fogo iniciado em {vertice}.")
                break
        except IndexError:
            print("Não há vértices válidos para pegar fogo (todos são lagos ou postos).")
            break


def em_chamas(grafo):
    # Verifica se algum vértice está pegando fogo
    for vertice in grafo:
        if grafo[vertice]["info"][3] == 1:
            return True
    return False

def criar_postos(grafo):

    chaves = list(grafo.keys())
    postos = random.sample(chaves,3)

    for v in postos:
        grafo[v]["info"][1] = True



def criar_coleta(grafo):
    vertices_utilizaveis = [v for v in grafo if grafo[v]["info"][1] == False]


    coleta = random.sample(vertices_utilizaveis,4)

    for v in coleta:
        grafo[v]["info"][2] = True

def propagacao(grafo):
    visitado = set()
    fila = deque()

    # Passo 1: Adiciona todos os vértices que já estão em chamas à fila
    for vertice in grafo:
        if grafo[vertice]["info"][3] == 1:
            fila.append(vertice)
            visitado.add(vertice)

    # Passo 2: Propaga o fogo em BFS
    while fila:
        atual = fila.popleft()
        for vizinho, _ in grafo[atual]["vizinhos"]:
            # Se ainda não está em chamas e não é lago ou posto
            if (
                grafo[vizinho]["info"][3] == 0 and 
                grafo[vizinho]["info"][1] == 0 and 
                grafo[vizinho]["info"][2] == 0
            ):
                if random.randint(0, 1):  # 50% de chance de pegar fogo
                    grafo[vizinho]["info"][3] = 1
                    fila.append(vizinho)
                    print(f"O vértice {vizinho} começou a pegar fogo!")


# Gera o grafo com postos, lago e fogo inicial
criar_postos(grafo)
criar_coleta(grafo)
lagos = [k for k in grafo if grafo[k]["info"][2]]    # info[2] == True → lago
postos = [k for k in grafo if grafo[k]["info"][1]]   # info[1] == True → posto

# Inicializa fogo em vértices aleatórios que não são postos nem lagos
criarfogo(grafo, postos, lagos)

print("=== Estado inicial do grafo ===")
for vertice, dados in grafo.items():
    info = dados["info"]
    vizinhos = ", ".join([f"{v} (custo {c})" for v, c in dados["vizinhos"]])
    print(f"Vértice {vertice}:")
    print(f"  Água necessária: {info[0]}")
    print(f"  Posto de brigada: {info[1]}")
    print(f"  Lago: {info[2]}")
    print(f"  Estado do fogo: {info[3]}")
    print(f"  Vizinhos: {vizinhos}")
    print()

print("=== Propagando fogo... ===")
propagacao(grafo)

# Exibe estado após propagação
print("\n=== Estado do grafo após propagação ===")
for vertice, dados in grafo.items():
    info = dados["info"]
    print(f"Vértice {vertice}: fogo = {info[3]}")


# class vingadores:
#     def __init__(self, local, qtd_agua):
#         self.local = local
#         self.qtd_agua = qtd_agua
#         self.caminho = []
#         self.capacidadeAtual = qtd_agua

#     def __str__(self):
#         return f"Brigada se encontra no local {self.local}, com a de água = {self.capacidadeAtual}/{self.qtd_agua}."


class vingadores:
    def __init__(self, local, qtd_agua):
        self.local = local
        self.qtd_agua = qtd_agua
        self.caminho = []
        self.capacidadeAtual = qtd_agua

    def __str__(self):
        return f"Brigada se encontra no local {self.local}, com a de água = {self.capacidadeAtual}/{self.qtd_agua}."

    def andando(self, grafo):
        print(f"\n🚶 Equipe no vértice {self.local} com {self.capacidadeAtual}/{self.qtd_agua} de água.")

        # Se está no fogo e tem água
        if grafo[self.local]["info"][3] == 1 and self.capacidadeAtual > 0:
            print("fogo no local")
            self.apagar(grafo)
            return

        # Se está sem água
        if self.capacidadeAtual == 0:
            print("Sem água. Procurando ponto de reabastecimento")
            self.abastecer(grafo)
            return

        # Encontrar o fogo mais próximo
        distancia, pai = dijkstra(grafo, self.local)
        menor = float('inf')
        destino = None

        for v in grafo:
            if grafo[v]["info"][3] == 1 and distancia[v] < menor:
                menor = distancia[v]
                destino = v

        if destino:
            caminho = reconstroi(pai, self.local).get(destino)
            if caminho and len(caminho) > 1:
                proximo = caminho[1]
                print(f"Indo de {self.local} para {proximo} apagar fogo em {destino}")
                self.local = proximo
            else:
                print("Já está no destino do fogo.")
                self.apagar(grafo)
        else:
            print("Nenhum fogo conhecido. Esperando instruções.")

    # def abastecer(self, grafo): 
    #     distancias, pais = dijkstra(grafo, self.local)
    #     menor = float('inf')
    #     destino = None

    #     for v in grafo:
    #         if (grafo[v]["info"][1] or grafo[v]["info"][2]) and distancias[v] < menor:
    #             menor = distancias[v]
    #             destino = v

    #     if destino:
    #         caminho = reconstroi(pais, self.local).get(destino)
    #         if caminho and len(caminho) > 1:
    #             proximo = caminho[1]
    #             print(f"Indo reabastecer: {self.local} → {proximo}")
    #             self.local = proximo
    #         else:
    #             print(f"Chegou ao ponto de reabastecimento {self.local}. Recarregando tanque.")
    #             self.capacidadeAtual = self.qtd_agua
    #     else:
    #         print("Nenhum ponto de reabastecimento acessível.")

    # def apagar(self, grafo):
    #     agua_necessaria = grafo[self.local]["info"][0]
    #     print(f"Tentando apagar fogo em {self.local} (precisa de {agua_necessaria}, tem {self.capacidadeAtual})")

    #     if agua_necessaria > self.capacidadeAtual:
    #         grafo[self.local]["info"][0] -= self.capacidadeAtual
    #         print(f"Fogo reduzido. Ainda falta {grafo[self.local]['info'][0]} de água.")
    #         self.capacidadeAtual = 0
    #     else:
    #         self.capacidadeAtual -= agua_necessaria
    #         grafo[self.local]["info"][0] = 0
    #         grafo[self.local]["info"][3] = -1  # fogo extinto
    #         print(f"Fogo em {self.local} apagado com sucesso! Restante de água: {self.capacidadeAtual}")

        


