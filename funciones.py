import sys

sys.stdout.reconfigure(encoding='utf-8')

'''
EJERCICIO N°1
-------------
Escribir un programa que pregunte al usuario su nombre y edad. Debe mostrar por pantalla si es mayor de edad o no.
'''
def verificar_mayoria_edad():
    '''
    Función principal que solicita nombre y edad al usuario,
    valida los tipos de datos y determina la mayoría de edad.
    '''
    print("\nIniciando verificación de edad...👶🏻🧑🏻 \n")

    # Solicitamos el nombre y usamos .strip() para eliminar espacios en blanco accidentales al inicio o final.
    nombre = input("\nIngresá tu nombre: ").strip()
    
    # Bucle infinito para forzar al usuario a ingresar un dato válido.
    # Esto evita que el sistema "rompa" (crashee) por un ValueError.
    while True:
        try:
            # Intentamos convertir la entrada del usuario a un entero (int).
            edad = int(input(f"\nHola {nombre}, ingresá tu edad: "))
            
            # Validación lógica: la edad no puede ser un número negativo.
            if edad < 0:
                print("\nError: La edad no puede ser negativa. Intentá de nuevo. ❌")
                continue # Vuelve al inicio del bucle while.

            elif edad > 120:
                print("\nNo podés ser más viejo que Matusalén. Poné una edad real. 🧐")
                continue
                
            # Si la conversión y la validación lógica son exitosas, salimos del bucle.
            break 
            
        except ValueError:
            # Si el usuario ingresa letras o símbolos, se captura el error y se le pide que intente de nuevo.
            print("\nError de tipo: Ingresá un número entero válido (ej: 25). ⚠️")

    # Estructura condicional para evaluar si es mayor o menor.
    if edad >= 18:
        print(f"\n¡Todo listo, {nombre}! Confirmado que sos mayor de edad. !Felicidades!🍻🔞")
    else:
        print(f"\nMirá, {nombre}, todavía sos menor de edad. Faltan un par de años. 👶🏻🍼")


'''
EJERCICIO N°2
-------------
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
'''
def calcular_division():
    '''
    Solicita dos números al usuario y calcula su división.
    Implementa manejo de excepciones para evitar caídas del sistema
    por ingresos de tipos inválidos o intentos de división por cero.
    '''
    print("\nIniciando módulo de división... ➗\n")
    
    # Bucle infinito para garantizar que el programa no termine hasta obtener un resultado válido.
    while True:
        try:
            # .strip() previene errores por espacios accidentales.
            numerador = float(input("\nIngresá el primer número (numerador): ").strip())
            divisor = float(input("\nIngresá el segundo número (divisor): ").strip())
            
            # Intento de operación. Si el divisor es 0, Python levanta un ZeroDivisionError.
            resultado = numerador / divisor
            
            # Si la operación es exitosa, se muestra el resultado y se sale del bucle.
            print(f"\n✅ Operación exitosa: El resultado de dividir {numerador} por {divisor} es {resultado}")
            break
            
        except ValueError:
            # Captura el error si la conversión a float() falla (ej: el usuario ingresó "hola").
            print("\n⚠️ Error de ingreso: Tenés que ingresar valores numéricos válidos. Probá de nuevo.")
            
        except ZeroDivisionError:
            # Captura la restricción matemática fundamental. 
            # Aislar esta excepción nos permite dar un mensaje claro y específico.
            print("\n❌ Error lógico: La división por cero no está definida. Ingresá un divisor distinto de cero.")


'''
EJERCICIO N°3
-------------
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
def determinar_paridad():
    '''
    Solicita un número entero al usuario y determina si es par o impar
    utilizando la operación módulo (%). Incluye validación de tipo de dato.
    '''
    print("\nIniciando análisis de paridad... 🔢\n")
    
    # Bucle de validación para garantizar la entrada correcta
    while True:
        try:
            # Solicitamos el dato, limpiamos espacios en blanco con .strip()
            # y forzamos la conversión a número entero (int), predeclarádolo.
            entrada = int(input("\nIngresá un número entero: ").strip())
            
            # Evaluación lógica: verificamos si el resto de la división por 2 es 0.
            if entrada % 2 == 0:
                print(f"\n✅ Análisis completo: El número {entrada} es PAR. 🔵")
            else:
                print(f"\n✅ Análisis completo: El número {entrada} es IMPAR. 🔴")
                
            # Salimos del bucle porque ya obtuvimos una respuesta válida
            break
            
        except ValueError:
            # Si el usuario ingresa letras o un número con decimales (ej: 4.5),
            # int() falla y capturamos el error para no romper el programa.
            print("\n⚠️ Error de formato: Tenés que ingresar exclusivamente un número entero (ej: 42 o -7). Probá de nuevo.")


'''
EJERCICIO N°4
-------------
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores 
a 1000000 mensuales. 
Escribir un programa que pregunte al usuario su nombre, edad y sus ingresos mensuales y muestre por pantalla si el 
usuario tiene que tributar o no.
'''
# Definición de constantes de negocio. Por convención en Python, las constantes se escriben en MAYÚSCULAS.
# En un sistema real, estos datos se consumirían de una API, base de datos o archivo de configuración (.env).
EDAD_MINIMA_TRIBUTARIA = 16
INGRESO_MINIMO_TRIBUTARIO = 1000000.0

def evaluar_tributacion():
    '''
    Solicita datos personales y financieros al usuario para determinar
    si cumple con los requisitos legales para tributar el impuesto.
    '''
    print("\nIniciando módulo de evaluación fiscal... 🏛️\n")
    
    # Obtenemos el nombre y lo sanitizamos eliminando espacios en blanco.
    nombre = input("\nIngresá tu nombre: ").strip()
    
    # Bucle de validación para garantizar la integridad de los datos de entrada.
    while True:
        try:
            # La edad es una variable discreta, usamos int().
            edad = int(input(f"\nPerfecto {nombre}, ingresá tu edad: ").strip())

            if edad > 120:
                print("\nNo podés ser más viejo que Matusalén. Poné una edad real. 🧐")
                continue
            
            # Los ingresos son una variable continua, usamos float() para admitir centavos.
            ingresos = float(input("\nAhora ingresá tus ingresos mensuales en pesos: ").strip())
            
            # Validación de consistencia de negocio: ni la edad ni los ingresos deberían ser negativos.
            if edad < 0 or ingresos < 0:
                print("\n⚠️ Error de lógica: La edad y los ingresos no pueden ser números negativos. Intentá de nuevo.")
                continue # Reiniciamos el ciclo de preguntas.
                
            # Si los datos son consistentes, rompemos el bucle.
            break
            
        except ValueError:
            # Captura de error de tipado si el usuario ingresa texto en lugar de números.
            print("\n❌ Error de formato: Asegurate de ingresar la edad como número entero y los ingresos como número decimal (ej: 1250000.50).")

    # Evaluación lógica condicional
    # Usamos el operador lógico 'and' ya que se deben cumplir AMBAS condiciones obligatoriamente.
    if edad > EDAD_MINIMA_TRIBUTARIA and ingresos >= INGRESO_MINIMO_TRIBUTARIO:
        print(f"\n📋 Resultado fiscal: {nombre}, dadas tus condiciones actuales, TENÉS que tributar. 💸⚖️")
    else:
        print(f"\n📋 Resultado fiscal: {nombre}, en este momento NO te corresponde tributar. 🛡️📉")


'''
EJERCICIO N°5
-------------
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular 
de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al 
usuario nombre y edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede 
entrar gratis, si tiene entre 4 y 18 años debe pagar u$s 5 y si es mayor de 18 años, u$s 10
'''
# Constantes del dominio del negocio. 
# Centralizar estos valores acá permite que una actualización de tarifas se haga en un solo lugar 
# y no buscando a lo largo de todo el código.
EDAD_LIMITE_INFANTIL = 4
EDAD_LIMITE_ADOLESCENTE = 18

PRECIO_INFANTIL = 0
PRECIO_ADOLESCENTE = 5
PRECIO_ADULTO = 10

def calcular_precio_entrada():
    '''
    Sistema de cálculo tarifario para sala de juegos.
    Solicita datos, valida tipos y determina el cobro exacto.
    '''
    print("\nIniciando sistema de facturación de sala de juegos... 🕹️\n")
    
    # Capturamos el nombre y sanitizamos el texto.
    nombre = input("\nIngresá el nombre del cliente: ").strip()
    
    # Bucle de validación para garantizar la integridad del dato etario (edad).
    while True:
        try:
            # Solicitamos la edad forzando un tipo de dato entero.
            edad = int(input(f"\nIngresá la edad de {nombre}: ").strip())
            
            # Validación de dominio: bloqueamos edades ilógicas.
            if edad < 0:
                print("\n⚠️ Error lógico: La edad no puede ser un número negativo. Corregí el dato.")
                continue # Obliga a reiniciar el bucle
                
            break # El dato es válido, cortamos el bucle
            
        except ValueError:
            print("\n❌ Error de tipo: Tenés que ingresar la edad como un número entero (ej: 8).")

    # Evaluación de la lógica de negocio usando estructuras mutuamente excluyentes (if-elif-else).
    if edad < EDAD_LIMITE_INFANTIL:
        # Menores de 4 años (0, 1, 2, 3).
        precio = PRECIO_INFANTIL
        categoria = "Infantil (Gratis) 👶🏻"
        
    elif edad <= EDAD_LIMITE_ADOLESCENTE:
        # Entre 4 y 18 años inclusive. 
        # Python solo llega a esta línea si la condición anterior fue falsa (es decir, ya sabe que edad >= 4).
        precio = PRECIO_ADOLESCENTE
        categoria = "Menores/Adolescentes 👦🏻👧🏻"
        
    else:
        # Cualquier edad mayor a 18 (19, 20...).
        precio = PRECIO_ADULTO
        categoria = "Adultos 👨🏻👩🏼"

    # Salida por pantalla formateada.
    print("\n" + "-" * 40)
    print(" 🎟️ TICKET DE INGRESO ")
    print("-" * 40 + "\n")
    print(f"👤 Cliente: {nombre}")
    print(f"🎂 Edad: {edad} años")
    print(f"🏷️ Categoría: {categoria}")
    print(f"💵 Total a cobrar: u$s {precio}")
    print("\n" + "-" * 40)


# Menú para mostrar en consola y ejecutar cada ejercicio de manera ordenada.
def menu():
    '''
    Despliega el menú interactivo, captura la carpeta del usuario y rutea la ejecución hacia la función seleccionada.
    '''
    while True:
        print("\n" + "=" * 32)
        print(" 🛠️  MENÚ PRINCIPAL (Funciones) ")
        print("=" * 32 + "\n")
        print("1. Verificar mayoría de edad")
        print("2. Calcular división")
        print("3. Determinar paridad")
        print("4. Evaluar tributación")
        print("5. Calcular precio de entrada")
        print("0. Salir del sistema")
        print("=" * 32 + "\n")

        opcion = input("Ingresá la opción deseada: ").strip()

        # Inicio del bloque de Coincidencia de Patrones Estructurales.
        # Evalúa la variable 'opcion' (que es un string, porque input() siempre devuelve string).
        match opcion:

            # Comprueba si el valor de 'opcion' es exactamente igual al string '1'.
            # Si es cierto, ejecuta verificar_mayoria_edad() y salta directamente al final del bloque match.
            case "1":
                verificar_mayoria_edad()
            
            # Repite la lógica de igualdad simple para los casos 2, 3, 4 y 5.
            case "2":
                calcular_division()
            case "3":
                determinar_paridad()
            case "4":
                evaluar_tributacion()
            case "5":
                calcular_precio_entrada()

            # Caso de salida del sistema.
            case "0":
                print("\n Saliendo del sistema. Hasta luego.👋🏻")
                sys.exit(0)
            
            # 'case _' es el patrón comodín: Es el equivalente directo al 'default' de C++.
            # Si el usuario ingresó 'A', '6', o cualquier cosa que no esté en los 'case' de arriba,
            # el flujo cae acá, previniendo que el programa falle silenciosamente.
            case _:
                print("\n❌ Error: Opción inválida. Ingresá un número del 0 al 5.")

# Punto de entrada del script: Buena práctica para evitar que el código se ejecute automáticamente si se 
# importa desde otro módulo.
if __name__ == "__main__":
    
    menu()