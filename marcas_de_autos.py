
marcas_file = "C:\\Users\\monet\\OneDrive - Universidad Autonoma de Nuevo León\\Mis cursos\\CURSOS EXTRA\\CURSO PYTHON DALTO\\CodigosGIT3.1\\marcas.txt"


with open("marcas_file","w+") as f:
    marcas=["Audi\n","Alfa Romeo\n","BMW\n","Mercedes Benz\n"]
    f.writelines(marcas)
    f.seek(0,0)

    for linea in f:
        print(linea)
    
