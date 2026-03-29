#Ejercicio 1
# Se ingresa el nombre del cliente
nombre = input("Ingrese el nombre del cliente: ")
#Se valida que el nombre ingresado no este vacio o sea un digito
while not nombre .isalpha():
    print("Nombre mal ingresado")
    nombre = input("Ingrese el nombre del cliente: ")
#Se ingresa la cantidad de productos
cantidad_productos = input("Ingrese la cantidad de productos: ")
#Se valida que la cantidad ingresada sea un digito y distinta a 0
while not cantidad_productos.isdigit() or cantidad_productos == "0":
    print("Cantidad erronea")
    cantidad_productos = input("Ingrese la cantidad de productos: ")
# Se transforma cantidad_producto a un int
cantidad_productos = int(cantidad_productos)
# acumuladores del total con y sin descuento
descuento = 10
precio_total_sin_descuento = 0
total_sin_descuento = 0
total_con_descuento = 0


#Ingreso de los datos precio y descuento de la cantidad de productos ingresada
for cant_product in range (cantidad_productos):
    precio = input("Ingrese el precio: ")
    while not precio .isdigit:
        print("El precio debe estar expresado en digitos")
        precio = input("Ingrese el precio: ")
    precio = float(precio)
    precio_total_sin_descuento += precio
    val_descuento = input("El producto lleva descuento?(Ingrese S / N): ").lower()
    while not val_descuento =="s" and not val_descuento == "n":
        print("Error, ingreso solo la letra ""S"" lleva o ""N"" si no lleva")
        val_descuento = input("El producto lleva descuento?(Ingrese S / N): ").lower()
    if val_descuento == "s":
        total_con_descuento += precio
    else:
        total_sin_descuento += precio
#calculos finales
descuento_aplicado = (total_con_descuento * descuento)/100
descuento_aplicado_final = (total_con_descuento - descuento_aplicado)+total_sin_descuento
total_ahorrado = precio_total_sin_descuento - descuento_aplicado_final

print ("--------------")
print(f"Total sin descuento: {precio_total_sin_descuento}")
print(f"Total con descuento: {descuento_aplicado_final}")
print(f"Total Ahorrado: {total_ahorrado} ") 
print(f"Promedio por producto: {descuento_aplicado_final / cantidad_productos} ")
#========================================================================================================================================
#Ejercicio 2
# Se especifican credenciales
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

#Bandera
intentos = 3
ingreso_exitoso = False

for cont in range (intentos):
    usuario = input("Ingrese usario: ")
    contraseña = input("Ingrese contraseña: ")
#si el usuario y contraseña son correctos ingresa y sale del bucle
    if usuario == USUARIO_CORRECTO and contraseña == CLAVE_CORRECTA:
        print("Correcto")
        ingreso_exitoso = True
        break
    else:
        if cont < 2:
            print(f"Credenciales invalidas, te quedan {intentos-1} intentos")
            intentos -= 1
        else:
            print("Usuario bloqueado")    
if ingreso_exitoso:
    opcion = "" # Inicializamos la variable
    
    while opcion != "4":
        # 1. Mostramos el menú y pedimos la opción
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Estado de la Inscripcion")
        print("2. Cambio de Contraseña")
        print("3. Frase motivacional")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        # 2. Validamos que la opción sea válida
        while opcion not in ["1", "2", "3", "4"]:
            print("Opcion incorrecta, debe ingresar 1, 2, 3 o 4")
            opcion = input("Ingrese el menu(1,2,3 o 4): ")

        # 3. Ejecutamos la acción según la opción
        match opcion:
            case "1":
                print("Estado: Inscripto")
            case "2":
                nueva_clv = input("Nueva contraseña (mínimo 6 caracteres): ")
                confirma = input("Confirme nueva clave: ")
                
                while nueva_clv != confirma or len(nueva_clv) <= 6:
                    print("Error en el cambio de clave")
                    if len(nueva_clv) <= 6:
                        print("- Debe tener al menos 6 caracteres")
                    if nueva_clv != confirma:
                        print("- Las contraseñas no coinciden")
                    
                    nueva_clv = input("Intente de nuevo: ")
                    confirma = input("Confirme de nuevo: ")
                
                CLAVE_CORRECTA = nueva_clv # Actualizamos la clave real
                print("Contraseña actualizada correctamente")
            case "3":
                print("Sic parvis magna: La grandeza nace de pequeños comienzos")
            case "4":
                print("Saliendo del sistema...")

#=========================================================================================================================================
#Ejercicio 3

nombre_operador = input("Ingrese Nombre del operador: ").lower()

while not nombre_operador.isalpha(): #validacion de solo letras
    print("Error, solo puede ingresar letras")
    nombre_operador = input("Ingrese Nombre del operador: ").lower()
#turnos disponibles   
lunes_disp = 4
martes_disp = 3

#agenda
l1 = ""; l2 = ""; l3 = ""; l4 = ""
m1 = ""; m2 = ""; m3 = ""

opcion = "" 

while opcion != "5":
    print ("--- MENU PRINCIPAL ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Ingrese una opcion(1,2,3,4 o 5): ")
    while opcion not in ["1","2","3","4","5"]:# validacion para solo tomar un numero del 1 al 5
        print("Error, debe ingresar una opcion 1-5")
        opcion = input("Ingrese una opcion(1,2,3,4 o 5): ")
    match opcion: # parametros del menu
        case "1":
            print("------Menu de reserva------")
            #Eleccion del dia
            elec_dia = input("Seleccione el día 1=Lunes o 2=Martes(Solo numero): ")
            while elec_dia not in ["1","2"]: #validacion
                print("Error, Ingrese solo 1 o 2 segun el día que desee")
                elec_dia = input("Seleccione el día 1=Lunes o 2=Martes(Solo numero): ")
            
            if elec_dia == "1":
                if lunes_disp == 0:
                    print("El día lunes se encuentra completo")
                else:
                    #Nombre del paciente
                    nomb_paciente = input("Ingrese el nombre del paciente: ").lower()
                    while not nomb_paciente.isalpha():#validacion
                        print("Error, Solo ingresar letras")
                        nomb_paciente = input("Ingrese el nombre del paciente: ").lower()
                    if nomb_paciente in [l1,l2,l3,l4]:
                        print("Error, el paciente ya tiene un turno agendado")
                    elif l1 == "":
                        l1 = nomb_paciente
                        lunes_disp -= 1
                        print("Turno agendado en cupo 1")
                    elif l2 == "":
                        l2 = nomb_paciente
                        lunes_disp -= 1
                        print("Turno agendado en cupo 2")
                    elif l3 == "":
                        l3 = nomb_paciente
                        lunes_disp-=1
                        print("Turno agendado en cupo 3")
                    elif l4 =="":
                        l4 = nomb_paciente
                        lunes_disp-=1
                        print("Turno agendado en cupo 4")
            elif elec_dia == "2":
                if martes_disp==0:
                    print("El día martes se encuentra completo")
                else:
                    #Nombre del paciente
                    nomb_paciente = input("Ingrese el nombre del paciente: ").lower()
                    while not nomb_paciente.isalpha():#validacion
                        print("Error, Solo ingresar letras")
                        nomb_paciente = input("Ingrese el nombre del paciente: ").lower()
                    if nomb_paciente in [m1,m2,m3]:
                        print("Error, el paciente ya tiene un turno agendado")
                    elif m1 =="":
                        m1 =nomb_paciente
                        martes_disp-=1
                        print("Turno agendado en cupo 1")
                    elif m2 == "":
                        m2=nomb_paciente
                        martes_disp-=1
                        print("Turno agendado en cupo 2")
                    elif m3 == "":
                        m3=nomb_paciente
                        martes_disp-=1
                        print("Turno agendado en cupo 3")
        case "2":
            print("------Menu cancelación turno------")
            elec_dia=input("Que día saco su turno(1=lunes,2=martes): ")
            while elec_dia not in ["1","2"]:
                print("Error, Solo debe ingresar 1 o 2")
                elec_dia=input("Que día saco su turno(1=lunes,2=martes): ")
            if elec_dia == "1":
                nomb_paciente = input("Ingrese el nombre del paciente: ").lower()
                while not nomb_paciente.isalpha():#validacion
                    print("Error, Solo ingresar letras")
                    nomb_paciente = input("Ingrese el nombre del paciente: ").lower()
                if nomb_paciente in [l1]:
                    l1=""
                    lunes_disp+=1
                    print("Turno cancelado")
                elif nomb_paciente in [l2]:
                    l2 = ""
                    lunes_disp+=1
                    print("Turno cancelado")
                elif nomb_paciente in [l3]:
                    l3=""
                    lunes_disp+=1
                    print("Turno cancelado")
                elif nomb_paciente in [l4]:
                    l4 = ""
                    lunes_disp+=1
                    print("Turno cancelado")
            elif elec_dia=="2":
                nomb_paciente = input("Ingrese el nombre del paciente: ").lower()
                while not nomb_paciente.isalpha():#validacion
                    print("Error, Solo ingresar letras")
                    nomb_paciente = input("Ingrese el nombre del paciente: ").lower()
                if nomb_paciente in [m1]:
                    m1=""
                    martes_disp+=1
                    print("Turno cancelado")
                if nomb_paciente in [m2]:
                    m2=""
                    martes_disp+=1
                    print("Turno cancelado")
                if nomb_paciente in [m3]:
                    m3=""
                    martes_disp+=1
                    print("Turno cancelado")
        case "3":
            print("------Agenda------")
            print("-------------------")
            print("Día Lunes")
            print(f"Turno 1: {l1} \nTurno 2: {l2} \nTurno 3: {l3} \nTurno 4: {l4}")
            print("-------------------")
            print("Día Martes")
            print(f"Turno 1: {m1} \nTurno 2: {m2} \nTurno 3: {m3} ")
        case "4":
            print("------Resumen------")
            print(f"Cantidad de turnos disponibles: \nLunes:{lunes_disp} \nMartes:{martes_disp} ")
            if lunes_disp > martes_disp:
                print("El día con mas turnos disponibles es el Lunes")
            elif lunes_disp < martes_disp:
                print("El día con mas turnos disponibles es el Martes")
            else:
                print("Ambos dias cuentan con la misma cantidad de turnos")
        case "5":
            print("Saliendo del sistema...")
#==============================================================================================================================================================            
#Ejecicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar= 0

nombre_agente = input("Ingrese su Nombre: ").lower()
while not nombre_agente.isalpha():
    print("El nombre ingresado es incorrecto. Ingresar solo letras")
    nombre_agente = input("Ingrese su Nombre: ").lower()
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:
    # REGLA DE BLOQUEO POR ALARMA
    if alarma and tiempo <= 3:
        print("\n--- ¡SISTEMA BLOQUEADO POR ALARMA! Has sido capturado ---")
        break
    print("----Estado----")
    print(f"La energia es de {energia} puntos")
    print(f"Tiempo restante {tiempo}")
    print(f"Cerraduras abiertas {cerraduras_abiertas}")
    print("------------------------------------------")
    print("----Menu del juego----")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    opcion = input("Que opcion elige(1,2 o 3): ")
    while opcion not in ["1","2","3"]:
        print("Opcion incorrecta, debe ingresar 1, 2 o 3")
        opcion = input("Que opcion elige(1,2 o 3): ")
    match opcion:
        case "1":
            energia -= 20
            tiempo -= 2
            racha_forzar+=1
            if racha_forzar==3:
                alarma=True
                print("Derrota, Se activo la alarma")
                break
            if energia < 40:
                numer = input("Elige 1 2 o 3 para intenar la accion: ")
                while numer not in ["1","2","3"]:
                    print("Error, ingrese 1, 2 o 3")
                    numer = input("Elige 1 2 o 3 para intenar la accion: ")
                if numer == "3":
                    alarma=True
                    print("Derrota... Activo la alarma")
                    break
                else:
                    cerraduras_abiertas +=1
                    print("Exelente!! logro abrir una cerradura")
            else:
                cerraduras_abiertas+=1
                print("Cerradura abierta limpiamente")
        case "2":
            print("Iniciando Hackeo...")
            energia -=10
            tiempo -=3
            racha_forzar=0
            for paso in range(1, 5): 
                porcentaje = paso * 25
                print(f"Hackeando... {porcentaje}%")
                codigo_parcial += "X" 
            print(f"Código actual: {codigo_parcial}")
            # Verificamos si el código llegó a 8 o más
            if len(codigo_parcial) >= 8:
                if cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print("¡SISTEMA HACKEADO! El código está completo y se abrió una cerradura.")
                    codigo_parcial = "" 
                else:
                    print("El código está listo, pero ya abriste todas las cerraduras.")
            else:
                faltan = 8 - len(codigo_parcial)
                print(f"Código insuficiente. Faltan {faltan} caracteres más para abrir una cerradura.")
        case "3":
            racha_forzar = 0
            tiempo -= 1
            if alarma == False:
                energia += 15
                if energia > 100:
                    energia = 100
                print(f"Has descansado. Energía: {energia}")
            else:
                energia -= 10 # Penalización por alarma
                print("La alarma no te deja descansar, pierdes energía.")
# --- CONDICIONES DE FIN DE JUEGO (FUERA DEL BUCLE) ---
print("\n=============================")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El agente {nombre_agente.upper()} abrió la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: Te quedaste sin recursos (energía o tiempo agotados).")
else:
    print("DERROTA: El sistema se bloqueó por la alarma.")
print("=============================")

#=====================================================================================================================================================
#Ejercicio 5
Nombre_jugador = input("Ingrese su nombre Gladiador: ")
while not Nombre_jugador.isalpha():
    print("Error. Solo se permitien letras")
    Nombre_jugador = input("Ingrese su nombre Gladiador: ")

vida_gladiador = 100
vida_enemigo = 100
posiones_vida = 3
daño_base_pesado = 15
daño_base_enemigo = 12
turno_gladiador = True

while vida_gladiador > 0 and vida_enemigo > 0:
    while turno_gladiador == True:
        print(f"-------Que inicie el combate {Nombre_jugador}-------")
        print("----------------------------------------------")
        print(f"Vida de {Nombre_jugador}= {vida_gladiador} ")
        print(f"Vida del enemigo= {vida_enemigo} ")
        print(f"Posiones de vida restantes= {posiones_vida}")
        print("----------------------------------------------")
        print("1. Ataque pesado")
        print("2. Rafaga veloz")
        print("3. Cura")
        opcion = input("Ingrese su movimiento(1,2 o 3): ")
        while not opcion.isdigit() or opcion not in ["1","2","3"]:
            print("Error, debe ingresar 1, 2 o 3")
            opcion = input("Ingrese su movimiento(1,2 o 3): ")
        match opcion:
            case "1":
                print("---Ataque pesado---")
                if vida_enemigo < 20:
                    golpe_critico = daño_base_pesado * 1.5
                    vida_enemigo -= golpe_critico
                    print(f"¡Atacaste al enemigo por {golpe_critico} de daño!")
                    turno_gladiador=False
                else:
                    vida_enemigo-=daño_base_pesado
                    print(f"Golpeaste por {daño_base_pesado} puntos de daño")
                    turno_gladiador=False
            case"2":
                print("---Rafaga veloz---")
                for cont in range(3):
                    vida_enemigo-=5
                    print("Golpe conectado por 5 de daño")
                    turno_gladiador=False
            case "3":
                print("---Curación---")
                if posiones_vida > 0:
                    vida_gladiador+=30
                    if vida_gladiador>100:
                        vida_gladiador=100
                        print("Estas al maximo de vida")
                    posiones_vida-=1
                    print("Tu vida aumenta en 30 puntos")
                    turno_gladiador=False
                else:
                    print("¡No te quedan posiones!")
                    turno_gladiador=False
    while turno_gladiador == False:
        vida_gladiador-=daño_base_enemigo
        print(f"¡El enemigo te ataco por {daño_base_enemigo} puntos de daño!")
        turno_gladiador=True

if vida_gladiador > 0:
    print(f"¡VICTORIA! {Nombre_jugador} ha ganado la batalla")
else:
    print("DERROTA. Has caido en combate")
