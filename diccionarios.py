##diccionarios:

##son colecciones de datos 
## cada elemento en un diccionario
## se puede dividir en
##   1.
##   2. valor:
##   ejemplo de diccionario:
## para caracterizar un pais:

pais = {
    "nombre": "colombia",
    "capital": "Bogota",
    "idioma": "español",
    "poblacion": 51,
    "superficie": 1142748,
    "moneda": "peso colombiano",
    "ciudades":[
        "bogota",
        "medellin",
        "cali",
        "barranquilla",
        "cartagena"
    ]
}

#acceder a propiedades:
print("capital de colombia:" , pais["capital"])
print("y se habla:" , pais["idioma"])
print("habitantes:" , pais["poblacion"])
print("y sus ciudades son:")
for ciudad in pais ["ciudades"]:
    print(ciudad)