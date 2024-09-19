import flet as ft

from utils.nav import go_to_menu_admin

from modules.dataBaseInfo.addData import agregarUsuario, agregarDoctor, agregarDomicilioDoctor

def agregarDoctor(page: ft.Page):
    correo = ft.TextField(label="Correo", width=500)
    password = ft.TextField(label="Contraseña", width=500)

    nombre = ft.TextField(label="Nombre", width=500)
    apellido = ft.TextField(label="Apellido", width=500)
    telefono = ft.TextField(label="Teléfono", width=500)
    especialidad = ft.TextField(label="Especialidad", width=500)

    calle = ft.TextField(label="Calle", width=500)
    numero = ft.TextField(label="Número", width=500)
    codigoPostal = ft.TextField(label="Codigo Postal", width=500)
    colonia = ft.TextField(label="Colonia", width=500)
    ciudad = ft.TextField(label="Ciudad", width=500)
    estado = ft.TextField(label="Estado", width=500)
    pais = ft.TextField(label="País", width=500)

    page.controls[0].controls[2].controls = [
        ft.Text("Agregar Doctor", size=20),
        correo,
        password,
        nombre,
        apellido,
        telefono,
        especialidad,
        calle,
        numero,
        codigoPostal,
        colonia,
        ciudad,
        estado,
        pais,
        ft.ElevatedButton(
            text="Agregar Doctor",
            on_click=lambda e: [
                usuario_id := agregarUsuario(correo.value, password.value, "Doctor"),
                id_direccion := agregarDomicilioDoctor(calle.value, numero.value, codigoPostal.value, colonia.value, ciudad.value, estado.value, pais.value),
                agregarDoctor(nombre.value, apellido.value, telefono.value, especialidad.value, id_direccion, usuario_id),
                go_to_menu_admin(page)
            ]
        ),
    ]

    page.update()