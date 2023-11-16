import json

Original=[
    ['correo','nombre','telefono'],
    ['juan@gmail.com','Juan','8123232323'],
    ['maria@gmail.com','Maria','5545454545'],
    ['diana@homail.com','Diana','4490909090']
]

with open("archivo.json","w+") as f:
    json.dump(Original,f,indent=4)

with open("archivo.json","r") as f:
    recuperados=json.load(f)
    
print(recuperados)
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==recuperados)