import random

def mapmaker(i, j):
    #i linhas , j colunas cria e incializa uma matriz com zeros
    M = []
    for x in range(i):
        A = []
        for y in range(j):
                A.append(0)

        M.append(A)

    # print(M)
    return M
def mapfill(r, m=[]):
    #só pra preencher automaticamente os valores. deve ter um método automático em python, mas um loop serve. Come memória? E daí
    for x in range(len(m)):
        for y in range(len(m[0])):
            if m[x][y] == 0:
                m[x][y] = r

def statecode(b,c=[]):
    #calcular a posição ordinal de um ponto [i,j] na matriz Q, seguindo a organização descrita abaixo
    return (b*c[0])+c[1]
def nextState(x, a, b, s=[]):
    # ponto com coordenads, c=[i,j] e x ação a ser tomada = [n,s,l,o], [a,b] map dimensions.
    # mover respeitando constraints dimensionais. deixei check de parede fora

    c = s[:] #copiar a lista pra evitar erro
    if x == 0:
        #norte
        if not((c[0]+1) > a):
            #check para não extrapolar coordenadas. se extrapolar, fica no mesmo canto
            c[0] = c[0]+1

    elif x == 1:
        #sul
        if not((c[0]-1)<0):
            c[0] = c[0]-1
    elif x == 2:
        #leste
        if not((c[1]+1) > b):
            c[1] = c[1] + 1
    elif x == 3:
        #oeste
        if not ((c[1] - 1) < 0):
            c[1] = c[1] - 1

    return c

def qualitestimate (y, alpha, gamma, c=[], m=[], q=[]):
    #y é a ação tomada. alpha e gamma parametros pra bellman e q.
    # c é uma lista com as coordenadas do estado atual, m é a matriz de recompensa de cada estágio e q é a matriz de qualidade do q-learning
    x = statecode(4,c)
    next_state = nextState(y, 2, 3, c)
    next_x = statecode(4,next_state)
    next_state_reward = m[next_state[0]][next_state[1]]
    next_value_estimate = max(Q[next_x])
    next_Bellman = next_state_reward + gamma*next_value_estimate
    updated_state_value = Q[x][y] + alpha*(next_Bellman-Q[x][y])
    Q[x][y] = updated_state_value
    # print("estimate: ", c, "at: ",x,y, "and ",next_state, "to see: ",Q[next_x])
    # print(Q)

def policywriter (Q=[], p=[],t=[]):
    W = mapmaker(3,4)
    for x in range(3):
        for y in range(4):
            statecodes = (x*4)+y
            # print(statecodes)
            if statecodes in t:
                W[x][y] = max(Q[statecodes])
            else:
                W[x][y] = p[Q[statecodes].index(max(Q[statecodes]))]

    return W

def printamatrix(Q=[]):
    #auxiliar pra imprimir linha a linha. Sim, eu sou acostumado com baixo nível e gosto de implementar
    for x in range(len(Q)):
        print(Q[x])


#------- let's go -----

M = mapmaker(3, 4)
#recompensa dos estados terminais
M[0][3] = 0.2
M[1][3] = -1
M[2][3] = 1

R = [-0.4, -0.04] #recompensa genérica

# print(M)
wall = [5] #estados parede
tStates = [3, 7, 11] #estados terminais

#os elementos da matriz foram contados a partir das linhas, numa configuração como:
#    0 1 2  3
# 0 |0 1 2  3
# 1 |4 5 6  7
# 2 |8 9 10 11

#desenhar essa matriz foi a única coisa não generalista neste código

Q = mapmaker(12, 4) #matriz Q-learning

for x in range(len(tStates)):
    for y in range(len(Q[0])):
        Q[tStates[x]][y] = M[x][3]
        #adicionando os estados terminais de forma preguiçosa e não generalista
        # e que teria que ser refeita se mudassem os estados terminais

# print(Q)
#admitindo alfa e gama
alpha = 0.5
gamma = 0.8
c = [0, 0] #ponto de partida
P = ["norte", "sul", "leste", "oeste"]
hungry = True #parametro logico pra saber se o algoritmo ainda tá buscando o estado terminal. Usei hungry por uma analogia metafórica em que os estados terminais são a comida kkk
step = 0 #conta quantos passos até achar um estado terminal
rounds = 5 #decide quantas vezes o laço roda

#testa dois casos de recompensas
mapfill(R[0], M) #0.4
# mapfill(R[1], M) #0.04

while(hungry):
    # escolhe a ação a ser tomada n aleatoriamente, seguindo pontos cardeais
    # em que P = [norte, sul, leste, oeste] com os indices correspondentes à direção tomada
    n = random.randint(0, 3)
    # print(n)
    next_c = nextState(n, 2, 3, c)
    # print("step: ", c, P[n], next_c)
    # calcula a recompensa da ação recebida e observa o estado a ser alcançado, estimando o valor e atualizando a tabela Q

    qualitestimate(n, alpha, gamma, c, M, Q)

    #se estado a ser alcançado for uma parede
    if (statecode(4, next_c) in wall):
        next_c = c

    print(c,"(", statecode(4,c),") ", P[n],next_c ,"(", statecode(4,next_c),") ")
    print("------------------------------------")

    c = next_c
    step = step +1
    #se estado a ser alcançado for um estado terminal
    if (statecode(4, next_c) in tStates):
        hungry = False
        print(step)
        print("Q: ")
        printamatrix(Q)
        print("politica: ")
        printamatrix(policywriter(Q, P, tStates))

    #reitera
    if not hungry:
        if rounds == 0:
            check = input("reiterar?: s/n ")
            if check == 's':
                hungry = True
                step = 0
                c = [0, 0]
                again = input("number of rounds? [1 - 3]")
                rounds = [1, 2, 3].index(int(again))
        else:
            rounds = rounds -1
            hungry = True
            step = 0
            c = [0, 0]
