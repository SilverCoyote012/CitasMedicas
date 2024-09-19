import flet as ft

from utils.nav import go_to_main_page

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
            on_click=lambda e: go_to_main_page(page)
        ),
    ]
    page.update()