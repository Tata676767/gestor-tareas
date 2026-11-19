tareas =[]

def agregar_tareas(titulo):
    if not titulo.strip():
        raise ValueError("titulo no puede estar vacio")
    tareas.append(titulo.strip())

def eliminar_tareas(indice):
def listar_tareas():
    return tareas
