import pickle
Original=[
    ['correo','nombre','telefono'],
    ['juan@gmail.com','Juan','8123232323'],
    ['maria@gmail.com','Maria','5545454545'],
    ['diana@homail.com','Diana','4490909090']
]
print("\n>> Serialización a Pickle.\n")
Original_pickle=pickle.dumps(Original)
print(Original_pickle)
print("\n>> Deserialización desde Pickle.\n")
Nueva_Lista=pickle.loads(Original_pickle)
print(Nueva_Lista)
print(type(Nueva_Lista))
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==Nueva_Lista)