import sys
import os


original_stdout = sys.stdout

def gerar_relatorio(arquivo="relatorio.txt"):

    url = os.path.join(os.path.dirname(__file__), arquivo)
    sys.stdout = open(url, "w", encoding="utf-8")
