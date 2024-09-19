id = None
correo = None
password = None
rol = None

def set_sesion(sesion):
    global id
    global correo
    global password
    global rol

    id = sesion[0]
    correo = sesion[1]
    password = sesion[2]
    rol = sesion[3]

def get_sesion():
    return id, correo, password, rol

def get_correo():
    return correo

def get_rol():
    return rol

def clear_sesion():
    global id
    global correo
    global password
    global rol

    id = None
    correo = None
    password = None
    rol = None