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
import time
from datetime import datetime



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaCliente(_clientes):
    dni = input("Ingresa tu DNI: ")
    if dni in _clientes:
        print("El cliente ya existe.")
    
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingrese su edad: "))
    telefono = input("Ingrese su numero de telefono: ")
    alterno = input("Ingresa un segundo numero de telefono. Si no tiene otro simplemente deje el campo vacio: ")
    if alterno == 0:
        print("----")

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
    # Se muestran todos los datos del cliente y el detalle 
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
        "telefonos": {
            "telefono1": movil,
            "telefono2": alterno
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

def agendarReserva(_clientes,_habitaciones,_reservas):
    dni = input("Ingrese su dni: ")
    if dni in _clientes and _clientes[dni]['activo']:

        capacidad = int(input("Ingrese cantidad de personas: "))

        aireAcondicionado = input("Busca habitacion con aire acondicionado? (s/n): ").lower()
        if aireAcondicionado == "s":
            aireAcondicionado = True
        else:
            aireAcondicionado = False

        frigo = input("Busca habitacion con frigobar? (s/n): ").lower()
        if frigo == "s":
            frigo = True
        else:
            frigo = False
        
        balcon = input("busca habitacion con balcon? (s/n): ").lower()
        if balcon == "s":
            balcon = True
        else:
            balcon = False

        for nroHabitacion, habitacionDatos in _habitaciones.items():
            if (habitacionDatos.get('disponible') and capacidad == habitacionDatos.get('capacidad') and aireAcondicionado == habitacionDatos.get('servicios', {}).get('aireAcondicionado') and
                frigo == habitacionDatos.get('servicios', {}).get('frigobar') and balcon == habitacionDatos.get('servicios', {}).get('balcon')):
                obj= time.localtime()
                idReserva = time.asctime(obj)
                fechaEntrada = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ")
                fechaSalida = input("Ingrese la fecha de salida (DD/MM/AAAA): ")
                metodoPago = input("Ingrese metodo de pago (Efectivo/Tarjeta): ")

                formato = "%d/%m/%Y"
                fechaEntradaDt = datetime.strptime(fechaEntrada, formato)
                fechaSalidaDt = datetime.strptime(fechaSalida, formato)
                diferencia = fechaSalidaDt - fechaEntradaDt
                dias = diferencia.days
                totalPagar = dias * habitacionDatos.get('costoPorDia')
                nuevaReserva = {
                "idReserva": idReserva,
                "dni": dni,
                "nroHabitacion": nroHabitacion,
                "activo": True,
                "cantidadPersonas": capacidad,
                "fechaDeEntrada": fechaEntrada,
                "fechaDeSalida": fechaSalida,
                "metodoDePago": metodoPago,
                "totalPagar": totalPagar
                }
                _reservas[idReserva]= nuevaReserva
                _habitaciones[nroHabitacion]['disponible'] == False
                print("Reserva realizada con exito. Total a pagar: $", totalPagar)
                return
        print("No hay habitacion para esa cantidad de personas y servicios seleccionados.")
    else:
        print("Usted es un cliente inactivo o no registrado por lo tanto no puede realizar reservas.")

def listarReservasActivas(_reservas):
    """
    Lista todos los clientes activos y sus detalles de tarjetas.
    """
    # Se muestran todos los datos del cliente y el detalle de sus tarjetas
    for idReserva, otrosDatos in _reservas.items():
        if otrosDatos['activo']:
            print(f"idReserva: {idReserva}")
            print(f"dni: {otrosDatos.get('dni', 'No disponible')}")
            print(f"nroHabitacion: {otrosDatos.get('nroHabitacion', 'No disponible')}")
            print(f"cantidadPersonas: {otrosDatos.get('cantidadPersonas', 'No disponible')}")
            print(f"fechaDeEntrada: {otrosDatos.get('fechaDeEntrada', 'No disponible')}")
            print(f"fechaDeSalida: {otrosDatos.get('fechaDeSalida', 'No disponible')}")
            print(f"metodoDePago: {otrosDatos.get('metodoDePago', 'No disponible')}")
            print(f"Total a pagar: $ {otrosDatos.get('totalPagar', 'No disponible')}")
            print("========================================")
    return

def resumenReservasAnualPorHabitacion(_reservas, _habitaciones):
    anio = input("Ingrese el año que desea consultar (AAAA): ")

    # Lista de meses para el encabezado
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
             "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

    # Inicializar resumen: {habitacion: [0]*12}
    resumen = {}
    for nroHabitacion, datos in _habitaciones.items():
        if datos['disponible']:
            resumen[nroHabitacion] = [0] * 12

    # Recorremos reservas activas y sumamos por mes
    for idReserva, datosReserva in _reservas.items():
        if datosReserva['activo']:
            fechaEntrada = datosReserva['fechaDeEntrada']
            fechaObj = datetime.strptime(fechaEntrada, "%d/%m/%Y")
            if str(fechaObj.year) == anio:
                habitacion = datosReserva['nroHabitacion']
                mes = fechaObj.month
                if habitacion in resumen:
                    resumen[habitacion][mes - 1] += 1

    # Imprimir tabla
    print("\n===============================================================")
    print(f"Resumen de cantidad de reservas por habitación - Año {anio}")
    print("===============================================================")
    print(f"{'Habitación':12}", end="")
    for m in meses:
        print(f"{m:>5}", end="")
    print()

    for habitacion, valores in resumen.items():
        print(f"{habitacion:12}", end="")
        for cantidad in valores:
            print(f"{cantidad:5}", end="")
        print()

def resumenRecaudacionAnualPorHabitacion(_reservas, _habitaciones):
    anio = input("Ingrese el año que desea consultar (AAAA): ")

    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
             "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

    # Inicializar resumen: {habitacion: [0]*12}
    resumen = {}
    for nroHabitacion, datos in _habitaciones.items():
        if datos['disponible']:
            resumen[nroHabitacion] = [0] * 12

    # Recorremos reservas activas y sumamos total recaudado por mes
    for idReserva, datosReserva in _reservas.items():
        if datosReserva['activo']:
            fechaEntrada = datosReserva['fechaDeEntrada']
            fechaObj = datetime.strptime(fechaEntrada, "%d/%m/%Y")
            if str(fechaObj.year) == anio:
                habitacion = datosReserva['nroHabitacion']
                mes = fechaObj.month
                total = datosReserva.get('totalPagar', 0)
                if habitacion in resumen:
                    resumen[habitacion][mes - 1] += int(total)

    # Imprimir tabla
    print("\n====================================================================")
    print(f"Resumen de recaudación por habitación - Año {anio}")
    print("====================================================================")
    print(f"{'Habitación':12}", end="")
    for m in meses:
        print(f"{m:>8}", end="")
    print()

    for habitacion, valores in resumen.items():
        print(f"{habitacion:12}", end="")
        for monto in valores:
            print(f"{monto:8}", end="")
        print()
           
def listarReservasPorMes(_reservas):
    mes = input("Ingrese el mes a consultar (1-12): ")
    anio = input("Ingrese el año (AAAA): ")

    print("==========================================================================")
    print(f"Listado de reservas del mes {mes}/{anio}")
    print("==========================================================================")
    print(f"{'ID Reserva':25} {'DNI':10} {'Habitación':12} {'Ingreso':12} {'Salida':12} {'Total ($)':>10}")
    print("--------------------------------------------------------------------------")

    for idReserva, datos in _reservas.items():
        if datos['activo']:
            fechaEntrada = datos['fechaDeEntrada']
            fechaObj = datetime.strptime(fechaEntrada, "%d/%m/%Y")

            if str(fechaObj.month) == mes and str(fechaObj.year) == anio:
                print(f"{idReserva:25} {datos['dni']:10} {datos['nroHabitacion']:12} {datos['fechaDeEntrada']:12} {datos['fechaDeSalida']:12} {datos['totalPagar']:10.2f}")


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
        }
    }

        # Diccionario de datos de productos: KEY=Código de producto, VALUE=Otros datos del producto
    habitaciones = {
        "1": {
            "disponible": True,
            "capacidad": 2,
            "costoPorDia": 10000,
            "servicios": {
                "aireAcondicionado": True,
                "frigobar": True,
                "balcon": True
            }
        },
        "2": {
            "disponible": True,
            "capacidad": 4,
            "costoPorDia": 10000,
            "servicios": {
                "aire condicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "3": {
            "disponible": True,
            "capacidad": 2,
            "costoPorDia": 10000,
            "servicios": {
                "aire acondicionado": True,
                "aireAcondicionado": True,
                "Balcon": True
            }
        },
        "4": {
            "disponible": True,
            "capacidad": 6,
            "costoPorDia": 10000,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": False,
                "Balcon": False
            }
        },
        "5": {
            "disponible": True,
            "capacidad": 4,
            "costoPorDia": 10000,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "6": {
            "disponible": True,
            "capacidad": 2,
            "costoPorDia": 10000,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "7": {
            "disponible": True,
            "capacidad": 3,
            "costoPorDia": 10000,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "8": {
            "disponible": True,
            "capacidad": 4,
            "costoPorDia": 10000,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": True
            }
        },
        "9": {
            "disponible": True,
            "capacidad": 2,
            "costoPorDia": 10000,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": False,
                "Balcon": True
            }
        },
        "10": {
            "disponible": True,
            "capacidad": 6,
            "costoPorDia": 10000,
            "servicios": {
                "aire acondicionado": True,
                "frigobar": True,
                "Balcon": False
            }
        }
    }

    reservas = {


        "10/10/2010": {
            "dni": "39592834",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/10": {
            "dni": "431223345",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "12/10/10": {
            "dni": "33451678",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/10": {
            "dni": "15675431",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/10": {
            "dni": "423411123",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/10": {
            "dni": "11234124",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/10": {
            "dni": "41234124",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/10": {
            "dni": "45212342",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/10": {
            "dni": "2142142",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
            "metodoDePago": "Efectivo",
            "totalPagar": 20000},

        "15/10/10": {
            "dni": "4042132",
            "nroHabitacion": 1,
            "activo": True,
            "cantidadPersonas": 2,
            "fechaDeEntrada": "02/06/2001",
            "fechaDeSalida": "06/06/2001",
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
                    listarReservasPorMes(reservas)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    resumenReservasAnualPorHabitacion(reservas,habitaciones)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    resumenRecaudacionAnualPorHabitacion(reservas,habitaciones)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()