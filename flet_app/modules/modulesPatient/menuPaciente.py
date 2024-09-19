import flet as ft

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