"""
-----------------------------------------------------------------------------------------------
Título: Brayy tirame la goma
Fecha: ...
Autor: ...

Descripción: ...

Pendientes:
- LISTADO DE CLIENTES ACTIVOS: FALTA FILTRAR PARA SÓLO LISTAR LOS CLIENTES ACTIVOS
...
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from datetime import date



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaCliente(clientes):
    ...
    return clientes


def inactivarCliente(_clientes):
    """
    doctring
    """
    dni = input("DNI del cliente a inactivar: ")
    print()
    
    # Se inactiva el cliente sólo si existe
    if dni in _clientes:
        _clientes[dni]["activo"] = False
        print(f"El clientes {dni} fue dado de baja.")
    else:
        print(f"El DNI {dni} es inexistente.")
    
    return _clientes

def listarClientesActivos(clientela):
    """
    Lista todos los clientes activos y sus detalles de tarjetas.
    """
    # Se muestran todos los datos del cliente y el detalle de sus tarjetas
    for dni, otrosDatos in clientela.items():
        if otrosDatos['activo']:  # Filtro para clientes activos
            
            
            print(f"CLIENTE: {dni}")
            print(f"NOMBRE: {otrosDatos.get('nombre', 'No disponible')}")
            
            # Verificar si el cliente tiene edad y sexo antes de imprimir
            print(f"EDAD: {otrosDatos.get('edad', 'No disponible')}")
            print(f"SEXO: {otrosDatos.get('sexo', 'No disponible')}")

            print("TARJETAS:")
            for tarjeta, nombreTarjeta in otrosDatos.get("tarjetas", {}).items():
                if nombreTarjeta:  # No imprimir tarjetas vacías
                    print(f"\t{tarjeta}: {nombreTarjeta}")
            
            print()
            
    
    return


def nuevoCliente(clientela):
    dni= input("Ingresa tu DNI: ")
    if dni in clientela:
        print("El cliente ya existe.")
        return
    
    nombre = input("Ingresa tu nombre: ")
    tarjeta1 = input("Ingresa la primera tarjeta(Opcional): ")
    tarjeta2 = input("Ingresa la segunda tarjeta(Opcional): ")
    tarjeta3 = input("Ingresa la tercera tarjeta(Opcional): ")

    nuevoCliente = {
        "activo": True,
        "nombre": nombre,
        "tarjetas": {
            "tarjeta1": tarjeta1,
            "tarjeta2": tarjeta2,
            "tarjeta3": tarjeta3,
            }
        }
    clientela[dni] = nuevoCliente
    print("Cliente agregado con exito.")
    return


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------


    # Diccionario de datos de clientes: KEY=Documento del cliente, VALUE=Otros datos del cliente
    clientela = {
        "38472910": {
            "activo": True,
            "nombre": "Tomás Ibáñez",
            "tarjetas": {
                "tarjeta1": "MASTER",
                "tarjeta2": "",
                "tarjeta3": ""
            }
        },
        "39592834": {
            "activo": True,
            "nombre": "Micaela Robles",
            "edad": 26,
            "sexo": "F",
            "tarjetas": {
                "tarjeta1": "VISA",
                "tarjeta2": "AMEX",
                "tarjeta3": ""
            }
        },
        "41294837": {
            "activo": True,
            "nombre": "Andrés Quiroga",
            "edad": 31,
            "sexo": "M",
            "tarjetas": {
                "tarjeta1": "AMEX",
                "tarjeta2": "MASTER",
                "tarjeta3": "VISA"
            }
        },
        "40291736": {
            "activo": True,
            "nombre": "Florencia Salas",
            "edad": 25,
            "sexo": "F",
            "tarjetas": {
                "tarjeta1": "MASTER",
                "tarjeta2": "VISA",
                "tarjeta3": ""
            }
        },
        "39284730": {
            "activo": True,
            "nombre": "Rodrigo Cabrera",
            "edad": 37,
            "sexo": "M",
            "tarjetas": {
                "tarjeta1": "AMEX",
                "tarjeta2": "",
                "tarjeta3": ""
            }
        },
        "38817290": {
            "activo": True,
            "nombre": "Elena Ponce",
            "edad": 30,
            "sexo": "F",
            "tarjetas": {
                "tarjeta1": "VISA",
                "tarjeta2": "MASTER",
                "tarjeta3": "AMEX"
            }
        },
        "40671829": {
            "activo": True,
            "nombre": "Matías Barreto",
            "edad": 33,
            "sexo": "M",
            "tarjetas": {
                "tarjeta1": "MASTER",
                "tarjeta2": "",
                "tarjeta3": ""
            }
        },
        "37928192": {
            "activo": True,
            "nombre": "Julieta San Martín",
            "edad": 28,
            "sexo": "F",
            "tarjetas": {
                "tarjeta1": "VISA",
                "tarjeta2": "AMEX",
                "tarjeta3": ""
            }
        },
        "40718293": {
            "activo": True,
            "nombre": "Iván Méndez",
            "edad": 35,
            "sexo": "M",
            "tarjetas": {
                "tarjeta1": "AMEX",
                "tarjeta2": "VISA",
                "tarjeta3": "MASTER"
            }
        },
        "38571820": {
            "activo": True,
            "nombre": "Pamela Córdoba",
            "edad": 34,
            "sexo": "F",
            "tarjetas": {
                "tarjeta1": "MASTER",
                "tarjeta2": "AMEX",
                "tarjeta3": ""
            }
        }
    }

        # Diccionario de datos de productos: KEY=Código de producto, VALUE=Otros datos del producto
    habitaciones = {
        "habitacion 1": {
            "disponible": True,
            "capacidad": 2,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "habitacion 2": {
            "disponible": True,
            "capacidad": 4,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "habitacion 3": {
            "disponible": True,
            "capacidad": 2,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "habitacion 4": {
            "disponible": True,
            "capacidad": 6,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": False,
                "Balcon": False
            }
        },
        "habitacion 5": {
            "disponible": True,
            "capacidad": 4,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "habitacion 6": {
            "disponible": True,
            "capacidad": 2,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "habitacion 7": {
            "disponible": True,
            "capacidad": 3,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "habitacion 8": {
            "disponible": True,
            "capacidad": 4,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "habitacion 9": {
            "disponible": True,
            "capacidad": 2,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": False,
                "Balcon": True
            }
        },
        "habitacion 10": {
            "disponible": True,
            "capacidad": 6,
            "servicios": {
                "frigobar": True,
                "aireAcondicionado": True,
                "Balcon": False
            }
        }
    }
        
        
        # Diccionario de datos de ventas: KEY=Código de venta, VALUE=Otros datos de la venta



#-------------------------------------------------
# Bloque de menú
#----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 5
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de clientes")
            print("[2] Gestión de habitaciones")
            print("[3] Gestión de reservas")
            print("[4] Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE CLIENTES")
                    print("---------------------------")
                    print("[1] Ingresar Cliente")
                    print("[2] Modificar cliente")
                    print("[3] Eliminar cliente")
                    print("[4] Listado de clientes")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    nuevoCliente(clientela)
                    print(clientela)
                    
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                    #clientes = inactivarCliente(clientes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    
                    listarClientesActivos(clientela)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ GESTION DE HABITACIONES")
                    print("---------------------------")
                    print("[1] Ingresar habitación")
                    print("[2] Modificar habitación")
                    print("[3] Eliminar habitación")
                    print("[4] Listado de habitaciones")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    ...
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    habitaciones = modificarHabitaciones(habitaciones)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarHabitaciones(habitaciones)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 1
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE GESTION DE RESERVAS")
                    print("---------------------------")
                    print("[1] Registro de reservas")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                    print("\n\n")

        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE INFORMES")
                    print("---------------------------")
                    print("[1] Reservas del Mes")
                    print("[2] Resumen Anual de reservas por habitación (Cantidades)")
                    print("[3] Resumen Anual de reservas por habitación (Pesos)")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    ...
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()