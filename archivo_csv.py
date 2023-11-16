import os 
Entradas=[
    ['correo','nombre','telefono'],
    ['juan@gmail.com','Juan','8123232323'],
    ['maria@gmail.com','Maria','5545454545'],
    ['diana@homail.com','Diana','4490909090']
]
for e in Entradas:
    print(f'{e[0]}|{e[1]}|{e[2]}')

 
print(">> Contenido de la lista.\n")
print(Entradas)

if os.path.exists("agenda.csv"):
    if (os.path.exists("agenda.bak")):
        os.remove("agenda.bak")
        os.rename("agenda.csv","agenda.bak")

with open("agenda.csv","w+") as f:
    for e in Entradas:
        f.write(f"{e[0]}|{e[1]}|{e[2]}\n")

    print("\n>> Contenido del archivo.\n")
with open("agenda.csv") as f:
    print(f.read())