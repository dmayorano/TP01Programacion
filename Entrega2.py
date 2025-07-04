"""
-----------------------------------------------------------------------------------------------
Título: TP Programacion 1 Entrega Final
Fecha: 07/07/2025
Autor: Agustin Avella

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
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from datetime import datetime



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def habitacionesMasRentables(reservas):
    """
    Muestra las habitaciones más rentables del hotel, ordenadas por ingresos.

    Args:
        reservas (dict): Diccionario de reservas del hotel.
    """
    habitaciones = {}

    for datos in reservas.values():
        if datos["activo"]:
            nroHabitacion = datos["nroHabitacion"]
            totalPagar = datos["totalPagar"]

            if nroHabitacion not in habitaciones:
                habitaciones[nroHabitacion] = 0

            habitaciones[nroHabitacion] += totalPagar

    habitacionesOrdenadas = []
    while habitaciones:
        maxHabitacion = max(habitaciones, key=habitaciones.get)
        habitacionesOrdenadas.append((maxHabitacion, habitaciones[maxHabitacion]))
        del habitaciones[maxHabitacion]

    print(f"{'='*50}")
    print(f"Habitaciones Más Rentables")
    print(f"{'='*50}")
    print("Nro. Habitación | Ingresos")
    for habitacion, ingresos in habitacionesOrdenadas:
        print(f"{habitacion:<15} | {ingresos:,.2f}")


def resumenMontoPorAñoYMes(reservas):
    """
    Muestra un resumen de los montos en pesos por año y mes.

    Args:
        reservas (dict): Diccionario de reservas del hotel.
    """
    resumen = {}

    for datos in reservas.values():
        if datos["activo"]:
            fechaStr = datos["fechaDeEntrada"]
            fecha = datetime.strptime(fechaStr, "%d/%m/%Y")
            año = fecha.year
            mes = fecha.month
            totalPagar = datos["totalPagar"]

            if año not in resumen:
                resumen[año] = [0] * 12

            resumen[año][mes - 1] += totalPagar

    print(f"{'='*70}")
    print(f"Resumen de monto en pesos por año y mes")
    print(f"{'='*70}")
    for año, meses in resumen.items():
        print(f"Año {año}")
        print("Mes | Monto")
        for i, monto in enumerate(meses):
            if monto > 0:
                print(f"{['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'][i]} | {monto:,.2f}")
        print()

    print(f"{'='*70}")
    print(f"Resumen de monto en pesos por año y mes (matriz)")
    print(f"{'='*70}")
    print("Año | Ene       Feb       Mar       Abr       May       Jun       Jul       Ago       Sep       Oct       Nov       Dic")
    for año, meses in resumen.items():
        linea = f"{año:<4} | "
        for monto in meses:
            linea += f"{monto:>10,.2f} "
        print(linea)


def informeIngresosPorFechaEntradaDelMes(reservas, clientes):
    """
    Muestra un informe de las operaciones del mes actual.

    Args:
        reservas (dict): Diccionario de reservas del hotel.
        clientes (dict): Diccionario de clientes del hotel.
    """
    
    fechaActual = datetime.now()
    mesActual = fechaActual.month
    añoActual = fechaActual.year

    
    print(f"{'Fecha ingreso':<20} {'Cliente':<20} {'Nro. Habitación':<15} {'Cant. Personas':<15} {'Método de Pago':<15} {'Total':<10}")
    print("-" * 100)

    
    for idReserva, reserva in reservas.items():
        fechaEntrada = datetime.strptime(reserva["fechaDeEntrada"], "%d/%m/%Y")
        if fechaEntrada.month == mesActual and fechaEntrada.year == añoActual:
            cliente = clientes.get(reserva["dni"], {}).get("nombre", "No disponible")
            print(f"{reserva['fechaDeEntrada']:<20} {cliente:<20} {reserva['nroHabitacion']:<15} {reserva['cantidadPersonas']:<15} {reserva['metodoDePago']:<15} ${reserva['totalPagar']:<10,.2f}")

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
        nombre = input("Ingresa tu nombre y apellido: ")
        while nombre.isdigit():
            nombre = input("El nombre y apellido no puede ser un numero: ")
        while True:
            edadInput = input("Ingrese su edad: ")
            try:
                edad = int(edadInput)
                if edad < 0:
                    print("La edad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("Edad inválida. Ingrese un número entero.")


        telefono = input("Ingrese su numero de telefono: ")
        while (len(telefono) < 10 or len(telefono) > 15 or telefono.isdigit()==False):
            telefono = input("Ingrese un numero de telefono válido (por lo menos 10 digitos): ")

        alterno = input("Ingresa un segundo numero de telefono. Si no tiene otro simplemente deje el campo vacio: ")
        if alterno == "":
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
        activo = input("Activo[1], Baja[2]: ")
        while activo != "1" and activo != "2":
            activo = input("Error. Introduzca 1 para verdadero o 2 para falso: ")
        if activo == "1":
            activo = True
        else:
            activo = False

        print("Si no desea cambiar un valor solo oprima enter para saltear al siguiente dato.")

        cambionombre = input(f"¿Nombre correcto?, {_clientes[dni]['nombre']}: ")
        if cambionombre == "":
            nombre = _clientes[dni]['nombre']
        else:
            nombre = cambionombre
        
        cambioedad = input(f"¿Edad correcta?, {_clientes[dni]['edad']}: ")
        if cambioedad == "":
            edad = _clientes[dni]['edad']
        else:
            while not (cambioedad.isdigit() and 0 <= int(cambioedad)):
                cambioedad = input("Edad inválida. Ingrese una edad mayor a 0: ")
            edad = int(cambioedad)       

        cambiomovil = input(f"¿Numero de télefono 1 correcto?, {_clientes[dni]['telefonos']['movil']}: ")
        if cambiomovil == "":
            movil = _clientes[dni]['telefonos']['movil']
        else:
            while not (cambiomovil.isdigit() and len(cambiomovil) >= 10 and len(cambiomovil) <= 15):
                cambiomovil = input("Número inválido. Vuelva a ingresarlo: ")
            movil = cambiomovil

        cambioalterno = input(f"¿Numero de télefono 2 correcto?, {_clientes[dni]['telefonos']['alterno']}: ")
        if cambioalterno == "":
            alterno = _clientes[dni]['telefonos']['alterno']
        else:
            while not (cambioalterno.isdigit() and len(cambioalterno) >= 10 and len(cambioalterno) <= 15):
                cambioalterno = input("Número inválido. Vuelva a ingresarlo: ")
            alterno = cambioalterno

        clienteModificado = {
            "activo": activo,
            "nombre": nombre,
            "edad": edad,
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
    while not (nroHabitacion.isdigit() and int(nroHabitacion) >= 0):
        nroHabitacion = input("Numero inválido. Ingrese un numero de habitacion que no sea negativo o letras: ")
    
    if nroHabitacion in _habitaciones:
        print()
        print("La habitacion ya existe.")
        return

    def validar_servicio(texto):
        opcion = input(f"{texto} [True/False]: ")
        while opcion != "True" and opcion != "False":
            opcion = input(f"Entrada inválida. Ingresa True o False para {texto}: ")
        if opcion == "True":
            return True
        else:
            return False
    while True:
        try:
            capacidad = int(input("Ingrese capacidad de personas: "))
            if capacidad <= 0:
                print("La capacidad debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error. Ingrese digitos númericos, no letras ni simbolos.")
        except TypeError:
            print("Error. Ingrese digitos númericos, no letras ni simbolos. ")

    while True:
        try:
            costoPorDia = int(input("Ingrese su costo por dia: "))
            if costoPorDia <= 0:
                costoPorDia = input("El costo por dia debe ser mayor a 0: ")
            else:
                break
        except ValueError:
            print("Error. Ingrese digitos númericos, no letras ni simbolos.")

    aireCondicionado = validar_servicio("Aire acondicionado")
    frigobar = validar_servicio("Frigobar")
    balcon = validar_servicio("Balcon")

    nuevaHabitacion = {
        "disponible": True,
        "capacidad": int(capacidad),
        "costoPorDia": costoPorDia,
        "servicios": {
            "aire acondicionado": aireCondicionado,
            "frigobar": frigobar,
            "balcon": balcon
        }
    }
    _habitaciones[nroHabitacion] = nuevaHabitacion
    print()
    print("Habitacion agregada con exito.")
    return


def inactivarHabitacion(_habitaciones):
    """
    Marca una habitación como no disponible (inhabilitada) si existe en el sistema.
    """
    nroHabitacion = input("Numero de habitacion a inhabilitar: ")
    while not (nroHabitacion.isdigit() and int(nroHabitacion) >= 0):
        nroHabitacion = input("Numero inválido. Ingrese un numero de habitacion que no sea negativo o letras: ")
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

    while not (nroHabitacion.isdigit() and int(nroHabitacion) >= 0):
        nroHabitacion = input("Numero inválido. Ingrese un numero de habitacion que no sea negativo o letras: ")

    if nroHabitacion not in _habitaciones:
        print("La habitación no existe.")
        return
    else:
        disponible = input("Disponible[True], No disponible[False]: ")
        while disponible not in ("True", "False"):
            disponible = input("Entrada inválida. Ingrese 'True' o 'False' para disponibilidad: ")
        if disponible == "True":
            disponible = True
        else:
            disponible = False

        print("==============")
        print("Si no desea cambiar un valor solo oprima enter para saltear al siguiente dato.")
        print("==============")

        while True:
            try:
                cambiocapacidad = input(f"¿Capacidad correcta?, {_habitaciones[nroHabitacion]['capacidad']}: ")
                if cambiocapacidad == "":
                    capacidad = _habitaciones[nroHabitacion]['capacidad']
                    break
                if not cambiocapacidad.isdigit() or int(cambiocapacidad) <= 0:
                    print("Capacidad inválida.")
                else:
                    capacidad = cambiocapacidad
                    break
            except ValueError:
                print("Entrada inválida. Ingrese numeros.")

        while True:
            try:
                cambiocostoPorDia = input(f"¿Costo por dia correcto?, {_habitaciones[nroHabitacion]['costoPorDia']}: ")
                if cambiocostoPorDia == "":
                    costoPorDia = _habitaciones[nroHabitacion]['costoPorDia']
                    break
                else:
                    if not cambiocostoPorDia.isdigit() and int(cambiocostoPorDia) > 0:
                        cambiocostoPorDia = input("Costo inválido. Ingrese un numero entero positivo.")
                    else:
                        costoPorDia = cambiocostoPorDia
                        break
            except ValueError:
                print("Entrada invalida. Ingrese numeros.")

        def validar_servicio(texto):
            opcion = input(f"{texto} [True/False]: ")
            while opcion != "True" and opcion != "False":
                opcion = input(f"Entrada inválida. Ingresa True o False para {texto}: ")
            if opcion == "True":
                return True
            else:
                return False
        
        aire = validar_servicio("Aire acondicionado")
        frigo = validar_servicio("Frigobar")
        balcon = validar_servicio("Balcón")

        habitacionModificada = {
            "disponible": disponible,
            "capacidad": int(capacidad),
            "costoPorDia": int(costoPorDia),
            "servicios": {
                "aire acondicionado": aire,
                "frigobar": frigo,
                "balcon": balcon
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

    while not (dni.isdigit() and len(dni) == 8):
        dni = input("DNI inválido. Ingrese un DNI de 8 dígitos: ")

    if dni in _clientes and _clientes[dni]['activo']:

        while True:
            capacidad_input = input("Ingrese cantidad de personas: ")
            if capacidad_input.isdigit() and int(capacidad_input) > 0:
                capacidad = int(capacidad_input)
                break
            else:
                print("Por favor, ingrese un número válido mayor que cero.")
        
        def pedir_confirmacion(texto):
            """
            Funcion para simplificar un paso dentro de otra funcion, lo que realiza es la validacion de los servicios.
            """
            opcion = input(f"{texto} [True/False]: ")
            while opcion != "True" and opcion != "False":
                opcion = input(f"Entrada inválida. Ingresa True o False para {texto}: ")
            if opcion == "True":
                return True
            else:
                return False

        aireAcondicionado = pedir_confirmacion("Aire acondicionado")
        frigo = pedir_confirmacion("Frigobar")
        balcon = pedir_confirmacion("Balcon")

        for nroHabitacion, habitacionDatos in _habitaciones.items():
            if (
                habitacionDatos.get('disponible') and
                capacidad == habitacionDatos.get('capacidad') and
                aireAcondicionado == habitacionDatos.get('servicios', {}).get('aire acondicionado') and
                frigo == habitacionDatos.get('servicios', {}).get('frigobar') and
                balcon == habitacionDatos.get('servicios', {}).get('balcon')
            ):
                idReserva = datetime.now().strftime("%Y.%m.%d %H.%M.%S")

                while True:
                    fechaEntrada = input("Fecha de ingreso (DD/MM/AAAA): ")
                    try:
                        fechaEntrada = datetime.strptime(fechaEntrada, "%d/%m/%Y")
                        if fechaEntrada < datetime.now():
                            print("=============================")
                            print("La fecha de entrada no puede ser anterior a hoy.")
                            return
                        break
                    except ValueError:
                        print("Fecha inválida. Intente nuevamente.")

                while True:
                    fechaSalida = input("Fecha de salida (DD/MM/AAAA): ")
                    try:
                        fechaSalida = datetime.strptime(fechaSalida, "%d/%m/%Y")
                        if fechaSalida <= fechaEntrada:
                            print("=============================")
                            print("La fecha de salida debe ser posterior a la de entrada.")
                            return
                        break
                    except ValueError:
                        print("Fecha inválida. Intente nuevamente.")
                metodoPago = input("Ingrese metodo de pago: [1] Efectivo / [2] Tarjeta: ")
                while (metodoPago != "1" and metodoPago != "2"):
                    metodoPago = input("Error. Ingrese metodo de pago: [1] Efectivo / [2] Tarjeta: ")
                if metodoPago == "1":
                    metodoPago = "Efectivo"
                else:
                    metodoPago = "Tarjeta"
                
                dias = (fechaSalida - fechaEntrada).days
                totalPagar = dias * habitacionDatos.get('costoPorDia')

                nuevaReserva = {
                    
                    "dni": dni,
                    "nombre": _clientes[dni].get('nombre', 'No disponible'),
                    "nroHabitacion": nroHabitacion,
                    "activo": True,
                    "cantidadPersonas": capacidad,
                    "fechaDeEntrada": fechaEntrada.strftime("%d/%m/%Y"),
                    "fechaDeSalida": fechaSalida.strftime("%d/%m/%Y"),
                    "metodoDePago": metodoPago,
                    "totalPagar": totalPagar
                }
                _reservas[idReserva] = nuevaReserva
                _habitaciones[nroHabitacion]['disponible'] = False
                print("Reserva realizada con exito. Total a pagar: $", totalPagar)
                return
        print("No hay habitacion para esa cantidad de personas y servicios seleccionados.")
    else:
        print("==========================")
        print("Usted es un cliente inactivo o no registrado por lo tanto no puede realizar reservas.")


def listarReservasActivas(_reservas):
    """
    Muestra todas las reservas que están activas en el sistema con sus detalles.
    """
    for idReserva, otrosDatos in _reservas.items():
        if otrosDatos['activo']:
            print(f"nombre: {otrosDatos.get('nombre', 'No disponible')}")
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
    while True:
        try:
            año = int(input("Ingrese año: "))
            break
        except ValueError:
            print("No ingreso una fecha o ingreso un dato que no es digito. Vuelva a introducir la fecha.")

    resumen = {i: [0]*12 for i in range(1, 11)}

    for datos in reservas.values():
        if datos["activo"]:
            fecha_str = datos["fechaDeEntrada"]
            try:
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            except ValueError:
                print(f"Formato de fecha inválido: {fecha_str}")
                continue  # Salta esta reserva si tiene mal la fecha

            if fecha.year == año:
                mes = fecha.month
                try:
                    habitacion = int(datos["nroHabitacion"])
                except ValueError:
                    print(f"NroHabitacion inválido: {datos['nroHabitacion']}")
                    continue

                if habitacion not in resumen:
                    resumen[habitacion] = [0] * 12
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
                    agendarReserva(clientela, habitaciones, reservas)
                elif opcionSubmenu == "2":
                    listarReservasActivas(reservas)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE INFORMES")
                    print("---------------------------")
                    print("[1] Resumen Anual de reservas por habitación")
                    print("[2] Informe de ingresos a habitaciones del mes en curso")
                    print("[3] Resumen de monto en pesos por año y mes")
                    print("[4] Habitaciones más rentables")
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
                    informeIngresosPorFechaEntradaDelMes(reservas, clientela)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    resumenMontoPorAñoYMes(reservas)

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    habitacionesMasRentables(reservas)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()# Punto de entrada al programa
# main()