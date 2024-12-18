import os
def print_stud(archiv_not):
    try:
        with open(archiv_not, "r", encoding="utf-8") as archiv:  # Abrir el archivo con codificación UTF-8
            contenido = archiv.read()  # Leer el contenido del archivo
        return contenido
    except FileNotFoundError:  # Esta es una excepción por si el archivo no es encontrado
        return "El archivo no se encontró."
    except Exception as e:  # Se utiliza para capturar un error inesperado que como tal no está definido
        return f"Ocurrió un error: {e}"

def procesar_contenido(contenido):
    lineas = contenido.strip().split('\n') # el split sirve para dividir  el contenido de la cadena
    estudiantes = [] # se crea una lista vacía para almacenar los estudiantes

    for linea in lineas:
        campos = linea.split(',')
        codigo_estudiante = campos[0].strip()
        nombre_estudiante = campos[1].strip()
        materias = []

        i = 2
        while i < len(campos):
            nombre_materia = campos[i].strip()
            codigo_materia = campos[i + 1].strip()
            nota1 = float(campos[i + 2].strip())
            creditos = int(campos[i + 3].strip())
            materias.append({
                'nombre_materia': nombre_materia,
                'codigo_materia': codigo_materia,
                'nota1': nota1,
                'creditos': creditos
            })
            i += 4    # Se incrementa el índice en 4 para pasar a la siguiente materia

        estudiantes.append({        
            'codigo_estudiante': codigo_estudiante,
            'nombre_estudiante': nombre_estudiante,
            'materias': materias
        })     # Se añade un diccionario con la información del estudiante a la lista de estudiantes

    return estudiantes

def create_student():
    pass

def get_coma():
    print("Función para obtener coma no implementada.")

def read_student():
    print("Función para leer estudiante no implementada.")

def update_student():
    print("Función para actualizar estudiante no implementada.")

def delete_student():
    print("Función para eliminar estudiante no implementada.")

def get_student():
    print("Función para obtener estudiante no implementada.")

def promedio_masalt():
    pass

def _message_welcome_student():
    print(""" WELCOME TO UNIVALLE:
          Qué desea realizar ?
          1. Print Student
          2. Create Student
          3. Read Student
          4. Update Student
          5. Delete Student
          6. promedio
          7. Exit
          """)

if __name__ == '__main__':
    _message_welcome_student()
    option = int(input("Enter your activity: "))
    if option == 1:
        archiv_not = "not_ing_2.txt"    # Nombre del archivo a leer
        contenido = print_stud(archiv_not) # Llamar a la función print_stud con el nombre del archivo
        if contenido.startswith("El archivo no se encontró") or contenido.startswith("Ocurrió un error"):   # Si el contenido empieza con "El archivo no se encontró" o "Ocurrió un error"
            print(contenido)   # Imprimir el contenido # el startwith es un metodo que se usa para verificar si una cadena comienza con un prefijo especifico
        else:
            estudiantes = procesar_contenido(contenido)
            for estudiante in estudiantes:
                print(f"Código del estudiante: {estudiante['codigo_estudiante']}")
                print(f"Nombre del estudiante: {estudiante['nombre_estudiante']}")
                for materia in estudiante['materias']:
                    print(f"  Materia: {materia['nombre_materia']}")
                    print(f"  Código de la materia: {materia['codigo_materia']}")
                    print(f"  Nota 1: {materia['nota1']}")
                    print(f"  Créditos: {materia['creditos']}")
                print()
    elif option == 2:
        create_student()
    elif option == 3:
        read_student()
    elif option == 4:
        update_student()
    elif option == 5:
        delete_student()
    elif option == 6:
        promedio_masalt()
    elif option == 7:
        print("Saliendo del programa.")
    else:
        print("Función seleccionada no disponible.")
