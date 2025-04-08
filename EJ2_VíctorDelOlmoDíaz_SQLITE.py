import sqlite3

# Ruta de la base de datos
ruta_db = r"E:\1DAM\FUTURE-SPACE\SQLITE\tareas.db"

# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

# Crear las tablas si no existen
cursor.execute("""
CREATE TABLE IF NOT EXISTS persona (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS lugar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarea TEXT NOT NULL,
    completada TEXT NOT NULL,
    persona_id INTEGER,
    lugar_id INTEGER,
    FOREIGN KEY (persona_id) REFERENCES persona(id),
    FOREIGN KEY (lugar_id) REFERENCES lugar(id)
)
""")
conexion.commit()

# Función para cargar las tareas desde la base de datos
def cargar_tareas():
    cursor.execute("""
        SELECT t.id, t.tarea, t.completada, p.nombre, l.nombre 
        FROM tareas t
        LEFT JOIN persona p ON t.persona_id = p.id
        LEFT JOIN lugar l ON t.lugar_id = l.id
    """)
    filas = cursor.fetchall()
    
    tareas = []
    for fila in filas:
        estado = fila[2]  # Estado de la tarea
        persona = fila[3] if fila[3] else "Desconocido"
        lugar = fila[4] if fila[4] else "Desconocido"
        tareas.append(f"{fila[0]}. {fila[1]} - {estado} (Persona: {persona}, Lugar: {lugar})")
    
    return tareas

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Agregar una tarea")
    print("2. Ver la lista de tareas")
    print("3. Marcar una tarea como completada")
    print("4. Eliminar una tarea")
    print("5. Salir")

# Función para agregar una nueva tarea con persona y lugar
def agregar_tarea():
    tarea = input("Introduce la tarea: ")
    persona = input("¿Quién la hará?: ")
    lugar = input("¿Dónde se realizará?: ")

    # Insertar persona si no existe
    cursor.execute("SELECT id FROM persona WHERE nombre = ?", (persona,))
    persona_id = cursor.fetchone()
    if not persona_id:
        cursor.execute("INSERT INTO persona (nombre) VALUES (?)", (persona,))
        persona_id = cursor.lastrowid
    else:
        persona_id = persona_id[0]

    # Insertar lugar si no existe
    cursor.execute("SELECT id FROM lugar WHERE nombre = ?", (lugar,))
    lugar_id = cursor.fetchone()
    if not lugar_id:
        cursor.execute("INSERT INTO lugar (nombre) VALUES (?)", (lugar,))
        lugar_id = cursor.lastrowid
    else:
        lugar_id = lugar_id[0]

    # Insertar tarea
    cursor.execute("""
        INSERT INTO tareas (tarea, completada, persona_id, lugar_id)
        VALUES (?, ?, ?, ?)
    """, (tarea, "Pendiente", persona_id, lugar_id))
    
    conexion.commit()
    print(f"Tarea '{tarea}' agregada con éxito.")

# Función para ver todas las tareas
def ver_tareas():
    tareas = cargar_tareas()
    if tareas:
        print("\nLista de tareas:")
        for tarea in tareas:
            print(tarea)
    else:
        print("No tienes tareas registradas.")

# Función para marcar una tarea como completada
def marcar_tarea_completada():
    ver_tareas()
    try:
        tarea_completada = int(input("Selecciona el número de la tarea a completar: "))
        cursor.execute("UPDATE tareas SET completada = ? WHERE id = ?", ("Completada", tarea_completada))
        conexion.commit()
        print(f"Tarea {tarea_completada} marcada como completada.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
    except sqlite3.Error:
        print("Error al marcar la tarea como completada.")

# Función para eliminar una tarea
def eliminar_tarea():
    ver_tareas()
    try:
        tarea_eliminada = int(input("Selecciona el número de la tarea a eliminar: "))
        cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_eliminada,))
        conexion.commit()
        print(f"Tarea {tarea_eliminada} eliminada.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
    except sqlite3.Error:
        print("Error al eliminar la tarea.")

# Función principal
def EJ2_VíctorDelOlmoDíaz_SQL():
    while True:
        mostrar_menu()  
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            marcar_tarea_completada()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

# Llamada directa a la función principal
EJ2_VíctorDelOlmoDíaz_SQL()

# Cerrar la conexión
conexion.close()
