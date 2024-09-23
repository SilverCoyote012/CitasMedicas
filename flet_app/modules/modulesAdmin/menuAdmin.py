import flet as ft

from modules.modulesAdmin.funcionesAdmin import agregarDoctor, eliminarDoctor, verDoctores

from utils.nav import go_to_main_page

def menuAdmin(page: ft.Page):
    page.title = "Menu Admin"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    agregarDoctorButton = ft.ElevatedButton(
        text="Agregar Doctor",
        on_click=lambda e: agregarDoctor(page)
    )
    eliminarDoctorButton = ft.ElevatedButton(
        text="Eliminar Doctor",
        on_click=lambda e: eliminarDoctor(page)
    )
    verDoctoresButton = ft.ElevatedButton(
        text="Ver Doctores",
        on_click=lambda e: verDoctores(page)
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
        on_click=lambda e: go_to_main_page(page)
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