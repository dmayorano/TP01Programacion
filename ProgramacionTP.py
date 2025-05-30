"""
-----------------------------------------------------------------------------------------------
Título: Programacion 1 TP
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
def altaCliente(_clientes):
    dni = input("Ingresa tu DNI: ")
    if dni in _clientes:
        return "El cliente ya existe."
    
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingrese su edad: "))
    telefono = input("Ingrese su numero de telefono: ")
    alterno = input("Ingresa un segundo numero de telefono (Opcional): ")


    nuevoCliente = {
        "activo": True,
        "nombre": nombre,
        "edad": edad,
        "télefonos": {
            "telefono": telefono,
            "telefono alterno": alterno,
            }
        }
    _clientes[dni] = nuevoCliente
    return "Cliente agregado con exito"


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

def listarClientesActivos(_clientes):
    """
    Lista todos los clientes activos y sus detalles de tarjetas.
    """
    # Se muestran todos los datos del cliente y el detalle de sus tarjetas
    for dni, otrosDatos in _clientes.items():
        if otrosDatos['activo']:  # Filtro para clientes activos
            
            
            print(f"DNI: {dni}")
            print(f"NOMBRE: {otrosDatos.get('nombre', 'No disponible')}")
            
            # Verificar si el cliente tiene edad y sexo antes de imprimir
            print(f"EDAD: {otrosDatos.get('edad', 'No disponible')}")

            print("TELEFONOS:")
            for telefono, numeroTelefono in otrosDatos.get("telefonos", {}).items():
                if numeroTelefono:  # No imprimir tarjetas vacías
                    print(f"\t{telefono}: {numeroTelefono}")
            print("========================================")
    return

def modificarCliente(_clientes):
    dni = input("Ingresa tu DNI a Modificar: ")
    if dni in _clientes:
        
        activo = input("Activo[True], Baja[False]: ")
        nombre = input(f"¿Nombre correcto?, {_clientes[nombre]}: ")
        movil = input(f"¿Numero de télefono 1 correcto?, {_clientes[movil]}: ")
        alterno = input(f"¿Numero de télefono 2 correcto?, {_clientes[alterno]}: ")

        clienteModificado = {
        
        "activo": activo,
        "nombre": nombre,
        "télefonos": {
            "télefono1": movil,
            "télefono2": alterno
            }
        }
        _clientes[dni] = clienteModificado
        print("Cliente modificado con exito.")

def altaHabitacion(_habitaciones):
    nroHabitacion = input("Ingrese numero de la habitacion: ")
    if nroHabitacion in _habitaciones:
        return "La habitacion ya existe."
    
    capacidad = input("Ingrese capacidad de personas: ")
    costoPorDia = int(input("Ingrese su costo por dia: "))
    aireCondicionado = input("Ingrese True si tiene aire acondicionado o False si no tiene:  ")
    frigobar = input("Ingrese True si tiene frigobar o False si no tiene: ")
    balcon= input("Ingrese True si tiene balcon o False si no tiene: ")


    nuevaHabitacion = {
        "disponible": True,
        "capacidad": capacidad,
        "costo por dia": costoPorDia,
        "servicios": {
            "aire condicionado": aireCondicionado,
            "frigobar": frigobar,
            "balcon": balcon
            }
        }
    _habitaciones[nroHabitacion] = nuevaHabitacion
    return "Habitacion agregada con exito."


def inactivarHabitacion(_habitaciones):
    """
    doctring
    """
    nroHabitacion = input("Numero de habitacion a inhabilitar: ")
    print("======================================")
    
    # Se inactiva el cliente sólo si existe
    if nroHabitacion in _habitaciones:
        _habitaciones[nroHabitacion]["disponible"] = False
        print(f"La habitacion {nroHabitacion} fue inhabilitada.")
    else:
        print(f"El numero de habitacion {nroHabitacion} no existe.")
    
    return _habitaciones

def listarHabitacionesActivas(_habitaciones):
    """
    Lista todos los clientes activos y sus detalles de tarjetas.
    """
    # Se muestran todos los datos del cliente y el detalle de sus tarjetas
    for nroHabitacion, otrosDatos in _habitaciones.items():
        if otrosDatos['disponible']:  # Filtro para habitaciones activas
            
            
            print(f"Habitacion: {nroHabitacion}")
            print(f"Capacidad: {otrosDatos.get('capacidad', 'No disponible')}")
            print(f"Costo por dia: {otrosDatos.get('costo por dia', 'No disponible')}")

            print("Servicios:")
            for servicios, nombreServicio in otrosDatos.get("servicios", {}).items():
                print(f"\t{servicios}: {nombreServicio}")
            print("========================================")
    return

def modificarHabitacion(_habitaciones):
    nroHabitacion = input("Ingresa numero de habitacion a modificar: ")
    if nroHabitacion in _habitaciones:
        
        disponible = input("Disponible[True], No disponible[False]: ")
        capacidad = input(f"¿Capacidad correcta?, {_habitaciones[capacidad]}: ")
        costoPorDia = input(f"¿Costo por dia correcto?, {_habitaciones[costoPorDia]}: ")
        aire = input(f"¿Servicio aire acondicionado: Si[True] No[False]?, {_habitaciones[aire]}: ")
        frigo = input(f"¿Servicio frigobar: Si[True] No[False]?, {_habitaciones[frigo]}: ")
        balcon = input(f"¿Servicio balcon: Si[True] No[False]?, {_habitaciones[balcon]}: ")

        habitacionModificada = {
        
        "disponible": disponible,
        "capacidad": capacidad,
        "costo por dia": costoPorDia,
        "servicios": {
            "aire acondicionado": aire,
            "frigobar": frigo,
            "balcon": balcon 
            }
        }
        _habitaciones[nroHabitacion] = habitacionModificada
        print("Cliente modificado con exito.")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------


    # Diccionario de datos de clientes: KEY=Documento del cliente, VALUE=Otros datos del cliente
    clientela = {
        "39592834": {
            "activo": True,
            "nombre": "Micaela Robles",
            "edad": 26,
            "télefonos": {
                "móvil": "11 5002415123",
                "alterno": ""
            }
        },
        "431223345": {
            "activo": True,
            "nombre": "Martin Gonzales",
            "edad": 26,
            "télefonos": {
                "móvil": "11 500245621",
                "alterno": ""
            }
        },
        "33451678": {
            "activo": True,
            "nombre": "Fito Parrez",
            "edad": 26,
            "télefonos": {
                "móvil": "11 500241234",
                "alterno": ""
            }
        },
        "15675431": {
            "activo": True,
            "nombre": "Gonzalo Robledo",
            "edad": 26,
            "télefonos": {
                "móvil": "11 500241252",
                "alterno": ""
            }
        },
        "423411123": {
            "activo": True,
            "nombre": "Martin Serin",
            "edad": 26,
            "télefonos": {
                "móvil": "11 500241211",
                "alterno": ""
            }
        },
        "11234124": {
            "activo": True,
            "nombre": "Gaston Soldati",
            "edad": 26,
            "télefonos": {
                "móvil": "11 695241234",
                "alterno": ""
            }
        },
        "41234124": {
            "activo": True,
            "nombre": "Marcelo Chavez",
            "edad": 26,
            "télefonos": {
                "móvil": "11 531241234",
                "alterno": ""
            }
        },
        "45212342": {
            "activo": True,
            "nombre": "Fernando Alonso",
            "edad": 26,
            "télefonos": {
                "móvil": "11 498241234",
                "alterno": ""
            }
        },
        "2142142": {
            "activo": True,
            "nombre": "Martin Gimenez",
            "edad": 26,
            "télefonos": {
                "móvil": "11 233241234",
                "alterno": ""
            }
        },
        "4042132": {
            "activo": True,
            "nombre": "Lionel Messi",
            "edad": 26,
            "télefonos": {
                "móvil": "11 503241234",
                "alterno": ""
            }
        }
    }

        # Diccionario de datos de productos: KEY=Código de producto, VALUE=Otros datos del producto
    habitaciones = {
        "1": {
            "disponible": True,
            "capacidad": 2,
            "servicios": {
                "aire condicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "2": {
            "disponible": True,
            "capacidad": 4,
            "servicios": {
                "aire condicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "3": {
            "disponible": True,
            "capacidad": 2,
            "servicios": {
                "aire acondicionado": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "4": {
            "disponible": True,
            "capacidad": 6,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": False,
                "Balcon": False
            }
        },
        "5": {
            "disponible": True,
            "capacidad": 4,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "6": {
            "disponible": True,
            "capacidad": 2,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "7": {
            "disponible": True,
            "capacidad": 3,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "8": {
            "disponible": True,
            "capacidad": 4,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "9": {
            "disponible": True,
            "capacidad": 2,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": False,
                "Balcon": True
            }
        },
        "10": {
            "disponible": True,
            "capacidad": 6,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
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
                    print("[3] Inactivar cliente")
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
                    altaCliente(clientela)
                    
                    
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    modificarCliente(clientela)
                    
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    inactivarCliente(clientela)
                
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
                    altaHabitacion(habitaciones)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    modificarHabitacion(habitaciones)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    inactivarHabitacion(habitaciones)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarHabitacionesActivas(habitaciones)

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