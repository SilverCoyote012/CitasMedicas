sesion_actual = None
correo = None
rol = None

def set_sesion(sesion):
    global sesion_actual
    global correo
    global rol
    sesion_actual = sesion
    correo = sesion[1]
    rol = sesion[2]

def get_sesion():
    return sesion_actual

def get_correo():
    return correo

def get_rol():
    return rol
