"""
-----------------------------------------------------------------------------------------------
Título: TP Programacion 1 primer entrega
Fecha: 03/06/2025
Autor: Agustin Avella, Bryan Charra, Damian Mayorano, Nahuel Ganduglia

Descripción: 
Este es un proyecto desarrollado para la materia Programación I (3.4.071) de la Universidad Argentina de la Empresa (UADE).
El objetivo es crear un sistema simple de gestión hotelera que permita informatizar y organizar las reservas, habitaciones y clientes del hotel Hotel Transilvania.

📌 Descripción
El sistema permite llevar el control de:

Clientes: registro de información personal y estado (activo/inactivo).
Habitaciones: control de disponibilidad, capacidad, costo por día y servicios disponibles.
Reservas: alta y cancelación de reservas, incluyendo fechas, cantidad de personas, habitación asignada y método de pago.
⚙️ Características principales
Informes: para poder estar al tanto a los datos/rendimiento del negocio.
Implementación de baja lógica para clientes y reservas (no se eliminan registros, solo se actualiza su estado).
Sistema basado en menús por consola, orientado a prácticas básicas de programación estructurada.
Diseño de datos basado en entidades maestras (Cliente y Habitación) y una entidad de transacción (Reserva).
Proyecto orientado al aprendizaje de conceptos fundamentales de desarrollo de software.

Pendientes:
- Funcion informes por año (cantidad)
- Funcion informes por año (pesos)
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time
from datetime import datetime



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaCliente(_clientes):
    """
    Solicita los datos de un nuevo cliente y lo registra si el DNI no existe.
    """
    dni = input("Ingresa tu DNI: ")
    while not (dni.isdigit() and len(dni) == 8):
        dni = input("DNI inválido. Ingrese un DNI de 8 dígitos: ")
    if dni in _clientes:
        print("El cliente ya existe.")
    else:
        nombre = input("Ingresa tu nombre: ")
        while nombre.isdigit():
            nombre = input("El nombre no puede ser un numero: ")
        while True:
            edad_input = input("Ingrese su edad: ")
            try:
                edad = int(edad_input)
                if edad < 0:
                    print("La edad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("Edad inválida. Ingrese un número entero.")


        telefono = input("Ingrese su numero de telefono: ")
        while (len(telefono) < 10 or telefono.isdigit()==False):
            telefono = input("Ingrese un numero de telefono válido (por lo menos 10 digitos): ")

        alterno = input("Ingresa un segundo numero de telefono. Si no tiene otro simplemente deje el campo vacio: ")
        if alterno == None:
            print("-----")
        else:
            while (len(alterno) < 10 or alterno.isdigit()==False):
                alterno = input("Ingresa un segundo numero de telefono válido (por lo menos 10 digitos): ")

        nuevoCliente = {
            "activo": True,
            "nombre": nombre,
            "edad": edad,
            "telefonos": {
                "movil": telefono,
                "alterno": alterno,
            }
        }
        _clientes[dni] = nuevoCliente
        print("==============================")
        print("Cliente agregado con exito.")
        return


def inactivarCliente(_clientes):
    """
    Inactiva un cliente existente dado su DNI. Si no existe, muestra mensaje de que no existe tal dni.
    """
    dni = input("DNI del cliente a inactivar: ")
    while not (dni.isdigit() and len(dni) == 8):
        dni = input("DNI inválido. Ingrese un DNI de 8 dígitos: ")

    print()

    if dni in _clientes:
        _clientes[dni]["activo"] = False
        print(f"El cliente {dni} fue dado de baja.")
    else:
        print(f"El DNI {dni} es inexistente.")

    return _clientes


def listarClientesActivos(_clientes):
    """
    Muestra en pantalla los datos de todos los clientes activos del sistema.
    """
    for dni, otrosDatos in _clientes.items():
        if otrosDatos['activo']:
            print(f"DNI: {dni}")
            print(f"NOMBRE: {otrosDatos.get('nombre', 'No disponible')}")
            print(f"EDAD: {otrosDatos.get('edad', 'No disponible')}")
            print("TELEFONOS:")
            for telefono, numeroTelefono in otrosDatos.get("telefonos", {}).items():
                if numeroTelefono:
                    print(f"\t{telefono}: {numeroTelefono}")
            print("========================================")
    return


def modificarCliente(_clientes):
    """
    Permite modificar los datos de un cliente existente, incluyendo nombre, teléfonos y estado.
    """
    dni = input("Ingresa tu DNI a Modificar: ")
    while not (dni.isdigit() and len(dni) == 8):
        dni = input("DNI inválido. Ingrese un DNI de 8 dígitos: ")
    if dni in _clientes:
        activo = input("Activo[True], Baja[False]: ")
        nombre = input(f"¿Nombre correcto?, {_clientes[dni]['nombre']}: ")
        movil = input(f"¿Numero de télefono 1 correcto?, {_clientes[dni]['telefonos']['movil']}: ")
        alterno = input(f"¿Numero de télefono 2 correcto?, {_clientes[dni]['telefonos']['alterno']}: ")

        clienteModificado = {
            "activo": activo == "True",
            "nombre": nombre,
            "telefonos": {
                "movil": movil,
                "alterno": alterno
            }
        }
        _clientes[dni] = clienteModificado
        print("Cliente modificado con exito.")


def altaHabitacion(_habitaciones):
    """
    Registra una nueva habitación con sus características si no existe previamente.
    """
    nroHabitacion = input("Ingrese numero de la habitacion: ")
    while not (nroHabitacion.isdigit()):
        nroHabitacion = input("DNI inválido. Ingrese un DNI de 8 dígitos: ")
    if nroHabitacion in _habitaciones:
        return "La habitacion ya existe."

    capacidad = input("Ingrese capacidad de personas: ")
    costoPorDia = int(input("Ingrese su costo por dia: "))
    aireCondicionado = input("Ingrese True si tiene aire acondicionado o False si no tiene:  ")
    frigobar = input("Ingrese True si tiene frigobar o False si no tiene: ")
    balcon = input("Ingrese True si tiene balcon o False si no tiene: ")

    nuevaHabitacion = {
        "disponible": True,
        "capacidad": int(capacidad),
        "costoPorDia": costoPorDia,
        "servicios": {
            "aire acondicionado": aireCondicionado == "True",
            "frigobar": frigobar == "True",
            "balcon": balcon == "True"
        }
    }
    _habitaciones[nroHabitacion] = nuevaHabitacion
    return "Habitacion agregada con exito."


def inactivarHabitacion(_habitaciones):
    """
    Marca una habitación como no disponible (inhabilitada) si existe en el sistema.
    """
    nroHabitacion = input("Numero de habitacion a inhabilitar: ")
    print("======================================")

    if nroHabitacion in _habitaciones:
        _habitaciones[nroHabitacion]["disponible"] = False
        print(f"La habitacion {nroHabitacion} fue inhabilitada.")
    else:
        print(f"El numero de habitacion {nroHabitacion} no existe.")

    return _habitaciones


def listarHabitacionesActivas(_habitaciones):
    """
    Muestra en pantalla todas las habitaciones disponibles y sus servicios asociados.
    """
    for nroHabitacion, otrosDatos in _habitaciones.items():
        if otrosDatos['disponible']:
            print(f"Habitacion: {nroHabitacion}")
            print(f"Capacidad: {otrosDatos.get('capacidad', 'No disponible')}")
            print(f"Costo por dia: {otrosDatos.get('costoPorDia', 'No disponible')}")
            print("Servicios:")
            for servicios, nombreServicio in otrosDatos.get("servicios", {}).items():
                print(f"\t{servicios}: {nombreServicio}")
            print("========================================")
    return


def modificarHabitacion(_habitaciones):
    """
    Permite modificar los atributos de una habitación existente, incluyendo servicios y costo.
    """
    nroHabitacion = input("Ingresa numero de habitacion a modificar: ")
    if nroHabitacion in _habitaciones:
        disponible = input("Disponible[True], No disponible[False]: ")
        capacidad = input("Nueva capacidad: ")
        costoPorDia = input("Nuevo costo por día: ")
        aire = input("¿Servicio aire acondicionado: Si[True] No[False]?: ")
        frigo = input("¿Servicio frigobar: Si[True] No[False]?: ")
        balcon = input("¿Servicio balcón: Si[True] No[False]?: ")

        habitacionModificada = {
            "disponible": disponible == "True",
            "capacidad": int(capacidad),
            "costoPorDia": int(costoPorDia),
            "servicios": {
                "aire acondicionado": aire == "True",
                "frigobar": frigo == "True",
                "balcon": balcon == "True"
            }
        }
        _habitaciones[nroHabitacion] = habitacionModificada
        print("Habitación modificada con éxito.")


def agendarReserva(_clientes, _habitaciones, _reservas):
    """
    Agenda una reserva para un cliente activo si hay una habitación que cumple con los requisitos.
    Calcula el total a pagar y guarda los datos en el sistema.
    """
    dni = input("Ingrese su dni: ")
    if dni in _clientes and _clientes[dni]['activo']:
        capacidad = int(input("Ingrese cantidad de personas: "))
        aireAcondicionado = input("Busca habitacion con aire acondicionado? (s/n): ").lower() == "s"
        frigo = input("Busca habitacion con frigobar? (s/n): ").lower() == "s"
        balcon = input("busca habitacion con balcon? (s/n): ").lower() == "s"

        for nroHabitacion, habitacionDatos in _habitaciones.items():
            if (
                habitacionDatos.get('disponible') and
                capacidad == habitacionDatos.get('capacidad') and
                aireAcondicionado == habitacionDatos.get('servicios', {}).get('aire acondicionado') and
                frigo == habitacionDatos.get('servicios', {}).get('frigobar') and
                balcon == habitacionDatos.get('servicios', {}).get('balcon')
            ):
                obj = time.localtime()
                idReserva = time.asctime(obj)

                while True:
                    fechaEntrada = input("Fecha de ingreso (DD/MM/AAAA): ")
                    try:
                        fechaEntrada_valida = datetime.strptime(fechaEntrada, "%d/%m/%Y")
                        break
                    except ValueError:
                        print("Fecha inválida. Intente nuevamente.")

                while True:
                    fechaSalida = input("Fecha de salida (DD/MM/AAAA): ")
                    try:
                        fechaSalida_valida = datetime.strptime(fechaEntrada, "%d/%m/%Y")
                        break
                    except ValueError:
                        print("Fecha inválida. Intente nuevamente.")
                metodoPago = input("Ingrese metodo de pago: [1] Efectivo / [2] Tarjeta: ")
                while (metodoPago != "1" and metodoPago != "2"):
                    metodoPago = input("Ingrese metodo de pago: [1] Efectivo / [2] Tarjeta: ")
                formato = "%d/%m/%Y"
                fechaEntradaDt = datetime.strptime(fechaEntrada, formato)
                fechaSalidaDt = datetime.strptime(fechaSalida, formato)
                dias = (fechaSalidaDt - fechaEntradaDt).days
                totalPagar = dias * habitacionDatos.get('costoPorDia')

                nuevaReserva = {
                    "dni": dni,
                    "nroHabitacion": nroHabitacion,
                    "activo": True,
                    "cantidadPersonas": capacidad,
                    "fechaDeEntrada": fechaEntrada,
                    "fechaDeSalida": fechaSalida,
                    "metodoDePago": metodoPago,
                    "totalPagar": totalPagar
                }
                _reservas[idReserva] = nuevaReserva
                _habitaciones[nroHabitacion]['disponible'] = False
                print("Reserva realizada con exito. Total a pagar: $", totalPagar)
                return
        print("No hay habitacion para esa cantidad de personas y servicios seleccionados.")
    else:
        print("Usted es un cliente inactivo o no registrado por lo tanto no puede realizar reservas.")


def listarReservasActivas(_reservas):
    """
    Muestra todas las reservas que están activas en el sistema con sus detalles.
    """
    for idReserva, otrosDatos in _reservas.items():
        if otrosDatos['activo']:
            print(f"dni: {otrosDatos.get('dni', 'No disponible')}")
            print(f"nroHabitacion: {otrosDatos.get('nroHabitacion', 'No disponible')}")
            print(f"cantidadPersonas: {otrosDatos.get('cantidadPersonas', 'No disponible')}")
            print(f"fechaDeEntrada: {otrosDatos.get('fechaDeEntrada', 'No disponible')}")
            print(f"fechaDeSalida: {otrosDatos.get('fechaDeSalida', 'No disponible')}")
            print(f"metodoDePago: {otrosDatos.get('metodoDePago', 'No disponible')}")
            print(f"Total a pagar: $ {otrosDatos.get('totalPagar', 'No disponible')}")
            print("========================================")
    return


def reporteReservasPorAño(reservas):
    """
    Genera un reporte resumen de la cantidad de reservas por habitación para un año dado.
    """
    año = int(input("Ingrese año: "))
    resumen = {i: [0]*12 for i in range(1, 11)}

    for datos in reservas.values():
        if datos["activo"]:
            fecha_str = datos["fechaDeEntrada"]
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            if fecha.year == año:
                mes = fecha.month
                habitacion = int(datos["nroHabitacion"])
                resumen[habitacion][mes - 1] += 1

    print(f"{'='*70}")
    print(f"Resumen de cantidad de reservas por habitación - Año {año}")
    print(f"{'='*70}")
    print("Habitación | Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic")
    for hab, meses in resumen.items():
        linea = f"{hab:<10} | " + " ".join(f"{m:<3}" for m in meses)
        print(linea)

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
            "telefonos": {
                "móvil": "11 5002415123",
                "alterno": ""
            }
        },
        "431223345": {
            "activo": True,
            "nombre": "Martin Gonzales",
            "edad": 26,
            "telefonos": {
                "móvil": "11 500245621",
                "alterno": "1124070486"
            }
        },
        "33451678": {
            "activo": True,
            "nombre": "Fito Parrez",
            "edad": 26,
            "telefonos": {
                "móvil": "11 500241234",
                "alterno": ""
            }
        },
        "15675431": {
            "activo": True,
            "nombre": "Gonzalo Robledo",
            "edad": 26,
            "telefonos": {
                "móvil": "11 500241252",
                "alterno": ""
            }
        },
        "423411123": {
            "activo": True,
            "nombre": "Martin Serin",
            "edad": 26,
            "telefonos": {
                "móvil": "11 500241211",
                "alterno": ""
            }
        },
        "11234124": {
            "activo": True,
            "nombre": "Gaston Soldati",
            "edad": 26,
            "telefonos": {
                "móvil": "11 695241234",
                "alterno": ""
            }
        },
        "41234124": {
            "activo": True,
            "nombre": "Marcelo Chavez",
            "edad": 26,
            "telefonos": {
                "móvil": "11 531241234",
                "alterno": ""
            }
        },
        "45212342": {
            "activo": True,
            "nombre": "Fernando Alonso",
            "edad": 26,
            "telefonos": {
                "móvil": "11 498241234",
                "alterno": ""
            }
        },
        "2142142": {
            "activo": True,
            "nombre": "Martin Gimenez",
            "edad": 26,
            "telefonos": {
                "móvil": "11 233241234",
                "alterno": ""
            }
        },
        "4042132": {
            "activo": True,
            "nombre": "Lionel Messi",
            "edad": 26,
            "telefonos": {
                "móvil": "11 503241234",
                "alterno": ""
            }
        },
        "43404740": {
            "activo": True,
            "nombre": "Agustin Avella",
            "edad": 23,
            "telefonos": {
                "móvil": "11 503241234",
                "alterno": "11 41231233"
            }
        }
    }

        # Diccionario de datos de productos: KEY=Código de producto, VALUE=Otros datos del producto
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


        "20/12/2010": {
            "dni": "39592834",
            "nroHabitacion": 1,
            "activo": False,
            "cantidadPersonas": 2,
            "fechaDeEntrada": '02/06/2025',
            "fechaDeSalida": "06/06/2025",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/2010": {
            "dni": "431223345",
            "nroHabitacion": 2,
            "activo": False,
            "cantidadPersonas": 2,
            "fechaDeEntrada": '02/05/2001',
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "20/12/2015": {
            "dni": "39592834",
            "nroHabitacion": 1,
            "activo": False,
            "cantidadPersonas": 2,
            "fechaDeEntrada": '10/06/2025',
            "fechaDeSalida": "06/06/2025",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

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
                    opciones = 2
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE GESTION DE RESERVAS")
                    print("---------------------------")
                    print("[1] Registro de reservas")
                    print("[2] Lista de reservas activas")
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
                    agendarReserva(clientela,habitaciones,reservas)
                elif opcionSubmenu == "2":
                    listarReservasActivas(reservas)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 1
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE INFORMES")
                    print("---------------------------")
                    print("[1] Resumen Anual de reservas por habitación")
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
                    reporteReservasPorAño(reservas)
                    
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