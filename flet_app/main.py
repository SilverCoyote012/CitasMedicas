import flet as ft

from utils.conexion import conexionDataBase
from utils.sesion import set_sesion

# ====================================================== Funciones ====================================================== #
def on_login_click(page: ft.Page, username, password):
    try:
        conexion = conexionDataBase()
        cursor = conexion.cursor()
        consulta = "SELECT * FROM Usuarios WHERE Correo = %s AND Password = %s"
        cursor.execute(consulta, (username, password))
        resultado = cursor.fetchone()

        set_sesion(resultado)

        if resultado:
            if resultado[3] == 'Paciente':
                menuPaciente(page)
                pass
            elif resultado[3] == 'Doctor':
                menuDoctor(page)
                pass
            elif resultado[3] == 'Admin':
                menuAdmin(page)
        else:
            print("Usuario no registrado")
    except Exception as e:
        print("Error: ", e)

def on_register_click(page: ft.Page, username, password, password_confirm):
    if username and password and password_confirm:
        if password == password_confirm:
            conexion = conexionDataBase()
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Usuarios WHERE Correo = %s"
            cursor.execute(consulta, (username,))
            resultado = cursor.fetchone()

            if resultado:
                print("El correo ya está registrado")
            else:
                consulta = "INSERT INTO Usuarios (Correo, Password, Rol) VALUES (%s, %s, %s)"
                cursor.execute(consulta, (username, password, 'Paciente'))
                conexion.commit()
                print("Usuario registrado")
                mainPage(page)
        else:
            print("Las contraseñas no coinciden")
    else:
        print("Todos los campos son requeridos")

# ====================================================== Páginas ====================================================== #

def registerPage(page: ft.Page):
    page.title = "Registro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    username = ft.TextField(label="Correo", width=500)
    password = ft.TextField(label="Contraseña", password=True, width=500)
    password_confirm = ft.TextField(label="Confirmar contraseña", password=True, width=500)
    register_button = ft.ElevatedButton(
        text="Registrarse", 
        on_click=lambda e: on_register_click(page, username.value, password.value, password_confirm.value)
    )
    login_button = ft.ElevatedButton(text="Iniciar sesión", on_click=lambda e: mainPage(page))

    # Alinear en el centro
    page.controls = [
        ft.Column(
            controls=[
                ft.Text("Registro", size=20),
                username,
                password,
                password_confirm,
                register_button,
                ft.Text("¿Ya tienes cuenta?"),
                login_button,
            ],
        )
    ]
    page.update()

def agregarDoctor(page: ft.Page):
    page.controls[0].controls[2].controls = [
        ft.Text("Agregar Doctor", size=20),
        ft.TextField(label="Nombre", width=500),
        ft.TextField(label="Apellido", width=500),
        ft.TextField(label="Teléfono", width=500),
        ft.TextField(label="Especialidad", width=500),

        ft.TextField(label="Calle", width=500),
        ft.TextField(label="Número", width=500),
        ft.TextField(label="Codigo Postal", width=500),
        ft.TextField(label="Colonia", width=500),
        ft.TextField(label="Ciudad", width=500),
        ft.TextField(label="Estado", width=500),
        ft.TextField(label="País", width=500),
        ft.ElevatedButton(
            text="Agregar Doctor",
            on_click=lambda e: menuAdmin(page)

        ),
    ]
    page.update()

# Crear una dataTable para mostrar los doctores registrados en la base de datos y mover la tabla con un botón hacia arriba y hacia abajo y un TextField para buscar doctores por nombre
# def eliminarDoctor(page: ft.Page):
#     page.controls[0].controls[2].controls = [
#         ft.Text("Eliminar Doctor", size=20),
#         ft.TextField(label="Nombre", width=500),
#         ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Nombre")),
#                 ft.DataColumn(ft.Text("Apellido")),
#                 ft.DataColumn(ft.Text("Especialidad")),
#                 ft.DataColumn(ft.Text("Teléfono")),
#             ],
#             rows=[
#                 ft.DataRow(
#                     cells=[
#                         ft.Text("Juan"),
#                         ft.Text("Perez"),
#                         ft.Text("Cardiología"),
#                         ft.Text("1234567890"),
#                     ],
#                 ),
#                 ft.DataRow(
#                     cells=[
#                         ft.Text("Maria"),
#                         ft.Text("Gonzalez"),
#                         ft.Text("Pediatría"),
#                         ft.Text("0987654321"),
#                     ],
#                 ),
#                 ft.DataRow(
#                     cells=[
#                         ft.Text("Carlos"),
#                         ft.Text("Hernandez"),
#                         ft.Text("Dermatología"),
#                         ft.Text("6789012345"),
#                     ],
#                 ),
#                 ft.DataRow(
#                     cells=[
#                         ft.Text("Ana"),
#                         ft.Text("Ramirez"),
#                         ft.Text("Oftalmología"),
#                         ft.Text("4567890123"),
#                     ],
#                 ),
#             ],
#         ),
#         ft.ElevatedButton(
#             text="Eliminar Doctor",
#             on_click=lambda e: menuAdmin(page)
#         ),
#     ]
#     page.update()


def menuAdmin(page: ft.Page):
    page.title = "Menu Admin"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    agregarDoctorButton = ft.ElevatedButton(
        text="Agregar Doctor",
        on_click=lambda e: agregarDoctor(page)
    )
    eliminarDoctorButton = ft.ElevatedButton(
        text="Eliminar Doctor",
        # on_click=lambda e: eliminarDoctor(page)
    )
    verDoctoresButton = ft.ElevatedButton(
        text="Ver Doctores",
    )
    crearCitasButton = ft.ElevatedButton(
        text="Crear Citas",
    )
    verCitasButton = ft.ElevatedButton(
        text="Ver Citas",
    )
    eliminarCitasButton = ft.ElevatedButton(
        text="Eliminar Citas",
    )
    crearConsultasButton = ft.ElevatedButton(
        text="Crear Consultas",
    )
    verConsultasButton = ft.ElevatedButton(
        text="Ver Consultas",
    )
    eliminarConsultasButton = ft.ElevatedButton(
        text="Eliminar Consultas",
    )
    cerrarSesionButton = ft.ElevatedButton(
        text="Cerrar Sesion",
        on_click=lambda e: mainPage(page)
    )

    page.controls = [
        # Crear dos columnas
        ft.Row(
            controls=[
                cerrarSesionButton,

                ft.Column(
                    controls=[
                        ft.Text("MENU ADMIN", size=20),
                        agregarDoctorButton,
                        eliminarDoctorButton,
                        verDoctoresButton,
                        crearCitasButton,
                        verCitasButton,
                        eliminarCitasButton,
                        crearConsultasButton,
                        verConsultasButton,
                        eliminarConsultasButton,
                    ],
                    spacing=20,
                ),
                ft.Column(
                    controls=[
                        
                    ],
                    spacing=20,
                ),
            ],
            spacing=50,
            width = 1000,
        )
    ]
    page.update()

    return page

def menuDoctor(page: ft.Page):
    page.title = "Menu Doctor"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.controls = [
        ft.Column(
            controls=[
                ft.Text("Menu Doctor", size=20),
            ],
        )
    ]
    page.update()

def menuPaciente(page: ft.Page):
    page.title = "Menu Paciente"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.controls = [
        ft.Column(
            controls=[
                ft.Text("Menu Paciente", size=20),
            ],
        )
    ]
    page.update()

# ====================================================== Página principal ====================================================== #

def mainPage(page: ft.Page):
    page.title = "Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def show_login():
        username = ft.TextField(label="Correo", width=500)
        password = ft.TextField(label="Contraseña", password=True, width=500)
        login_button = ft.ElevatedButton(
            text="Iniciar sesión", 
            on_click=lambda e: on_login_click(page, username.value, password.value)
        )
        register_button = ft.ElevatedButton(
            text="Registrarse",
            on_click=lambda e: registerPage(page)
        )

        page.controls = [
            ft.Column(
                controls=[
                    ft.Text("Iniciar sesión", size=20),
                    username,
                    password,
                    login_button,
                    ft.Text("¿No tienes cuenta?"),
                    register_button,
                ],
                width=500,
                spacing=20,
            )
        ]
        page.update()

    show_login()

    return page

if __name__ == "__main__":
    ft.app(target=mainPage)