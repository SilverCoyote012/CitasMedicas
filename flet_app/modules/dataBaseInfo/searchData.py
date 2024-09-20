from ...utils.conexion import conexionDataBase

#Buscar todas las especialidades
def buscarEspecialidades():
    try:
        conexion = conexionDataBase()
        cursor = conexion.cursor()
        consulta = "SELECT * FROM Especialidades"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print("Error: ", e)