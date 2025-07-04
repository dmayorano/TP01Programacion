import json

# Copiá acá tus 3 diccionarios exactamente como están:
clientela = {
    "39592834": {
        "activo": True,
        "nombre": "Micaela Robles",
        "edad": 26,
        "telefonos": {
            "movil": "11 5002415123",
            "alterno": ""
        }
    },
    "431223345": {
        "activo": True,
        "nombre": "Martin Gonzales",
        "edad": 26,
        "telefonos": {
            "movil": "11 500245621",
            "alterno": "1124070486"
        }
    },
    "33451678": {
        "activo": True,
        "nombre": "Fito Parrez",
        "edad": 26,
        "telefonos": {
            "movil": "11 500241234",
            "alterno": ""
        }
    },
    "15675431": {
        "activo": True,
        "nombre": "Gonzalo Robledo",
        "edad": 26,
        "telefonos": {
            "movil": "11 500241252",
            "alterno": ""
        }
    },
    "423411123": {
        "activo": True,
        "nombre": "Martin Serin",
        "edad": 26,
        "telefonos": {
            "movil": "11 500241211",
            "alterno": ""
        }
    },
    "11234124": {
        "activo": True,
        "nombre": "Gaston Soldati",
        "edad": 26,
        "telefonos": {
            "movil": "11 695241234",
            "alterno": ""
        }
    },
    "41234124": {
        "activo": True,
        "nombre": "Marcelo Chavez",
        "edad": 26,
        "telefonos": {
            "movil": "11 531241234",
            "alterno": ""
        }
    },
    "45212342": {
        "activo": True,
        "nombre": "Fernando Alonso",
        "edad": 26,
        "telefonos": {
            "movil": "11 498241234",
            "alterno": ""
        }
    },
    "2142142": {
        "activo": True,
        "nombre": "Martin Gimenez",
        "edad": 26,
        "telefonos": {
            "movil": "11 233241234",
            "alterno": ""
        }
    },
    "4042132": {
        "activo": True,
        "nombre": "Lionel Messi",
        "edad": 26,
        "telefonos": {
            "movil": "11 503241234",
            "alterno": ""
        }
    },
    "43404740": {
        "activo": True,
        "nombre": "Agustin Avella",
        "edad": 23,
        "telefonos": {
            "movil": "11 503241234",
            "alterno": "11 41231233"
        }
    }
}  # Pegá tu clientela completa
habitaciones = {
    "1": {
        "disponible": True,
        "capacidad": 2,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "2": {
        "disponible": True,
        "capacidad": 4,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "3": {
        "disponible": True,
        "capacidad": 2,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "4": {
        "disponible": True,
        "capacidad": 6,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": False,
            "balcon": False
        }
    },
    "5": {
        "disponible": True,
        "capacidad": 4,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "6": {
        "disponible": True,
        "capacidad": 2,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "7": {
        "disponible": True,
        "capacidad": 3,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "8": {
        "disponible": True,
        "capacidad": 4,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "9": {
        "disponible": True,
        "capacidad": 2,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": False,
            "balcon": True
        }
    },
    "10": {
        "disponible": True,
        "capacidad": 6,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": False
        }
    }
}
reservas = {
    "1": {
        "disponible": True,
        "capacidad": 2,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "2": {
        "disponible": True,
        "capacidad": 4,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "3": {
        "disponible": True,
        "capacidad": 2,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "4": {
        "disponible": True,
        "capacidad": 6,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": False,
            "balcon": False
        }
    },
    "5": {
        "disponible": True,
        "capacidad": 4,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "6": {
        "disponible": True,
        "capacidad": 2,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "7": {
        "disponible": True,
        "capacidad": 3,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "8": {
        "disponible": True,
        "capacidad": 4,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": True
        }
    },
    "9": {
        "disponible": True,
        "capacidad": 2,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": False,
            "balcon": True
        }
    },
    "10": {
        "disponible": True,
        "capacidad": 6,
        "costoPorDia": 10000,
        "servicios": {
            "aire acondicionado": True,
            "frigobar": True,
            "balcon": False
        }
    }
}  # Pegá habitaciones completas
reservas = {
    "20/12/2025-1": {
        "nombre":"Micaela Robles",
        "dni": "39592834",
        "nroHabitacion": 1,
        "activo": True,
        "cantidadPersonas": 2,
        "fechaDeEntrada": '02/06/2025',
        "fechaDeSalida": "06/06/2025",
        "metodoDePago": "Efectivo",
        "totalPagar": 20000
    },
    "15/10/2025-2": {
        "nombre":"Martin Gonzales",
        "dni": "431223345",
        "nroHabitacion": 2,
        "activo": True,
        "cantidadPersonas": 2,
        "fechaDeEntrada": '02/05/2025',
        "fechaDeSalida": "06/05/2025",
        "metodoDePago": "Efectivo",
        "totalPagar": 20000
    },
    "20/12/2025-3": {
        "nombre":"Fito Parrez",
        "dni": "33451678",
        "nroHabitacion": 3,
        "activo": True,
        "cantidadPersonas": 2,
        "fechaDeEntrada": '10/06/2025',
        "fechaDeSalida": "16/06/2025",
        "metodoDePago": "Efectivo",
        "totalPagar": 60000
    },
    "25/12/2025-4": {
        "nombre":"Gonzalo Robledo",
        "dni": "15675431",
        "nroHabitacion": 4,
        "activo": True,
        "cantidadPersonas": 4,
        "fechaDeEntrada": '20/06/2025',
        "fechaDeSalida": "25/06/2025",
        "metodoDePago": "Tarjeta",
        "totalPagar": 50000
    },
    "01/01/2026-5": {
        "nombre":"Martin Serin",
        "dni": "423411123",
        "nroHabitacion": 5,
        "activo": True,
        "cantidadPersonas": 3,
        "fechaDeEntrada": '01/07/2025',
        "fechaDeSalida": "05/07/2025",
        "metodoDePago": "Efectivo",
        "totalPagar": 40000
    },
    "15/06/2026-6": {
        "nombre":"Cristian",
        "dni": "11234124",
        "nroHabitacion": 6,
        "activo": True,
        "cantidadPersonas": 2,
        "fechaDeEntrada": '15/07/2025',
        "fechaDeSalida": "20/07/2025",
        "metodoDePago": "Tarjeta",
        "totalPagar": 50000
    },
    "20/08/2026-7": {
        "nombre":"Marcelo Chavez",
        "dni": "41234124",
        "nroHabitacion": 7,
        "activo": True,
        "cantidadPersonas": 4,
        "fechaDeEntrada": '20/08/2025',
        "fechaDeSalida": "25/08/2025",
        "metodoDePago": "Efectivo",
        "totalPagar": 50000
    },
    "10/09/2026-8": {
        "nombre":"Fernando Alonso",
        "dni": "45212342",
        "nroHabitacion": 8,
        "activo": True,
        "cantidadPersonas": 3,
        "fechaDeEntrada": '10/09/2025',
        "fechaDeSalida": "15/09/2025",
        "metodoDePago": "Tarjeta",
        "totalPagar": 50000
    },
    "05/10/2026-9": {
        "nombre":"Martin Gimenez",
        "dni": "2142142",
        "nroHabitacion": 9,
        "activo": True,
        "cantidadPersonas": 2,
        "fechaDeEntrada": '05/10/2025',
        "fechaDeSalida": "10/10/2025",
        "metodoDePago": "Efectivo",
        "totalPagar": 50000
    },
    "15/11/2026-10": {
        "nombre":"Lionel Messi",
        "dni": "4042132",
        "nroHabitacion": 10,
        "activo": True,
        "cantidadPersonas": 6,
        "fechaDeEntrada": '15/11/2025',
        "fechaDeSalida": "20/11/2025",
        "metodoDePago": "Tarjeta",
        "totalPagar": 50000
    }
}  # Pegá reservas completas

# Guardar como JSON
with open("clientes.json", "w", encoding="utf-8") as archivo:
    json.dump(clientela, archivo, indent=4, ensure_ascii=False)

with open("habitaciones.json", "w", encoding="utf-8") as archivo:
    json.dump(habitaciones, archivo, indent=4, ensure_ascii=False)

with open("reservas.json", "w", encoding="utf-8") as archivo:
    json.dump(reservas, archivo, indent=4, ensure_ascii=False)

print("¡Datos convertidos y guardados en archivos JSON con éxito!")
