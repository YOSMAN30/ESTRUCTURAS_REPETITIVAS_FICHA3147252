# Colección de países
paises = [
    {
        "nombre": "colombia",
        "capital": "Bogota",
        "moneda": "peso colombiano",
        "ciudades": [
            {
                "nombre": "bogota",
                "poblacion": 8.2,
                "fundacion": 1538,
            },
            {
                "nombre": "medellin",
                "poblacion": 2.6,
                "fundacion": 1675
            },
            {
                "nombre": "cali",
                "poblacion": 2.2,
                "fundacion": 1536,
            }
        ]
    },
    {
        "nombre": "peru",
        "capital": "lima",
        "moneda": "sol",
        "ciudades": [
            {
                "nombre": "lima",
                "poblacion": 2.5,
                "fundacion": 1535,
            },
            {
                "nombre": "cuzco",
                "poblacion": 2.2,
                "fundacion": 1100,
            }
        ]
    },
    {
        "nombre": "francia",
        "capital": "paris",
        "moneda": "euro",
        "ciudades": [
            {
                "nombre": "marsella",
                "poblacion": 8.7,
                "fundacion": 600,
            },
            {
                "nombre": "lion",
                "poblacion": 5.15,
                "fundacion": 43,
            }
        ]
    },
    {
        "nombre": "venezuela",
        "capital": "caracas",
        "moneda": "bolivares",
        "ciudades": [
            {
                "nombre": "maracaibo",
                "poblacion": 2.5,
                "fundacion": 1529,
            },
            {
                "nombre": "carabobo",
                "poblacion": 2.5,
                "fundacion": 1824,
            }
        ]
    }
]

# Iterar cada país e imprimir información
print("-------------------")
print("Recorrido de países")
print("-------------------")

for pais in paises:
    print("Nombre:", pais["nombre"])
    print("Capital:", pais["capital"])
    print("Ciudades principales de", pais["nombre"])
    
    for ciudad in pais["ciudades"]:
        print(f"- {ciudad['nombre']}: Población: {ciudad['poblacion']} millones, Fundación: {ciudad['fundacion']}")
    
    print("----------------------")
    