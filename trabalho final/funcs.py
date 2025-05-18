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


# utilizando o busca em largura
def propagacao(grafo):
    visitado = set()
    fila = deque()

    for vertice in grafo:
        if grafo[vertice]["info"][3] == 1:
            fila.append(vertice)    
            visitado.add(vertice)
    while fila:
        atual = fila.popleft()
        for vizinho, _ in grafo[atual]["vizinhos"]:
            if (
                grafo[vizinho]["info"][3] == 0 and 
                grafo[vizinho]["info"][1] == 0 and 
                grafo[vizinho]["info"][2] == 0
            ):
                if random.randint(1, 5) <= 4:
                    grafo[vizinho]["info"][3] = 1
                    fila.append(vizinho)
                    print(f"O vértice {vizinho} começou a pegar fogo!")


class Vingadores:
    def __init__(self, local, qtd_agua):
        self.local = local
        self.qtd_agua = qtd_agua
        self.caminho = []
        self.capacidadeAtual = qtd_agua
        self.trajeto = [] 

    def __str__(self):
        return f"Brigada se encontra no local {self.local}, com a de água = {self.capacidadeAtual}/{self.qtd_agua}."
    
    def andando(self, grafo):
        print(f"\n Equipe se encontra aqui: {self.local} e essa é a quantidade de água: {self.capacidadeAtual}/{self.qtd_agua}")

        # andando até o fogo
        distancia, anterior = dijkstra(grafo, self.local)
        ate_fogo = float('inf')
        destino = None

        for i in grafo:
            if grafo[i]["info"][3] == 1 and distancia[i] < ate_fogo:
                ate_fogo = distancia[i]
                destino = i

        #primeiras verificações
        if self.capacidadeAtual == 0:
            print("Sem água. Procurando ponto de reabastecimento")
            self.abastecer(grafo)
            return
        
        if grafo[self.local]["info"][3] == 1 and self.capacidadeAtual > 0:
            print("Fogo no local")
            self.apagar(grafo, destino)
            return
        

        if destino:
            self.caminho = reconstroi(anterior, self.local).get(destino)
            if self.caminho and len(self.caminho) > 1:
                proximo = self.caminho[1]
                print(f"Indo de {self.local} para {proximo} apagar fogo em {destino}")
                self.local = proximo
                self.trajeto.append(proximo)
            else:
                print("Já está no destino do fogo.")
                self.apagar(grafo, destino)

        else:
            print("Nenhum fogo conhecido. Esperando instruções.")

    def apagar(self,grafo, i):
        fogo=grafo[i]["info"][0]
        if fogo <= self.capacidadeAtual:
            self.capacidadeAtual -= fogo
            grafo[i]["info"][0] = 0 
            grafo[i]["info"][3] = -1

        else:
            grafo[i]["info"][0] -= self.capacidadeAtual
            self.capacidadeAtual = 0
    
    def abastecer(self, grafo):
        distancia, anterior = dijkstra(grafo, self.local)
        menor = float('inf')
        destino = None

        for v in grafo:
            isPosto = grafo[v]["info"][1]
            isLago = grafo[v]["info"][2]
            if (isPosto or isLago) and distancia[v] < menor:
                menor = distancia[v]
                destino = v

        if destino:
            print(f"Indo reabastecer: {self.local} → {destino}")
            self.caminho = reconstroi(anterior, self.local).get(destino)

            if self.local != self.caminho[-1]:  # Ainda não chegou ao destino
                proximo = self.caminho[self.caminho.index(self.local) + 1]
                print(f"Movendo de {self.local} para {proximo} para reabastecer.")
                self.local = proximo
                self.trajeto.append(proximo)
            else:
                print(f"Chegou no destino {self.local}. Reabastecendo.")
                self.capacidadeAtual = self.qtd_agua


def imprimirTrajetos(grafo, brigadas):
    print("\n=== 🔎 VISUALIZAÇÃO DO GRAFO COM ESTADOS ===")

    # Coleta todos os vértices que fazem parte do caminho de alguma brigada
    em_trajeto = set()
    for b in brigadas:
        em_trajeto.update(b.trajeto)

    for vertice in sorted(grafo.keys()):
        info = grafo[vertice]["info"]
        marcadores = []

        if info[3] == 1:
            marcadores.append("🔥 Fogo")
        elif info[3] == -1:
            marcadores.append("✅ Apagado")
        elif info[3] == 2:
            marcadores.append("❌ Queimado")

        if info[1]:
            marcadores.append("🧑‍🚒 Posto")
        if info[2]:
            marcadores.append("💧 Lago")

        if vertice in em_trajeto:
            marcadores.append("🟢 Visitado")

        marcador_str = " | ".join(marcadores) if marcadores else "Sem alerta"
        vizinhos_str = ", ".join([f"{viz} (custo {custo})" for viz, custo in grafo[vertice]["vizinhos"]])

        print(f"{vertice}: {marcador_str}")
        print(f"  ↳ Vizinhos: {vizinhos_str}")


# ==== EXECUÇÃO TESTE ====

# Inicializa grafo com postos, coleta e fogo
criar_postos(grafo)
criar_coleta(grafo)
lagos = [k for k in grafo if grafo[k]["info"][2]]   
postos = [k for k in grafo if grafo[k]["info"][1]]
criarfogo(grafo, postos, lagos)

# Mostra estado inicial
print("\n=== Estado inicial do grafo ===")
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

# Propagação inicial
print("\n=== Propagando fogo... ===")
propagacao(grafo)

# Cria brigadas nos postos
brigadas = []
for p in postos:
    b = Vingadores(p, qtd_agua = 2)
    brigadas.append(b)

turno = 0
tempo_fogo = {}

print("\n=== Simulando turnos até o fogo acabar ===")
while em_chamas(grafo):
    print(f"\n------ TURNO {turno} ------")
    
    # Atualiza tempo de fogo
    for vertice in grafo:
        if grafo[vertice]["info"][3] == 1:
            tempo_fogo[vertice] = tempo_fogo.get(vertice, 0) + 1
            if tempo_fogo[vertice] >= 4:
                grafo[vertice]["info"][3] = 2  # queimado
                print(f"💀 O vértice {vertice} queimou completamente após 4 turnos!")

    # Diminui intensidade do fogo com o tempo
    for vertice in grafo:
        if grafo[vertice]["info"][3] == 1:
            if grafo[vertice]["info"][0] > 0:
                grafo[vertice]["info"][0] -= 1
                print(f"🔥 O fogo em {vertice} perdeu intensidade! Agora precisa de {grafo[vertice]['info'][0]} de água.")
            if grafo[vertice]["info"][0] == 0:
                grafo[vertice]["info"][3] = -1
                print(f"✅ O fogo em {vertice} apagou sozinho por falta de combustível.")

    # Ações das brigadas
    for b in brigadas:
        b.andando(grafo)

    # Propagação do fogo
    propagacao(grafo)

    turno+=1

# Mostra caminhos percorridos
print("\n=== Caminhos percorridos pelas brigadas ===")
for b in brigadas:
    print(f"Brigada iniciou em {b.trajeto[0]} e percorreu:")
    print(" → ".join(b.trajeto))

# Imprime grafo com marcações
imprimirTrajetos(grafo, brigadas)



        


