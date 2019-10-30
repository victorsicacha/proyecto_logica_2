import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

def imprimir_imagen(A , B):
    figuras, cuadricula = plt.subplots()
    cuadricula.get_xaxis().set_visible(False)
    cuadricula.get_yaxis().set_visible(False)
    ###
    ###
    archivo_imagen = plt.imread("Ebano_D.png",format="png")
    imagen1 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen1.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Caoba_D.png",format="png")
    imagen2 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen2.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Cerezo_D.png",format="png")
    imagen3 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen3.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Roble_D.png",format="png")
    imagen4 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen4.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Eucalipto_D.png",format="png")
    imagen5 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen5.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Pino_D.png",format="png")
    imagen6 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen6.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Ebano_M.png",format="png")
    imagen7 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen7.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Caoba_M.png",format="png")
    imagen8 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen8.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Cerezo_M.png",format="png")
    imagen9 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen9.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Roble_M.png",format="png")
    imagen10 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen10.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Eucalipto_M.png",format="png")
    imagen11 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen11.image.axes = cuadricula
    
    archivo_imagen = plt.imread("Pino_M.png",format="png")
    imagen12 = OffsetImage(archivo_imagen,zoom = 0.2)
    imagen12.image.axes = cuadricula

    direccion = {}
    direccion[1] = [0.1, 0.467]
    direccion[2] = [0.26, 0.467]
    direccion[3] = [0.42, 0.467]
    direccion[4] = [0.58, 0.467]
    direccion[5] = [0.74, 0.467]
    direccion[6] = [0.90, 0.467]
    
    puerta_mala = AnnotationBbox(imagen7, direccion[1], frameon=False)
    puerta_mala2 = AnnotationBbox(imagen8, direccion[2], frameon=False)
    puerta_mala3 = AnnotationBbox(imagen9, direccion[3], frameon=False)
    puerta_mala4 = AnnotationBbox(imagen10, direccion[4], frameon=False)
    puerta_mala5 = AnnotationBbox(imagen11, direccion[5], frameon=False)
    puerta_mala6 = AnnotationBbox(imagen12, direccion[6], frameon=False)
    
    cuadricula.add_artist(puerta_mala)
    cuadricula.add_artist(puerta_mala2)
    cuadricula.add_artist(puerta_mala3)
    cuadricula.add_artist(puerta_mala4)
    cuadricula.add_artist(puerta_mala5)
    cuadricula.add_artist(puerta_mala6)
    
    for l in A:
        if '-' not in l:
            num = 0
            if "u" in l:
                num = 1
            elif "v" in l:
                num = 2
            elif "w" in l:
                num = 3
            elif "x" in l:
                num = 4
            elif "y" in l:
                num = 5
            elif "z" in l:
                num = 6
            diploma = AnnotationBbox(eval("imagen"+str(num)), direccion[num], frameon=False)
            cuadricula.add_artist(diploma)
    
    figuras.savefig("result_" + str(B) + ".png" )



F=[["-u","v","-w","-x","-y","-z"]]

imprimir_imagen(F,2)






