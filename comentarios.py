import sys

sys.stdout.reconfigure(encoding='utf-8')

def mostrar_comentarios():
    print
    print("=== MANERAS DE COMENTAR EN PYTHON ===\n")

    # 1. Comentarios de una sola línea.
    # Se utiliza el símbolo de numeral (hash). Todo lo que esté a la derecha es ignorado.
    print("1. Comentarios de línea completa:")
    print("   Se usa '#'. El intérprete descarta todo lo que sigue en esa línea.\n")

    # 2. Comentarios en línea (inline comments).
    x = 5  # Esto es un comentario en línea. Según PEP 8, debe separarse del código por al menos dos espacios.
    print("2. Comentarios en línea (inline):")
    print("   Van en la misma línea que el código, introducidos por '#'. Útiles para aclaraciones breves.\n")

    # 3. Comentarios de múltiples líneas.
    # Python no tiene un delimitador específico para bloques de comentarios (como /* ... */ en C o C++).
    # La convención oficial y más eficiente es usar un '#' por cada línea.
    print("3. Comentarios multilínea (Bloques):")
    print("   Python no tiene sintaxis de bloque de comentarios. Se usa un '#' en cada línea consecutiva.\n")

    # 4. Docstrings (Cadenas de documentación).
    """
    Esto es un Docstring.
    Estrictamente hablando, esto NO es un comentario. Es un string de múltiples líneas.
    Si no se asigna a una variable, el recolector de basura lo descarta rápidamente, 
    pero sí consume tiempo de evaluación. 
    Se usa por convención (PEP 257) para documentar módulos, clases y funciones, 
    ya que se guarda en el atributo mágico __doc__.
    """
    print("4. Docstrings (Cadenas con triple comilla):")
    print("   Usan \"\"\" o '''. Técnicamente son literales de texto, no comentarios puros.")
    print("   Se utilizan para generar documentación automática (atributos __doc__).\n")

if __name__ == "__main__":

    mostrar_comentarios()