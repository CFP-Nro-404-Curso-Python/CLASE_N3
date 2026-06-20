import sys
from abc import ABC, abstractmethod

sys.stdout.reconfigure(encoding='utf-8')

# ===================================================================
#  1. EL CONTRATO / INTERFAZ (Inviable en paradigma procedural puro)
# ===================================================================
class OperacionBase(ABC):
    """
    DIFERENCIA CLAVE: Polimorfismo y Contratos.
    En el enfoque funcional, no hay forma nativa de obligar a que 5 funciones distintas
    tengan el mismo nombre o sigan la misma estructura. 
    Acá, mediante Abstracción (ABC), creamos un molde estricto. Cualquier módulo nuevo 
    ESTÁ OBLIGADO a implementar 'ejecutar()'. Si te olvidás, el programa no corre.
    """
    @abstractmethod
    def ejecutar(self):
        pass

# ==============================================================================
# 2. ENCAPSULAMIENTO DEL DOMINIO (En funciones, dependés de variables globales)
# ==============================================================================

'''
EJERCICIO N°1
-------------
Escribir un programa que pregunte al usuario su nombre y edad. Debe mostrar por pantalla si es mayor de edad o no.
'''
class VerificarMayoriaEdad(OperacionBase):
    """
    DIFERENCIA CLAVE: Estado y Ámbito (Scope).
    Las funciones son "stateless" (sin estado propio). Si necesitan configurar algo, 
    usás constantes globales o se las pasás por parámetro.
    Acá, 'EDAD_MAYORIA' está encapsulada dentro de la clase. Modificar este valor 
    solo afecta a este objeto, reduciendo el riesgo de efectos secundarios en el script.
    """
    EDAD_MAYORIA = 18

    def ejecutar(self):
        print("\nIniciando verificación de edad...👶🏻🧑🏻 \n")

        nombre = input("\nIngresá tu nombre: ").strip()
        
        while True:
            try:
                edad = int(input(f"\nHola {nombre}, ingresá tu edad: "))
                
                if edad < 0:
                    print("\nError: La edad no puede ser negativa. Intentá de nuevo. ❌")
                    continue

                elif edad > 120:
                    print("\nNo podés ser más viejo que Matusalén. Poné una edad real. 🧐")
                    continue
                    
                break 
                
            except ValueError:
                print("\nError de tipo: Ingresá un número entero válido (ej: 25). ⚠️")

        # Usamos 'self.EDAD_MAYORIA' porque el dato le pertenece a la estructura del objeto.
        if edad >= self.EDAD_MAYORIA:
            print(f"\n¡Todo listo, {nombre}! Confirmado que sos mayor de edad. !Felicidades!🍻🔞")
        else:
            print(f"\nMirá, {nombre}, todavía sos menor de edad. Faltan un par de años. 👶🏻🍼")


'''
EJERCICIO N°2
-------------
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
'''
class CalcularDivision(OperacionBase):
    def ejecutar(self):
        print("\nIniciando módulo de división... ➗\n")
        
        while True:
            try:
                numerador = float(input("\nIngresá el primer número (numerador): ").strip())
                divisor = float(input("\nIngresá el segundo número (divisor): ").strip())
                
                resultado = numerador / divisor
                print(f"\n✅ Operación exitosa: El resultado de dividir {numerador} por {divisor} es {resultado}")
                break
                
            except ValueError:
                print("\n⚠️ Error de ingreso: Tenés que ingresar valores numéricos válidos. Probá de nuevo.")
            except ZeroDivisionError:
                print("\n❌ Error lógico: La división por cero no está definida. Ingresá un divisor distinto de cero.")


'''
EJERCICIO N°3
-------------
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
class DeterminarParidad(OperacionBase):
    def ejecutar(self):
        print("\nIniciando análisis de paridad... 🔢\n")
        
        while True:
            try:
                entrada = int(input("\nIngresá un número entero: ").strip())
                if entrada % 2 == 0:
                    print(f"\n✅ Análisis completo: El número {entrada} es PAR. 🔵")
                else:
                    print(f"\n✅ Análisis completo: El número {entrada} es IMPAR. 🔴")
                break
            except ValueError:
                print("\n⚠️ Error de formato: Tenés que ingresar exclusivamente un número entero (ej: 42 o -7). Probá de nuevo.")


'''
EJERCICIO N°4
-------------
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores 
a 1000000 mensuales. 
Escribir un programa que pregunte al usuario su nombre, edad y sus ingresos mensuales y muestre por pantalla si el 
usuario tiene que tributar o no.
'''
class EvaluarTributacion(OperacionBase):
    # Los parámetros fiscales quedan confinados a la gestión de esta clase.
    EDAD_MINIMA_TRIBUTARIA = 16
    INGRESO_MINIMO_TRIBUTARIO = 1000000.0

    def ejecutar(self):
        print("\nIniciando módulo de evaluación fiscal... 🏛️\n")
        nombre = input("\nIngresá tu nombre: ").strip()
        
        while True:
            try:
                edad = int(input(f"\nPerfecto {nombre}, ingresá tu edad: ").strip())
                if edad > 120:
                    print("\nNo podés ser más viejo que Matusalén. Poné una edad real. 🧐")
                    continue
                
                ingresos = float(input("\nAhora ingresá tus ingresos mensuales en pesos: ").strip())
                
                if edad < 0 or ingresos < 0:
                    print("\n⚠️ Error de lógica: La edad y los ingresos no pueden ser números negativos. Intentá de nuevo.")
                    continue
                break
            except ValueError:
                print("\n❌ Error de formato: Asegurate de ingresar la edad como número entero y los ingresos como número decimal (ej: 1250000.50).")

        if edad > self.EDAD_MINIMA_TRIBUTARIA and ingresos >= self.INGRESO_MINIMO_TRIBUTARIO:
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
class CalcularPrecioEntrada(OperacionBase):
    # Estructura interna de datos tarifarios. Ninguna otra clase puede alterarlos por accidente.
    EDAD_LIMITE_INFANTIL = 4
    EDAD_LIMITE_ADOLESCENTE = 18
    PRECIO_INFANTIL = 0
    PRECIO_ADOLESCENTE = 5
    PRECIO_ADULTO = 10

    def ejecutar(self):
        print("\nIniciando sistema de facturación de sala de juegos... 🕹️\n")
        nombre = input("\nIngresá el nombre del cliente: ").strip()
        
        while True:
            try:
                edad = int(input(f"\nIngresá la edad de {nombre}: ").strip())
                if edad < 0:
                    print("\n⚠️ Error lógico: La edad no puede ser un número negativo. Corregí el dato.")
                    continue
                break
            except ValueError:
                print("\n❌ Error de tipo: Tenés que ingresar la edad como un número entero (ej: 8).")

        if edad < self.EDAD_LIMITE_INFANTIL:
            precio = self.PRECIO_INFANTIL
            categoria = "Infantil (Gratis) 👶🏻"
        elif edad <= self.EDAD_LIMITE_ADOLESCENTE:
            precio = self.PRECIO_ADOLESCENTE
            categoria = "Menores/Adolescentes 👦🏻👧🏻"
        else:
            precio = self.PRECIO_ADULTO
            categoria = "Adultos 👨🏻👩🏼"

        print("\n" + "-" * 40)
        print(" 🎟️ TICKET DE INGRESO ")
        print("-" * 40 + "\n")
        print(f"👤 Cliente: {nombre}")
        print(f"🎂 Edad: {edad} años")
        print(f"🏷️ Categoría: {categoria}")
        print(f"💵 Total a cobrar: u$s {precio}")
        print("\n" + "-" * 40)


# ================================================================================
# 3. CONTROL DE FLUJO Y DESPACHO (Acá se rompe la dependencia del 'match/switch')
# ================================================================================
def menu():
    """
    DIFERENCIA CLAVE: Despacho dinámico vs Estructuras Condicionales rígidas.
    
    - Enfoque Funcional: Usaba un 'match opcion:' con 5 bloques 'case'. Si agregabas
      la función 6, tenías que romper el menú para meter otro 'case'. Alto acoplamiento.
      
    - Enfoque POO (Dictionary Dispatch): El diccionario mapea strings directamente
      a las referencias de las CLASES (Ojo: no a instancias, sino al plano de la clase).
      El menú se vuelve agnóstico: no sabe qué hace cada opción, solo sabe mapear.
    """
    opciones = {
        "1": VerificarMayoriaEdad,
        "2": CalcularDivision,
        "3": DeterminarParidad,
        "4": EvaluarTributacion,
        "5": CalcularPrecioEntrada
    }

    while True:
        print("\n" + "=" * 30)
        print(" 🛠️  MENÚ PRINCIPAL (POO) ")
        print("=" * 30 + "\n")
        print("1. Verificar mayoría de edad")
        print("2. Calcular división")
        print("3. Determinar paridad")
        print("4. Evaluar tributación")
        print("5. Calcular precio de entrada")
        print("0. Salir del sistema")
        print("=" * 30 + "\n")

        seleccion = input("Ingresá la opción deseada: ").strip()

        if seleccion == "0":
            print("\n Saliendo del sistema. Hasta luego.👋🏻")
            sys.exit(0)

        # Buscamos la clase. Complejidad algorítmica constante: O(1). No requiere iterar ni evaluar condiciones.
        ClaseOperacion = opciones.get(seleccion)

        if ClaseOperacion:
            """
            DIFERENCIA CLAVE: Gestión de Memoria (Lazy Loading / Instanciación diferida).
            Si usáramos funciones globales complejas o instanciáramos todo al inicio, 
            cargaríamos la memoria RAM con procesos que quizás el usuario jamás elija.
            
            Acá, la línea 'ClaseOperacion()' reserva el espacio en memoria para el objeto 
            RECIÉN cuando el usuario presiona el número. Al terminar el método 'ejecutar()',
            el objeto pierde su referencia y el Garbage Collector de Python lo barre de la RAM.
            Efficiente, limpio y escalable.
            """
            instancia = ClaseOperacion() # Instanciación dinámica
            instancia.ejecutar()         # Llamada polimórfica al contrato base
        else:
            print("\n❌ Error: Opción inválida. Ingresá un número del 0 al 5.")


if __name__ == "__main__":
    
    menu()