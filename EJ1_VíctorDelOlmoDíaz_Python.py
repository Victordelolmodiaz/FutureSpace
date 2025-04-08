# Ruta donde se guardará el archivo tareas.txt
archivo = r"E:\1DAM\FUTURE-SPACE\PYTHON\PRACTICA\tareas.txt"

# Cargar las tareas desde el archivo
def cargar_tareas():
    tareas = []
    try:
        with open(archivo, "r") as archivo:
            for linea in archivo:
                tarea = linea.strip()
                tareas.append(tarea)
    except FileNotFoundError:
        pass  
    return tareas

# Guardar las tareas en el archivo
def guardar_tareas(tareas):
    with open(archivo, "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

# Mostrar el menú de opciones
def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Agregar una tarea")
    print("2. Ver la lista de tareas")
    print("3. Marcar una tarea como completada")
    print("4. Eliminar una tarea")
    print("5. Salir")

# Agregar una nueva tarea
def agregar_tarea(tareas):
    tarea = input("Introduce la tarea que deseas agregar: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada con éxito.")

# Ver todas las tareas
def ver_tareas(tareas):
    if tareas:  
        print("\nLista de tareas:")
        for i in range(len(tareas)):  
            print(f"{i + 1}. {tareas[i]}")
    else:
        print("No tienes tareas pendientes.")

# Marcar una tarea como completada
def marcar_tarea_completada(tareas):
    if tareas:  
        ver_tareas(tareas)  
        try:
            tarea_completada = int(input("Selecciona el número de la tarea que deseas marcar como completada: "))
            tarea_seleccionada = tarea_completada - 1  
            if tarea_seleccionada >= 0:  
                tarea = tareas[tarea_seleccionada]
                tarea_actualizada = f"{tarea} (Completada)"  
                tareas[tarea_seleccionada] = tarea_actualizada  
                print(f"Tarea '{tarea}' marcada como completada.")
            else:
                print("Número de tarea no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    else:
        print("No tienes tareas para marcar como completadas.")

# Eliminar una tarea
def eliminar_tarea(tareas):
    if tareas:  
        ver_tareas(tareas)  
        try:
            tarea_eliminada = int(input("Selecciona el número de la tarea a eliminar: "))
            tarea_seleccionada = tarea_eliminada - 1 
            if tarea_seleccionada >= 0:  
                tarea = tareas[tarea_seleccionada]
                tareas[:] = [tarea for tarea in tareas if tarea != tarea] 
                print(f"Tarea '{tarea}' eliminada.")
            else:
                print("Número de tarea no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    else:
        print("No tienes tareas para eliminar.")

# Función principal
def EJ1_VíctorDelOlmoDíaz_Python():
    tareas = cargar_tareas()  

    while True:
        mostrar_menu()  
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)  
        elif opcion == "2":
            ver_tareas(tareas)  
        elif opcion == "3":
            marcar_tarea_completada(tareas)  
        elif opcion == "4":
            eliminar_tarea(tareas)  
        elif opcion == "5":
            guardar_tareas(tareas)  
            print("Tareas guardadas. ¡Hasta luego!")
            break  
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

# Llamada a la función principal
EJ1_VíctorDelOlmoDíaz_Python()
