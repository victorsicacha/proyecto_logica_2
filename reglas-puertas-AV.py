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

def imprime_ordenado(c):
    lista=[]
    for e in list(sorted(c, key=lambda s: (len(s), s))):
        for y in e:
            if(y not in lista):
                lista.append(y)
                continue
    return lista
def imprime_ordenado2(c):
    lista=[]
    for e in sorted(c, key=lambda s: (len(s), s)):
        lista.append(e)
    return lista

def combinaciones(c, n):
    
    return [s for s in potencia(c) if len(s) == n]



#print(imprime_ordenado2(combinaciones(["a","b","c","d","e","f","g","h","i","j","k","l"], 3)))

def negadores_de_el_resto(lista1, lista2):
    lista3=[]
    for aux1 in lista1:
        lista4= [x for x in lista2]
        for h in aux1:
            if(h in lista2):
                lista4.remove(h)        
        for i in range(9):
            lista4[i]=  lista4[i] + "-"
        
        var = aux1 + lista4
        lista3.append(var)
                
    return lista3
#fin = negadores_de_el_resto(imprime_ordenado2(combinaciones(["u","v","x-","uwO","ux--Y","vuO","w-","v","y","xw--Y","zw--Y","z"], 3)),["u","v","x-","uwO","ux--Y","vuO","w-","v","y","xw--O","zw--o","z"])
print(negadores_de_el_resto(imprime_ordenado2(combinaciones(["a","b","c","d","e","f","g","h","i","j","k","l"], 3)), ["a","b","c","d","e","f","g","h","i","j","k","l"]))
#imprime las combinaciones posibles de cuando 3 de las letras son verdaderas 
#y el resto falsas, crea una lista de listas que contienen todas las reglas que se usarán 































