import flet as ft
import mysql.connector

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
    login_button = ft.ElevatedButton(text="Iniciar sesión",)

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
            width=500,
            spacing=20,
        )
    ]
    page.update()

def menuAdmin(page: ft.Page):
    page.title = "Menu Admin"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.controls = [
        ft.Column(
            controls=[
                ft.Text("Menu Admin", size=20),
            ],
            width=400,
            spacing=20,
        )
    ]
    page.update()

def menuDoctor(page: ft.Page):
    page.title = "Menu Doctor"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.controls = [
        ft.Column(
            controls=[
                ft.Text("Menu Doctor", size=20),
            ],
            width=400,
            spacing=20,
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
            width=400,
            spacing=20,
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
                horizontal_alignment = ft.MainAxisAlignment.CENTER,
                width=500,
                spacing=20,
            )
        ]
        page.update()

    show_login()

    return page

if __name__ == "__main__":
    ft.app(target=mainPage)
