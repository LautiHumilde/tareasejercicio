import firebase_admin
from firebase_admin import credentials, db

# Inicializar la app de Firebase
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tareas-de-casa-47d70-default-rtdb.firebaseio.com'
})

# Referencia a la base de datos en Firebase
ref = db.reference('/archivos')

def tarea(tarea):
    # Agregar tarea a la base de datos de Firebase
    new_task_ref = ref.push()
    new_task_ref.set({
        'descripcion': tarea
    })
    return new_task_ref.key

def vertarea():
    # Obtener todas las tareas de la base de datos de Firebase
    tasks = ref.get()
    if tasks:
        for task_key, task_value in tasks.items():
            print(f"ID: {task_key}, Descripción: {task_value['descripcion']}")
    else:
        print("No hay tareas.")

def editartarea(identificador, nuevadescri):
    # Actualizar la descripción de una tarea en la base de datos de Firebase
    ref.child(identificador).update({
        'descripcion': nuevadescri
    })

def borrartarea(identificador):
    # Eliminar una tarea de la base de datos de Firebase
    ref.child(identificador).delete()

def main():
    while True:
        print("\nOpciones:")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opciones = input("\nSeleccione una opción: ")

        if opciones == "1":
            print("\nTareas:")
            vertarea()
            input("\nPulsa enter para volver al menú de opciones.")
        elif opciones == "2":
            descripcion = input("\nIngrese la tarea: ")
            tarea_agregada = tarea(descripcion)
            print(f"Tarea agregada exitosamente. ID: {tarea_agregada}")
        elif opciones == "3":
            identificador = input("\nIngrese el ID de la tarea que desea editar: ")
            nuevadescri = input("Ingrese la nueva descripción para la tarea: ")
            editartarea(identificador, nuevadescri)
            print("Tarea editada exitosamente.")
        elif opciones == "4":
            identificador = input("\nIngrese el ID de la tarea que desea eliminar: ")
            borrartarea(identificador)
            print("Tarea eliminada exitosamente.")
        elif opciones == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

main()
