from utils.conexion import conexionDataBase

def agregarUsuario(correo, password, rol):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Usuarios (Correo, Password, Rol) VALUES (%s, %s, %s)"
    cursor.execute(consulta, (correo, password, rol))
    conexion.commit()
    cursor.close()
    conexion.close()

    # Sacar el ID del usuario recien creado
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Usuario FROM Usuarios WHERE Correo = %s"
    cursor.execute(consulta, (correo,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    return resultado[0]

def agregarDoctor(nombre, apellido, telefono, id_especialidad, id_usuario):
    # Buscar el ID de la especialidad
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Especialidad FROM Especialidades WHERE Especialidad LIKE %s"
    cursor.execute(consulta, (id_especialidad,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    especialidad = resultado[0]
    print(especialidad)
    
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Doctores (Nombre, Apellido, Telefono, ID_EspecialidadID_Usuario) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, apellido, telefono, especialidad, id_usuario))
    conexion.commit()
    cursor.close()
    conexion.close()

def agregarPaciente(nombre, apellido, fecha_nacimiento, sexo, telefono, id_direccion, id_usuario):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Pacientes (Nombre, Apellido, Fecha_Nacimiento, Sexo, Telefono, ID_Direccion, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, apellido, fecha_nacimiento, sexo, telefono, id_direccion, id_usuario))
    conexion.commit()
    cursor.close()
    conexion.close()

def agregarDomicilioDoctor(calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Domicilio_doctores (Calle, Numero_Domicilio, Codigo_Postal, Colonia, Ciudad, Estado, Pais) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais))
    conexion.commit()
    cursor.close()
    conexion.close()

def agregarDomicilioPaciente(calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Domicilio_pacientes (Calle, Numero_Domicilio, Codigo_Postal, Colonia, Ciudad, Estado, Pais) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais))
    conexion.commit()
    cursor.close()
    conexion.close()

    # Sacar el ID de la direccion recien creada
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Direccion FROM Domicilio_pacientes WHERE Calle = %s AND Numero_Domicilio = %s"
    cursor.execute(consulta, (calle, numero_domicilio))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    return resultado[0]