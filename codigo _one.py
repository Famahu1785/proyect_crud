
import os

def leer_archivo(archiv_not):
    try:
        with open(archiv_not, "r", encoding="utf-8") as archiv:  # Abrir el archivo con codificación UTF-8
            contenido = archiv.read()  # Leer el contenido del archivo
        return contenido
    except FileNotFoundError:  # Esta es una excepción por si el archivo no es encontrado
        return "El archivo no se encontró."
    except Exception as e:  # Se utiliza para capturar un error inesperado que como tal no está definido
        return f"Ocurrió un error: {e}"

def procesar_contenido(contenido):
    lineas = contenido.strip().split('\n')
    estudiantes = []

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
            i += 4

        estudiantes.append({
            'codigo_estudiante': codigo_estudiante,
            'nombre_estudiante': nombre_estudiante,
            'materias': materias
        })

    return estudiantes

if __name__ == '__main__':
    # Imprimir el directorio de trabajo actual
    print("Directorio de trabajo actual:", os.getcwd())

    archiv_not = "proyet_crud/not_ing_2.txt"
    contenido = leer_archivo(archiv_not)
    if contenido.startswith("El archivo no se encontró") or contenido.startswith("Ocurrió un error"):
        print(contenido)
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
