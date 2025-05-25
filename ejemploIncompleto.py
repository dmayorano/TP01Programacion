"""
-----------------------------------------------------------------------------------------------
Título: ...
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


def listarClientesActivos(_clientes):
    """
    doctring
    """
    # Se muestran todos los datos del cliente y el detalle de sus tarjetas
    # PENDIENTE: FALTA FILTRAR PARA SÓLO LISTAR LOS CLIENTES ACTIVOS
    for dni, otrosDatos in _clientes.items():
        print(f"CLIENTE: {dni}")
        print(f"NOMBRE: {otrosDatos['nombre']}")
        print(f"EDAD: {otrosDatos['edad']}")
        print(f"SEXO: {otrosDatos['sexo']}")
        print("TARJETAS:")
        for tarjeta, nombreTarjeta in otrosDatos["tarjetas"].items():
            print(f"\t{nombreTarjeta}")
        
        print()
    
    return


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------

    # Diccionario de datos de clientes: KEY=Documento del cliente, VALUE=Otros datos del cliente
    clientes = {
        "38111222":{"activo"  :True,
                    "nombre"  :"Juan José Galván",
                    "edad"    :30,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"AMEX",
                                "tarjeta3":"MASTER"
                                }
                   },
        "40233455":{"activo"  :True,
                    "nombre"  :"María Luisa Pérez",
                    "edad"    :28,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"AMEX",
                                "tarjeta3":""
                                }
                   },
        "39128473":{"activo"  :True,
                    "nombre"  :"Carlos Daniel Ruiz",
                    "edad"    :35,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"VISA",
                                "tarjeta3":""
                                }
                   },
        "40399284":{"activo"  :True,
                    "nombre"  :"Lucía Fernández",
                    "edad"    :26,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "37283910":{"activo"  :True,
                    "nombre"  :"Martín Alejandro López",
                    "edad"    :42,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"MASTER",
                                "tarjeta3":"AMEX"
                                }
                   },
        "38902764":{"activo"  :True,
                    "nombre"  :"Sofía Beatriz Ramos",
                    "edad"    :31,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "41392847":{"activo"  :True,
                    "nombre"  :"Nicolás Emiliano Gómez",
                    "edad"    :29,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"MASTER",
                                "tarjeta3":"VISA"
                                }
                   },
        "40567219":{"activo"  :True,
                    "nombre"  :"Valentina Herrera",
                    "edad"    :24,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "39384756":{"activo"  :True,
                    "nombre"  :"Julián Castro",
                    "edad"    :36,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"AMEX",
                                "tarjeta3":""
                                }
                   },
        "38472918":{"activo"  :True,
                    "nombre"  :"Carla Noemí Torres",
                    "edad"    :27,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"VISA",
                                "tarjeta3":"MASTER"
                                }
            },
        "40298372":{"activo"  :True,
                    "nombre"  :"Agustín Vega",
                    "edad"    :33,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"AMEX",
                                "tarjeta3":""
                                }
                },
        "39482736":{"activo"  :True,
                    "nombre"  :"Romina Delgado",
                    "edad"    :39,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "37583927":{"activo"  :True,
                    "nombre"  :"Esteban Molina",
                    "edad"    :45,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"MASTER",
                                "tarjeta3":""
                                }
                   },
        "40672918":{"activo"  :True,
                    "nombre"  :"Milagros Acosta",
                    "edad"    :22,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"AMEX",
                                "tarjeta3":"MASTER"
                                }
                   },
        "39817264":{"activo"  :True,
                    "nombre"  :"Gonzalo Paredes",
                    "edad"    :34,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "37729384":{"activo"  :True,
                    "nombre"  :"Antonella Figueroa",
                    "edad"    :30,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"MASTER",
                                "tarjeta3":""
                                }
                   },
        "40384729":{"activo"  :True,
                    "nombre"  :"Leandro Navarro",
                    "edad"    :40,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"VISA",
                                "tarjeta3":""
                                }
                   },
        "38172947":{"activo"  :True,
                    "nombre"  :"Camila Duarte",
                    "edad"    :29,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"AMEX",
                                "tarjeta3":"VISA"
                                }
                   },
        "39947283":{"activo"  :True,
                    "nombre"  :"Federico Romero",
                    "edad"    :38,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "39485720":{"activo"  :True,
                    "nombre"  :"Daniela Montenegro",
                    "edad"    :32,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"VISA",
                                "tarjeta3":"MASTER"
                                }
                   },
        "38472910":{"activo"  :True,
                    "nombre"  :"Tomás Ibáñez",
                    "edad"    :27,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "39592834":{"activo"  :True,
                    "nombre"  :"Micaela Robles",
                    "edad"    :26,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"AMEX",
                                "tarjeta3":""
                                }
                   },
        "41294837":{"activo"  :True,
                    "nombre"  :"Andrés Quiroga",
                    "edad"    :31,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"MASTER",
                                "tarjeta3":"VISA"
                                }
                   },
        "40291736":{"activo"  :True,
                    "nombre"  :"Florencia Salas",
                    "edad"    :25,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"VISA",
                                "tarjeta3":""
                                }
                   },
        "39284730":{"activo"  :True,
                    "nombre"  :"Rodrigo Cabrera",
                    "edad"    :37,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "38817290":{"activo"  :True,
                    "nombre"  :"Elena Ponce",
                    "edad"    :30,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"MASTER",
                                "tarjeta3":"AMEX"
                                }
                   },
        "40671829":{"activo"  :True,
                    "nombre"  :"Matías Barreto",
                    "edad"    :33,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"",
                                "tarjeta3":""
                                }
                   },
        "37928192":{"activo"  :True,
                    "nombre"  :"Julieta San Martín",
                    "edad"    :28,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"VISA",
                                "tarjeta2":"AMEX",
                                "tarjeta3":""
                                }
                   },
        "40718293":{"activo"  :True,
                    "nombre"  :"Iván Méndez",
                    "edad"    :35,
                    "sexo"    :"M",
                    "tarjetas":{"tarjeta1":"AMEX",
                                "tarjeta2":"VISA",
                                "tarjeta3":"MASTER"
                                }
                   },
        "38571820":{"activo"  :True,
                    "nombre"  :"Pamela Córdoba",
                    "edad"    :34,
                    "sexo"    :"F",
                    "tarjetas":{"tarjeta1":"MASTER",
                                "tarjeta2":"AMEX",
                                "tarjeta3":""
                                }
                   }
    }

    # Se ordena el diccionario por el dni del cliente
    clientes = dict(sorted(clientes.items()))


    # Diccionario de datos de productos: KEY=Código de producto, VALUE=Otros datos del producto
    ...
    
    
    # Diccionario de datos de ventas: KEY=Código de venta, VALUE=Otros datos de la venta
    ...


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
            print("[1] Gestión de Clientes")
            print("[2] Opción 2")
            print("[3] Opción 3")
            print("[4] Opción 4")
            print("[5] Opción 5")
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
                    print("[2] Inactivar Cliente")
                    print("[3] Modificar Cliente")
                    print("[4] Listar Clientes Activos")
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
                    clientes = inactivarCliente(clientes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarClientesActivos(clientes)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            ...
        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            ...
        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            ...

        elif opcionMenuPrincipal == "5":   # Opción 5 del menú principal
            ...

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()