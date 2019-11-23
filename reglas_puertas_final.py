import  FNC_PROYECT_AV as fn
import DPLL_AV as dp
import inicio_Visu as visualizacion
#importando dpll y fnc
u = "uY-vY-wY-xY-yY-z" 
v = "-uYvY-wY-xY-yY-z"                     
w = "-uY-vYwY-xY-yY-z"                   
x = "-uY-vY-wYxY-yY-z"                 
y = "-uY-vY-wY-xYyY-z"                   
z = "-uY-vY-wY-xY-yYz"               
#es la regla de que solo una puerta puede tener el diploma, cuando negamos el resto hacemos que solo una tenga el diploma
letras = [u,v,w,x,y,z]
a="u"
b="v"
c="-x"
d="uOw"
e="-uY-x"
f="vOu"
g="-w"
h="v"
i="y"
j="-xY-w"
k="-zY-w"
l="z"



##########################
#funciones de apoyo para combinaciones de las letras y sus negadores 
##########################
def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]


def combinaciones(c, n):
    
    return [s for s in potencia(c) if len(s) == n]




###############
#negadores retorna una lista de listas de las reglas u-z en las cuales se niegan todas excepto 3 
###############    
def negadores_de_el_resto(lista1, lista2):
    lista3=[]
    for aux1 in lista1:
        lista4= [x for x in lista2]
        for h in aux1:
            if(h in lista4):
                lista4.remove(h)        
        for i in range(9):
            if(len(lista4[i])==1):
                lista4[i]= "-" + lista4[i] 
            elif(len(lista4[i])==2):
                lista4[i] = lista4[i][1]
            elif(len(lista4[i])==3):
                if(lista4[i][1]=="O"):
                    lista4[i] = "-" + lista4[i][0] + "Y" + "-" + lista4[i][2]
                if(lista4[i][1]=="Y"):
                    lista4[i] = "-" + lista4[i][0] + "O" + "-" + lista4[i][2]         
            elif(len(lista4[i])==5):
                if(lista4[i][2]=="Y"):
                    lista4[i] = lista4[i][1] + "O" + lista4[i][4]
                if(lista4[i][2]=="O"):
                    lista4[i] = lista4[i][1] + "Y" + lista4[i][4]
        var = aux1 + lista4
        lista3.append(var)
                
    return lista3
#################
#convertir retorna un estring con las reglas unidas por una Y
################
def convertir(list_of_list):
    text = ""
    for i in list_of_list:
        text += i + "Y"
    return text
    

var= negadores_de_el_resto(combinaciones([a,b,c,d,e,f,g,h,i,j,k,l], 3), [a,b,c,d,e,f,g,h,i,j,k,l])
#
#print(formaClausal(w))
#print(ff)

def union(u):
    conjuncion= ""
    for g in letras:
        for t in u:
            conjuncion += convertir(t)+ g 
            msg, dicc = dp.DPLL(fn.formaClausal(conjuncion),{})
            if (msg == "Satisfacible"):
                print(type(dicc))
                return msg , dicc
            else:conjuncion=""

mensaje, diccionar = union(var)

print(mensaje, diccionar)
llaves = diccionar.keys()
valores = diccionar.items()
lista_final = []
reglas_fin = ""

print(list(llaves),list( valores)[0][1])
for it in range(len(list(valores))):
    print(list(valores)[it])
    if( list(valores)[it][1] == 0   ):
        reglas_fin += "-" + list(llaves)[it]
        lista_final.append(reglas_fin)
        reglas_fin = ""
        continue
    elif(list(valores)[it][1] == 1 ):
        reglas_fin += list(llaves)[it]
        lista_final.append(reglas_fin)
        reglas_fin = ""
        continue
print(lista_final)



###########
#aquí va la parte de ilustracion 
###########
visualizacion.imprimir_imagen(lista_final,1)    
    
    
    
    
    
    
    
    