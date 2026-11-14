# Trabalho 01 - Estrutura de Dados; 
# Implementação do tipo abstrato de dados Pilha(estática);
# Prof. Dr. Franklin César Flores
# Alunos: Lucas Santana Zanzim RA: 143393
#         Gabriel Lopes;

# definição do tipo Pilha com função class, possui elem, um vetor onde os elementos da pilha serão armazenados e topo, 
# posição do último elemento da pilha;
# TamMax é uma constante que define o tamanho físico do vetor;
class Pilha:
    elem: list
    TamMax: int
    topo: int
    
    def __init__(self):
        self.TamMax = 100
        self.elem = [0] * (self.TamMax + 1)
        self.topo = -1


# Esvazia a pilha declarada, onde o topo da pilha receberá o valor -1, ou seja, não possui nenhum elemento armazenado;
def inicializa_pilha(self):
    self.topo = -1


# Verifica se a pilha está vazia ou não, retornando Verdadeiro ou Falso;
def pilha_vazia(P: Pilha) -> bool:
    return P.topo == -1


# Verifica se a pilha está cheia ou não, retornando Verdadeiro ou Falso;
def pilha_cheia(P: Pilha) -> bool:
    return P.topo == P.TamMax


# Coloca um novo valor no topo da Pilha;
def empilha(P: Pilha, x: int) -> None:
    if pilha_cheia(P):
        print("<erro>")
    P.topo = P.topo + 1
    P.elem[P.topo] = x

# Retira um valor do topo da Pilha;
def desempilha(P: Pilha):
    if pilha_vazia(P):
        print("<erro>")
    x = P.elem[P.topo]
    P.topo = P.topo - 1
    return x
        
# Retorna o valor que está no topo da Pilha;
def elemento_do_topo(P):
    if not pilha_vazia(P):
        return P.elem[P.topo]
    else:
        print("<erro>")