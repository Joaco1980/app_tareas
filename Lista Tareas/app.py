from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def to_dict(self):
        return {
            'descripcion': self.descripcion,
            'completada': self.completada
        }

class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def marcar_tarea_completada(self, posicion):
        try:
            self.tareas[posicion].marcar_completada()
        except IndexError:
            pass

    def eliminar_tarea(self, posicion):
        try:
            self.tareas.pop(posicion)
        except IndexError:
            pass

    def obtener_tareas(self):
        return [tarea.to_dict() for tarea in self.tareas]

lista_de_tareas = ListaDeTareas()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': lista_de_tareas.obtener_tareas()})

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    lista_de_tareas.agregar_tarea(data['descripcion'])
    return '', 204

@app.route('/complete_task/<int:posicion>', methods=['POST'])
def complete_task(posicion):
    lista_de_tareas.marcar_tarea_completada(posicion)
    return '', 204

@app.route('/delete_task/<int:posicion>', methods=['POST'])
def delete_task(posicion):
    lista_de_tareas.eliminar_tarea(posicion)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
