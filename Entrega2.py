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
import json
import os


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def cargar_datos(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    else:
        return {}

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

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


def resumenMontoPorAñoYMes():
    """
    Muestra un resumen de los montos en pesos por año y mes,
    cargando los datos desde reservas.json.
    """
    reservas = cargar_datos("reservas.json")

    if not reservas:
        print("No hay reservas registradas.")
        return

    resumen = {}

    for datos in reservas.values():
        if datos.get("activo"):
            try:
                fecha = datetime.strptime(datos["fechaDeEntrada"], "%d/%m/%Y")
            except ValueError:
                print(f"Fecha inválida en reserva: {datos}")
                continue

            año = fecha.year
            mes = fecha.month
            totalPagar = datos.get("totalPagar", 0)

            if año not in resumen:
                resumen[año] = [0] * 12

            resumen[año][mes - 1] += totalPagar

    print("=" * 70)
    print("Resumen de monto en pesos por año y mes")
    print("=" * 70)
    for año, meses in resumen.items():
        print(f"Año {año}")
        print("Mes | Monto")
        for i, monto in enumerate(meses):
            if monto > 0:
                nombre_mes = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", 
                              "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"][i]
                print(f"{nombre_mes} | ${monto:,.2f}")
        print()

    print("=" * 70)
    print("Resumen de monto en pesos por año y mes (matriz)")
    print("=" * 70)
    print("Año | " + " ".join([f"{mes:<10}" for mes in ["Ene", "Feb", "Mar", "Abr", "May", "Jun", 
                                                       "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]]))
    for año, meses in resumen.items():
        linea = f"{año:<4} | " + " ".join(f"${monto:>9,.2f}" for monto in meses)
        print(linea)


def informeIngresosPorFechaEntradaDelMes():
    """
    Muestra un informe de las reservas que tienen fecha de ingreso en el mes actual,
    cargando los datos desde reservas.json y clientes.json.
    """
    reservas = cargar_datos("reservas.json")
    clientes = cargar_datos("clientes.json")

    if not reservas:
        print("No hay reservas registradas.")
        return

    fechaActual = datetime.now()
    mesActual = fechaActual.month
    añoActual = fechaActual.year

    print("=" * 100)
    print(f"{'Fecha ingreso':<20} {'Cliente':<20} {'Nro. Habitación':<15} {'Cant. Personas':<15} {'Método de Pago':<15} {'Total':<10}")
    print("-" * 100)

    reservasEncontradas = False

    for reserva in reservas.values():
        try:
            fechaEntrada = datetime.strptime(reserva["fechaDeEntrada"], "%d/%m/%Y")
        except ValueError:
            print(f"Fecha inválida en reserva: {reserva}")
            continue

        if reserva.get("activo") and fechaEntrada.month == mesActual and fechaEntrada.year == añoActual:
            dni = reserva.get("dni")
            cliente = clientes.get(dni, {}).get("nombre", "No disponible")
            print(f"{reserva['fechaDeEntrada']:<20} {cliente:<20} {reserva['nroHabitacion']:<15} "
                  f"{reserva['cantidadPersonas']:<15} {reserva['metodoDePago']:<15} ${reserva['totalPagar']:<10,.2f}")
            reservasEncontradas = True

    if not reservasEncontradas:
        print("No se encontraron ingresos para el mes actual.")

def altaCliente():
    """
    Solicita los datos de un nuevo cliente y lo registra si el DNI no existe.
    Usa archivo JSON, validaciones y control de excepciones.
    """
    import re

    def validar_email(email):
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron, email) is not None

    clientes = cargar_datos("clientes.json")

    while True:
        try:
            dni = input("Ingresa tu DNI: ")
            if not (dni.isdigit() and len(dni) == 8):
                raise ValueError("DNI inválido. Debe tener 8 dígitos numéricos.")
            break
        except ValueError as e:
            print(e)

    if dni in clientes:
        print("El cliente ya existe.")
        return

    while True:
        nombre = input("Ingresa tu nombre y apellido: ")
        if not nombre.replace(" ", "").isalpha():
            print("El nombre no puede contener números ni símbolos.")
        else:
            break

    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Edad inválida. Ingrese un número entero.")

    while True:
        email = input("Ingrese su correo electrónico: ")
        if validar_email(email):
            break
        else:
            print("Email inválido. Intente nuevamente.")

    while True:
        telefono = input("Ingrese su número de teléfono (10-15 dígitos): ")
        if telefono.isdigit() and 10 <= len(telefono) <= 15:
            break
        else:
            print("Número inválido. Intente nuevamente.")

    alterno = input("Ingrese un teléfono alternativo (opcional): ")
    if alterno != "":
        while not (alterno.isdigit() and 10 <= len(alterno) <= 15):
            alterno = input("Número alternativo inválido. Intente nuevamente o deje vacío: ")

    nuevoCliente = {
        "activo": True,
        "nombre": nombre,
        "edad": edad,
        "email": email,
        "telefonos": {
            "movil": telefono,
            "alterno": alterno
        }
    }

    clientes[dni] = nuevoCliente
    guardar_datos("clientes.json", clientes)

    print("==============================")
    print("Cliente agregado con éxito.")


def inactivarCliente():
    """
    Inactiva un cliente en el archivo clientes.json dado su DNI.
    """
    clientes = cargar_datos("clientes.json")

    while True:
        try:
            dni = input("DNI del cliente a inactivar: ")
            if not dni.isdigit() or len(dni) != 8:
                raise ValueError("DNI inválido. Debe tener 8 dígitos numéricos.")
            break
        except ValueError as ve:
            print(ve)

    if dni in clientes:
        if not clientes[dni]["activo"]:
            print(f"El cliente {dni} ya estaba inactivo.")
        else:
            clientes[dni]["activo"] = False
            guardar_datos("clientes.json", clientes)
            print(f"Cliente {dni} inactivado con éxito.")
    else:
        print("No existe un cliente con ese DNI.")



def listarClientesActivos():
    """
    Muestra en pantalla los datos de todos los clientes activos registrados en clientes.json.
    """
    clientes = cargar_datos("clientes.json")

    if not clientes:
        print("No hay clientes registrados.")
        return

    encontrados = False

    for dni, datos in clientes.items():
        if datos.get('activo'):
            encontrados = True
            print(f"DNI: {dni}")
            print(f"NOMBRE: {datos.get('nombre', 'No disponible')}")
            print(f"EDAD: {datos.get('edad', 'No disponible')}")
            print("TELEFONOS:")
            for tipo, numero in datos.get("telefonos", {}).items():
                if numero:
                    print(f"\t{tipo}: {numero}")
            print("========================================")

    if not encontrados:
        print("No hay clientes activos para mostrar.")



def modificarCliente():
    """
    Permite modificar los datos de un cliente existente (nombre, edad, email, teléfonos, estado).
    Lee y guarda en clientes.json. Aplica validaciones y control de errores.
    """
    import re

    def validar_email(email):
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron, email) is not None

    clientes = cargar_datos("clientes.json")

    dni = input("Ingrese el DNI del cliente a modificar: ")
    while not (dni.isdigit() and len(dni) == 8):
        dni = input("DNI inválido. Ingrese un número de 8 dígitos: ")

    if dni not in clientes:
        print("El cliente no existe.")
        return

    cliente = clientes[dni]
    print("Si desea mantener un dato actual, presione ENTER.\n")

    # Estado
    estado = input(f"¿Activo? Actual: {cliente['activo']} (1=Sí / 2=No): ")
    if estado == "1":
        activo = True
    elif estado == "2":
        activo = False
    else:
        activo = cliente['activo']

    # Nombre
    nombre = input(f"Nombre actual: {cliente['nombre']}: ")
    if nombre.strip() == "":
        nombre = cliente['nombre']
    else:
        while not nombre.replace(" ", "").isalpha():
            nombre = input("Nombre inválido. Ingrese solo letras y espacios: ")

    # Edad
    edad_input = input(f"Edad actual: {cliente['edad']}: ")
    if edad_input.strip() == "":
        edad = cliente['edad']
    else:
        while not edad_input.isdigit() or int(edad_input) < 0:
            edad_input = input("Edad inválida. Ingrese un número positivo: ")
        edad = int(edad_input)

    # Email
    email = input(f"Email actual: {cliente.get('email', 'No registrado')}: ")
    if email.strip() == "":
        email = cliente.get('email', '')
    else:
        while not validar_email(email):
            email = input("Email inválido. Ingrese nuevamente: ")

    # Teléfono móvil
    movil = input(f"Teléfono actual: {cliente['telefonos']['movil']}: ")
    if movil.strip() == "":
        movil = cliente['telefonos']['movil']
    else:
        while not (movil.isdigit() and 10 <= len(movil) <= 15):
            movil = input("Número inválido. Ingrese entre 10 y 15 dígitos: ")

    # Teléfono alterno
    alterno = input(f"Tel. alternativo actual: {cliente['telefonos']['alterno']}: ")
    if alterno.strip() == "":
        alterno = cliente['telefonos']['alterno']
    else:
        while not (alterno.isdigit() and 10 <= len(alterno) <= 15):
            alterno = input("Número alternativo inválido. Ingrese entre 10 y 15 dígitos: ")

    cliente_actualizado = {
        "activo": activo,
        "nombre": nombre,
        "edad": edad,
        "email": email,
        "telefonos": {
            "movil": movil,
            "alterno": alterno
        }
    }

    clientes[dni] = cliente_actualizado
    guardar_datos("clientes.json", clientes)

    print("Cliente modificado con éxito.")


def altaHabitacion():
    """
    Registra una nueva habitación en habitaciones.json si no existe previamente.
    """
    habitaciones = cargar_datos("habitaciones.json")

    nroHabitacion = input("Ingrese número de la habitación: ")
    while not (nroHabitacion.isdigit() and int(nroHabitacion) >= 0):
        nroHabitacion = input("Número inválido. Ingrese un número positivo: ")

    if nroHabitacion in habitaciones:
        print("La habitación ya existe.")
        return

    def validar_servicio(texto):
        opcion = input(f"{texto} [True/False]: ")
        while opcion not in ["True", "False"]:
            opcion = input(f"Entrada inválida. Ingrese True o False para {texto}: ")
        return opcion == "True"

    # Capacidad
    while True:
        try:
            capacidad = int(input("Ingrese capacidad de personas: "))
            if capacidad <= 0:
                print("La capacidad debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error. Ingrese números enteros.")

    # Costo por día
    while True:
        try:
            costoPorDia = int(input("Ingrese costo por día: "))
            if costoPorDia <= 0:
                print("El costo debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error. Ingrese números enteros.")

    aire = validar_servicio("¿Tiene aire acondicionado?")
    frigo = validar_servicio("¿Tiene frigobar?")
    balcon = validar_servicio("¿Tiene balcón?")

    nuevaHabitacion = {
        "disponible": True,
        "capacidad": capacidad,
        "costoPorDia": costoPorDia,
        "servicios": {
            "aire acondicionado": aire,
            "frigobar": frigo,
            "balcon": balcon
        }
    }

    habitaciones[nroHabitacion] = nuevaHabitacion
    guardar_datos("habitaciones.json", habitaciones)

    print("Habitación agregada con éxito.")



def inactivarHabitacion():
    """
    Marca una habitación como no disponible en habitaciones.json.
    """
    habitaciones = cargar_datos("habitaciones.json")

    nroHabitacion = input("Ingrese número de habitación a inhabilitar: ")
    while not (nroHabitacion.isdigit() and int(nroHabitacion) >= 0):
        nroHabitacion = input("Número inválido. Ingrese un número válido y positivo: ")

    if nroHabitacion in habitaciones:
        habitaciones[nroHabitacion]["disponible"] = False
        guardar_datos("habitaciones.json", habitaciones)
        print(f"La habitación {nroHabitacion} fue inhabilitada.")
    else:
        print(f"La habitación {nroHabitacion} no existe.")



def listarHabitacionesActivas():
    """
    Muestra en pantalla todas las habitaciones disponibles cargadas desde habitaciones.json.
    """
    habitaciones = cargar_datos("habitaciones.json")

    if not habitaciones:
        print("No hay habitaciones registradas.")
        return

    alguna_activa = False

    for nroHabitacion, datos in habitaciones.items():
        if datos.get('disponible', False):
            alguna_activa = True
            print(f"Habitación: {nroHabitacion}")
            print(f"Capacidad: {datos.get('capacidad', 'No disponible')}")
            print(f"Costo por día: ${datos.get('costoPorDia', 'No disponible')}")
            print("Servicios:")
            for servicio, disponible in datos.get("servicios", {}).items():
                print(f"  - {servicio.capitalize()}: {'Sí' if disponible else 'No'}")
            print("=" * 40)

    if not alguna_activa:
        print("No hay habitaciones activas disponibles.")



def modificarHabitacion():
    """
    Permite modificar una habitación existente cargando y guardando en habitaciones.json.
    """
    habitaciones = cargar_datos("habitaciones.json")

    nroHabitacion = input("Ingrese número de habitación a modificar: ")
    while not (nroHabitacion.isdigit() and int(nroHabitacion) >= 0):
        nroHabitacion = input("Número inválido. Ingrese un número válido y positivo: ")

    if nroHabitacion not in habitaciones:
        print("La habitación no existe.")
        return

    habitacion = habitaciones[nroHabitacion]

    # Estado de disponibilidad
    disponible = input("¿Está disponible? [True/False] (ENTER para mantener actual): ")
    if disponible == "":
        disponible = habitacion.get("disponible", True)
    elif disponible in ["True", "False"]:
        disponible = disponible == "True"
    else:
        print("Entrada inválida. Se mantendrá el valor anterior.")
        disponible = habitacion.get("disponible", True)

    # Capacidad
    nueva_capacidad = input(f"Capacidad actual: {habitacion['capacidad']} - Nueva capacidad (ENTER para mantener): ")
    if nueva_capacidad == "":
        capacidad = habitacion["capacidad"]
    else:
        while not nueva_capacidad.isdigit() or int(nueva_capacidad) <= 0:
            nueva_capacidad = input("Capacidad inválida. Ingrese un número entero mayor a 0: ")
        capacidad = int(nueva_capacidad)

    # Costo por día
    nuevo_costo = input(f"Costo actual: ${habitacion['costoPorDia']} - Nuevo costo (ENTER para mantener): ")
    if nuevo_costo == "":
        costoPorDia = habitacion["costoPorDia"]
    else:
        while not nuevo_costo.isdigit() or int(nuevo_costo) <= 0:
            nuevo_costo = input("Costo inválido. Ingrese un número mayor a 0: ")
        costoPorDia = int(nuevo_costo)

    def modificar_servicio(nombre, valor_actual):
        nuevo = input(f"{nombre.capitalize()} actual: {valor_actual} - ¿Nuevo valor? [True/False] (ENTER para mantener): ")
        if nuevo == "":
            return valor_actual
        while nuevo not in ["True", "False"]:
            nuevo = input("Entrada inválida. Ingrese True o False o ENTER para mantener: ")
        return nuevo == "True"

    aire = modificar_servicio("aire acondicionado", habitacion["servicios"].get("aire acondicionado", False))
    frigo = modificar_servicio("frigobar", habitacion["servicios"].get("frigobar", False))
    balcon = modificar_servicio("balcon", habitacion["servicios"].get("balcon", False))

    habitaciones[nroHabitacion] = {
        "disponible": disponible,
        "capacidad": capacidad,
        "costoPorDia": costoPorDia,
        "servicios": {
            "aire acondicionado": aire,
            "frigobar": frigo,
            "balcon": balcon
        }
    }

    guardar_datos("habitaciones.json", habitaciones)
    print("Habitación modificada con éxito.")


def agendarReserva():
    """
    Agenda una reserva si el cliente está activo y hay una habitación disponible.
    Guarda todo en reservas.json y actualiza habitaciones.json.
    """
    clientes = cargar_datos("clientes.json")
    habitaciones = cargar_datos("habitaciones.json")
    reservas = cargar_datos("reservas.json")

    dni = input("Ingrese su DNI: ")
    while not (dni.isdigit() and len(dni) == 8):
        dni = input("DNI inválido. Ingrese 8 dígitos numéricos: ")

    if dni not in clientes or not clientes[dni]["activo"]:
        print("El cliente no está activo o no está registrado.")
        return

    while True:
        capacidad_input = input("Ingrese cantidad de personas: ")
        if capacidad_input.isdigit() and int(capacidad_input) > 0:
            capacidad = int(capacidad_input)
            break
        print("Ingrese un número válido mayor que cero.")

    def pedir_servicio(nombre):
        valor = input(f"{nombre} [True/False]: ")
        while valor not in ["True", "False"]:
            valor = input(f"Entrada inválida. Ingrese 'True' o 'False' para {nombre}: ")
        return valor == "True"

    aire = pedir_servicio("Aire acondicionado")
    frigo = pedir_servicio("Frigobar")
    balcon = pedir_servicio("Balcón")

    for nroHabitacion, datosHab in habitaciones.items():
        if (
            datosHab.get("disponible") and
            datosHab.get("capacidad") == capacidad and
            datosHab["servicios"].get("aire acondicionado") == aire and
            datosHab["servicios"].get("frigobar") == frigo and
            datosHab["servicios"].get("balcon") == balcon
        ):
            # Fecha ingreso
            while True:
                fechaEntradaStr = input("Fecha de ingreso (DD/MM/AAAA): ")
                try:
                    fechaEntrada = datetime.strptime(fechaEntradaStr, "%d/%m/%Y")
                    if fechaEntrada < datetime.now():
                        print("La fecha de entrada no puede ser anterior a hoy.")
                        continue
                    break
                except ValueError:
                    print("Formato de fecha inválido.")

            # Fecha salida
            while True:
                fechaSalidaStr = input("Fecha de salida (DD/MM/AAAA): ")
                try:
                    fechaSalida = datetime.strptime(fechaSalidaStr, "%d/%m/%Y")
                    if fechaSalida <= fechaEntrada:
                        print("La salida debe ser posterior al ingreso.")
                        continue
                    break
                except ValueError:
                    print("Formato de fecha inválido.")

            metodo = input("Método de pago [1] Efectivo / [2] Tarjeta: ")
            while metodo not in ["1", "2"]:
                metodo = input("Opción inválida. Elija [1] o [2]: ")
            metodo = "Efectivo" if metodo == "1" else "Tarjeta"

            dias = (fechaSalida - fechaEntrada).days
            total = dias * datosHab["costoPorDia"]

            idReserva = datetime.now().strftime("%Y.%m.%d %H.%M.%S")

            nuevaReserva = {
                "dni": dni,
                "nombre": clientes[dni]["nombre"],
                "nroHabitacion": nroHabitacion,
                "activo": True,
                "cantidadPersonas": capacidad,
                "fechaDeEntrada": fechaEntrada.strftime("%d/%m/%Y"),
                "fechaDeSalida": fechaSalida.strftime("%d/%m/%Y"),
                "metodoDePago": metodo,
                "totalPagar": total
            }

            reservas[idReserva] = nuevaReserva
            habitaciones[nroHabitacion]["disponible"] = False

            guardar_datos("reservas.json", reservas)
            guardar_datos("habitaciones.json", habitaciones)

            print(f"Reserva realizada con éxito. Total a pagar: ${total:,.2f}")
            return

    print("No hay habitaciones disponibles con esas características.")

def listarReservasActivas():
    """
    Muestra todas las reservas activas desde reservas.json con sus detalles.
    """
    reservas = cargar_datos("reservas.json")
    if not reservas:
        print("No hay reservas registradas.")
        return

    print(f"{'ID Reserva':<22} {'Nombre':<20} {'DNI':<10} {'Habitación':<10} {'Personas':<10} {'Ingreso':<12} {'Salida':<12} {'Pago':<10} {'Total':<10}")
    print("-" * 120)

    for idReserva, datos in reservas.items():
        if datos.get("activo", False):
            print(f"{idReserva:<22} {datos['nombre']:<20} {datos['dni']:<10} {datos['nroHabitacion']:<10} "
                  f"{datos['cantidadPersonas']:<10} {datos['fechaDeEntrada']:<12} {datos['fechaDeSalida']:<12} "
                  f"{datos['metodoDePago']:<10} ${datos['totalPagar']:,.2f}")



def reporteReservasPorAño():
    """
    Genera un reporte resumen de la cantidad de reservas por habitación para un año dado,
    cargando los datos desde reservas.json.
    """
    reservas = cargar_datos("reservas.json")

    if not reservas:
        print("No hay reservas registradas.")
        return

    while True:
        try:
            año = int(input("Ingrese el año para el reporte: "))
            break
        except ValueError:
            print("Entrada inválida. Ingrese un año como número (ej. 2025).")

    # Inicializa el resumen con 12 meses por cada habitación (del 1 al 10)
    resumen = {i: [0]*12 for i in range(1, 11)}

    for datos in reservas.values():
        if datos.get("activo"):
            try:
                fecha = datetime.strptime(datos["fechaDeEntrada"], "%d/%m/%Y")
            except ValueError:
                print(f"Fecha inválida en reserva: {datos}")
                continue

            if fecha.year == año:
                mes = fecha.month
                try:
                    habitacion = int(datos["nroHabitacion"])
                except ValueError:
                    print(f"Número de habitación inválido: {datos['nroHabitacion']}")
                    continue

                if habitacion not in resumen:
                    resumen[habitacion] = [0]*12
                resumen[habitacion][mes - 1] += 1

    print("=" * 70)
    print(f"Resumen de cantidad de reservas por habitación - Año {año}")
    print("=" * 70)
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
"""
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
"""
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
                    altaCliente()
                    
                    
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    modificarCliente()
                    
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    inactivarCliente()
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    
                    listarClientesActivos()

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
                    altaHabitacion()
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    modificarHabitacion()
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    inactivarHabitacion()
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarHabitacionesActivas()

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
                    agendarReserva()
                elif opcionSubmenu == "2":
                    listarReservasActivas()

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
                    reporteReservasPorAño()
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    informeIngresosPorFechaEntradaDelMes()
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    resumenMontoPorAñoYMes()

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    habitacionesMasRentables()

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()# Punto de entrada al programa
# main()