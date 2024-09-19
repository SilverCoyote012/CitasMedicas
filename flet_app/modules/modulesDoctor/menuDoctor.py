import flet as ft

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