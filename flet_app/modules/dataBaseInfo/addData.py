from utils.conexion import conexionDataBase

def agregarUsuario(correo, password, rol):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Usuarios (Correo, Password, Rol) VALUES (%s, %s, %s)"
    cursor.execute(consulta, (correo, password, rol))
    conexion.commit()

def agregarDoctor(nombre, apellido, telefono, especialidad):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Doctores (Nombre, Apellido, Telefono, Especialidad) VALUES (%s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, apellido, telefono, especialidad))
    conexion.commit()

def agregarPaciente(nombre, apellido, fecha_nacimiento, sexo, telefono, id_direccion, id_usuario):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Pacientes (Nombre, Apellido, Fecha_Nacimiento, Sexo, Telefono, ID_Direccion, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, apellido, fecha_nacimiento, sexo, telefono, id_direccion, id_usuario))
    conexion.commit()

def agregarDomicilioDoctor(calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Direcciones (Calle, Numero_Domicilio, Codigo_Postal, Colonia, Ciudad, Estado, Pais) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais))
    conexion.commit()

def agregarDomicilioPaciente(calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Direcciones (Calle, Numero_Domicilio, Codigo_Postal, Colonia, Ciudad, Estado, Pais) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais))
    conexion.commit()