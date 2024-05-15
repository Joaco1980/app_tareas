class Tarea:
    def __init__(self, descripcion):
        """
        Constructor de la clase Tarea. Inicializa la descripción y el estado de la tarea.
        """
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def __str__(self):
        """
        Devuelve una representación en cadena de la tarea, mostrando si está completada o pendiente.
        """
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"


class ListaDeTareas:
    def __init__(self):
        """
        Constructor de la clase ListaDeTareas. Inicializa una lista vacía de tareas.
        """
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """
        Agrega una nueva tarea a la lista de tareas pendientes.
        """
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{descripcion}' agregada.")

    def marcar_tarea_completada(self, posicion):
        """
        Marca una tarea como completada, dada su posición en la lista.
        Maneja excepciones si la posición no es válida.
        """
        try:
            self.tareas[posicion].marcar_completada()
            print(f"Tarea en posición {posicion} marcada como completada.")
        except IndexError:
            print("Error: Posición de tarea no válida.")

    def mostrar_tareas(self):
        """
        Imprime en pantalla todas las tareas pendientes, numeradas y mostrando su estado.
        """
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        """
        Elimina una tarea de la lista, dada su posición.
        Maneja excepciones si la posición no es válida.
        """
        try:
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        except IndexError:
            print("Error: Posición de tarea no válida.")


def main():
    lista_de_tareas = ListaDeTareas()

    while True:
        print("\nGestión de Tareas Pendientes")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_tarea_completada(posicion)
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        elif opcion == "3":
            lista_de_tareas.mostrar_tareas()
        elif opcion == "4":
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(posicion)
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
