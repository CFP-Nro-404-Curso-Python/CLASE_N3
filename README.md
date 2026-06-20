# 🐍 Curso de Python

**Centro de Formación Profesional N° 404**  
**Alumno:** David Hernan Bravo  

---

## 📌 Descripción del Proyecto

Este repositorio contiene la resolución de una serie de ejercicios prácticos implementados en Python. El objetivo principal es evidenciar la evolución arquitectónica del código: partiendo de buenas prácticas de documentación, pasando por el paradigma procedural (funciones), hasta llegar a una refactorización completa utilizando Programación Orientada a Objetos (POO) y patrones de diseño básicos.

## 📂 Estructura de Archivos

| Archivo | Propósito Principal | Enfoque Técnico |
| :--- | :--- | :--- |
| `comentarios.py` | Explicar convenciones de documentación. | PEP 8, PEP 257, Docstrings. |
| `funciones.py` | Resolución procedural de ejercicios. | Control de flujo, `match/case`, validación de inputs. |
| `clases.py` | Refactorización de los ejercicios a POO. | Abstracción, Encapsulamiento, Dictionary Dispatch. |

---

## 🛠️ Análisis Técnico de los Módulos

### 1. `comentarios.py`
Un script ejecutable que imprime en consola una guía práctica sobre cómo documentar código de forma estandarizada en Python. Aborda los siguientes puntos:
* Comentarios de línea completa (uso de `#`).
* Comentarios en línea (separados por dos espacios según normas PEP 8).
* Simulación de bloques multilínea convencionales.
* Uso de Docstrings (`"""`) para la documentación automática de módulos y funciones (PEP 257 y atributo `__doc__`).

### 2. `funciones.py`
Implementa cinco ejercicios matemáticos y de lógica de negocio (mayoría de edad, división segura, paridad, evaluación fiscal y sistema de cobro tarifario) utilizando un enfoque **procedural puro**.

**Bases Teóricas: Funciones en Python**
En el paradigma procedural, la unidad básica de modularización es la función. 
* **Definición y Propósito:** Se declaran con la palabra reservada `def`. Su objetivo fundamental es cumplir con el principio DRY (*Don't Repeat Yourself*): encapsular una lógica específica para no reescribir código.
* **Comportamiento *Stateless*:** Las funciones son inherentemente sin estado. Toman datos de entrada (parámetros), los procesan y (opcionalmente) devuelven un resultado mediante `return`. Una vez que la función termina su ejecución, sus variables locales se destruyen en la memoria.
* **Acoplamiento de Datos:** En este enfoque, los datos y el comportamiento están separados. Si una función necesita un contexto persistente o configuraciones de dominio (como las tarifas del sistema), dependés de variables globales o tenés que pasarlas continuamente como argumentos, lo cual no escala bien en sistemas complejos.

**Características clave de la implementación en este módulo:**
* **Manejo de Excepciones:** Uso riguroso de bloques `try-except` (`ValueError`, `ZeroDivisionError`) integrados en bucles `while True` para evitar caídas del sistema ante inputs inválidos por parte del usuario.
* **Sanitización de Datos:** Aplicación del método `.strip()` en todas las entradas de texto.
* **Enrutamiento:** Implementación de un menú interactivo basado en **Pattern Matching** (`match / case`), aprovechando la sintaxis moderna para el control de flujo y reemplazando los anidados `if-elif`.

### 3. `clases.py`
Representa la evolución técnica del código. Los mismos cinco ejercicios se refactorizaron en clases independientes para demostrar las ventajas y la escalabilidad de la **Programación Orientada a Objetos (POO)**.

**Bases Teóricas: Clases y POO en Python**
Si las funciones separan el comportamiento de los datos, las clases los unen en una sola entidad lógica.
* **Plantilla vs. Instancia:** Una clase (declarada con `class`) es simplemente un plano teórico o molde. Cuando ejecutás ese molde, creás una instancia (un objeto) que ocupa un lugar real en la memoria de la máquina.
* **Atributos y Estado:** A diferencia de las funciones, los objetos tienen memoria persistente durante su ciclo de vida. Los atributos (variables internas prefijadas con `self`) mantienen el estado del objeto.
* **Métodos:** Son las acciones que el objeto puede realizar. Técnicamente son funciones, pero están limitadas al contexto (el *scope*) de la clase y operan sobre el estado interno de esa misma instancia.

**Mejoras arquitectónicas aplicadas en este módulo:**
* **Contratos mediante Abstracción (ABC):** Se implementó la clase base `OperacionBase` con el método abstracto `ejecutar()`. Esto fuerza el **Polimorfismo** (distintos objetos respondiendo a la misma orden a su manera) y obliga a cualquier nuevo módulo a respetar la misma interfaz estricta. Si creás una clase y no definís `ejecutar()`, Python te frena en seco y no compila.
* **Encapsulamiento del Dominio:** Las constantes de negocio (como `EDAD_MAYORIA` o `PRECIO_INFANTIL`) dejaron de ser variables globales de un script suelto. Ahora pertenecen al estado interno de cada clase, reduciendo la posibilidad de efectos secundarios (*side effects*) y evitando que otra parte del código las altere por error.
* **Dictionary Dispatch vs Match/Case:** Se eliminó la dependencia de estructuras condicionales rígidas en el menú principal. En su lugar, se utilizó un diccionario que mapea las opciones en formato string directamente a las referencias en memoria de las clases. Esto baja la complejidad algorítmica de búsqueda a O(1): no importa si tenés 5 o 5000 opciones, el tiempo de ruteo es constante.
* **Lazy Loading (Instanciación Diferida):** El sistema solo reserva memoria y crea el objeto de la clase correspondiente en el momento exacto en que el usuario selecciona una opción. Cuando la operación termina, el objeto pierde su referencia y el *Garbage Collector* libera la memoria RAM. Esto es eficiencia de recursos pura.

---

## 🚀 Ejecución

Para correr cualquiera de los scripts, abrí tu terminal de comandos, ubicate en el directorio del proyecto y ejecutá el archivo deseado con el intérprete de Python. 

**Requisito indispensable:** Asegurate de tener instalada la versión **Python 3.10 o superior** (necesaria para el correcto funcionamiento de las sentencias `match / case` en el script procedural).

**Comandos de terminal:**
* `python comentarios.py`
* `python funciones.py`
* `python clases.py`