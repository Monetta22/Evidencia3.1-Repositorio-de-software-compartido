
ruta = "C:\\Users\\monet\\OneDrive - Universidad Autonoma de Nuevo León\\Mis cursos\\CURSOS EXTRA\\CURSO PYTHON DALTO\\CodigosGIT3.1\\agenda.csv"

Datos=[]

with open(ruta,"r") as f:
    for linea in f:
        lista=linea.split("|")
        lista[2]=lista[2].replace("\n","")
        Datos.append(lista)
        
        
print(">> Contenido de la nueva lista.\n")
print(Datos)