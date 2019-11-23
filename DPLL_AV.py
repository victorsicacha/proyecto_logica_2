def clausula_unitaria(U):
    flag = False
    posicion = -1
    for i in range(len(U)):
        if(len(U[i]) == 0):
            return (True, False, posicion)
        elif(len(U[i]) == 1):
            flag = True
            posicion = i
            break
    return(False, flag, posicion)

def claUnit(S):
    for i in S:
        if(len(i) == 1):
            return True
    return False

def Complemento(l):
    if(l[0] == '-'):
        return l.replace('-', '')
    else:
        return '-' + l

def quitar_clausula(S, l):
    S.remove(l)
    if(len(l) >= 1):
        if(l[0] == '-'):
            L = l.replace('-', '')
        else:
            L = l[0]
        for i in S:
            if L in i:
                S.remove(i)
    return S

def quita_negacion(S, l):
    if(len(l) >= 1):
        L = l[0]
        L = Complemento(L)
        for i in S:
            if L in i:
                i.remove(L)
    return S

def unitPropagate(clausulas, Interpretacion):
    vacia, unitaria, posicion = clausula_unitaria(clausulas)
    while(vacia == False and claUnit(clausulas)):
        for i in clausulas:
            clausulas = quitar_clausula(clausulas, i)
            clausulas = quita_negacion(clausulas, i)
            if(len(i) == 0):
                return 'Insatisfacible',  Interpretacion
            if(i[0] == '-'):
                 Interpretacion[Complemento(i[0])] = 0
            else:
                 Interpretacion[i[0]] = 1
    return clausulas,  Interpretacion

def lDicc(D):
    A = D.copy()
    for i in A:
        if(i[0] == '-'):
            A.pop(i)
            i = Complemento(i)
            if(A.get(i) == 0):
                A[i[0]] = 1
            else:
                A[i[0]] = 0
    return A

def DPLL(S, I):
    S, I = unitPropagate(S, I)

    if(S == "Insatisfacible"):
        return 'Insatisfacible', "{}"
    if(len(S) == 0):
        return 'Satisfacible', lDicc(I)
    for i in S:
        if(len(i) == 0):
            return 'Insatisfacible', "{}"
    L = S[0]
    L = Complemento(Complemento(L[0]))
    cop = I.copy()
    if(L[0] == '-'):
        cop[Complemento(L[0])] = 0
    else:
        cop[L[0]] = 1

    Sp = S.copy()
    Sp.append(L[0])

    aux1, aux2 = DPLL(Sp, cop)
    if(aux1 == 'Satisfacible'):
        return 'Satisfacible', lDicc(cop)
    else:
        scop = S.copy()
        scop.append(Complemento(L[0]))
        icopy = I.copy()
        if(L[0] == '-'):
            icopy[Complemento(L[0])] = 1
        else:
            icopy[L[0]] = 0
    return DPLL(scop, icopy)


#prueba = [["p", "-q", "r"], ["-p", "q", "-r"], ["-p", "-q", "r"], ["-p", "-q", "-r"]]
##prueba2 = [["p"], ["-p", "q", "-r"], ["q"]]
#prueba4= [['-u'],[ '-v'],[ 'w'], ['-x'], [ '-y '],[ '-z']]#prueba para la regla de que soo una puerta tiene detras el diploma 
##en este caso la unica manera de que sea verdadera es que el valor de verdad de mi W sea igual a 1___{'w': 1, 'u': 0, 'y': 0, 'v': 0, 'z': 0, 'x': 0}


#prueba3 = [["p"], ["-p", "q"], ["-q", "r", "s"]]
#interpretaciones = {}
#msg, dicc_inter = DPLL(prueba4, interpretaciones)
#print(msg, dicc_inter)
