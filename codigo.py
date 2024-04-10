import sqlite3

def conexion(archivo):
    conn = None
    try:
        conn = sqlite3.connect(archivo)
        return conn
    except sqlite3.Error as e:
        print(e)

def tabla(conn):
    sql = ''' CREATE TABLE IF NOT EXISTS datos (
                id INTEGER PRIMARY KEY,
                descripcion TEXT
            ); '''
    cur = conn.cursor()
    cur.execute(sql)

def tarea(conn, tarea):
    sql = ''' INSERT INTO datos(descripcion)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, tarea)
    conn.commit()
    return cur.lastrowid

def vertarea(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM datos")
    fila = cur.fetchall()
    for fila in fila:
        print(fila)

def editartarea(conn, identificador, nuevadescri):
    sql = ''' UPDATE datos
              SET descripcion = ?
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (nuevadescri, identificador))
    conn.commit()

def borrartarea(conn, identificador):
    sql = ''' DELETE FROM datos WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (identificador,))
    conn.commit()

def main():
    archivo = "tareas.db"
    conn = conexion(archivo)
    with conn:
        tabla(conn)
        while True:
            print("\nOpciones:")
            print("1. Ver tareas")
            print("2. Agregar tarea")
            print("3. Editar tarea")
            print("4. Eliminar tarea")
            print("5. Salir")
            pciones = input("Seleccione una opción: ")

            if pciones == "1":
                print("\nTareas:")
                vertarea(conn)
            elif pciones == "2":
                descripcion = input("\nIngrese la tarea: ")
                tarea_ingresada = (descripcion,)
                tarea(conn, tarea_ingresada)
                print("Tarea agregada exitosamente.")
            elif pciones == "3":
                identificador = input("\nIngrese el ID de la tarea que desea editar: ")
                nuevadescri = input("Ingrese la nueva descripción para la tarea: ")
                editartarea(conn, identificador, nuevadescri)
                print("Tarea editada exitosamente.")
            elif pciones == "4":
                identificador = input("\nIngrese el ID de la tarea que desea eliminar: ")
                borrartarea(conn, identificador)
                print("Tarea eliminada exitosamente.")
            elif pciones == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
