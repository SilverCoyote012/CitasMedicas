import flet as ft

from utils.nav import go_to_menu_admin
from utils.conexion import conexionDataBase

from modules.dataBaseInfo.addData import agregarUsuarioDB, agregarDoctorDB, agregarDomicilioDoctorDB
from modules.dataBaseInfo.delateData import eliminarDoctorDB

def agregarDoctor(page: ft.Page):
    correo = ft.TextField(label="Correo", width=600)
    password = ft.TextField(label="Contraseña", width=600)

    nombre = ft.TextField(label="Nombre", width=600)
    apellido = ft.TextField(label="Apellido", width=600)
    telefono = ft.TextField(label="Teléfono", width=600)

    def buscarEspecialidades():
        try:
            conexion = conexionDataBase()
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Especialidades"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            
            especialidades = []
            for especialidad in resultado:
                especialidades.append(especialidad[1])
            return especialidades
        except Exception as e:
            print("Error: ", e)
            return []
    
    especialidad = ft.Dropdown(
        label="Especialidad",
        options=[ft.dropdown.Option(text=especialidad) for especialidad in buscarEspecialidades()],
        width=600
    )

    calle = ft.TextField(label="Calle", width=600)
    numero = ft.TextField(label="Número", width=600)
    codigoPostal = ft.TextField(label="Codigo Postal", width=600)
    colonia = ft.TextField(label="Colonia", width=600)
    ciudad = ft.TextField(label="Ciudad", width=600)
    estado = ft.TextField(label="Estado", width=600)
    pais = ft.TextField(label="País", width=600)

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
        # colocar dos botones en la misma fila
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Agregar Doctor",
                    on_click=lambda e: [
                        print(especialidad.value),
                        usuario_id := agregarUsuarioDB(correo.value, password.value, "Doctor"),
                        id_direccion := agregarDomicilioDoctorDB(calle.value, numero.value, codigoPostal.value, colonia.value, ciudad.value, estado.value, pais.value),
                        print(usuario_id),
                        print(id_direccion),
                        agregarDoctorDB(nombre.value, apellido.value, telefono.value, especialidad.value, id_direccion, usuario_id),
                        go_to_menu_admin(page)
                    ]
                ),
                ft.ElevatedButton(
                    text="Cancelar",
                    on_click=lambda e: go_to_menu_admin(page)
                ),
            ],
        ),
    ]

    page.update()


def eliminarDoctor(page: ft.Page):
    def buscarDoctores():
        try:
            conexion = conexionDataBase()
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Doctores"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            
            doctores = []
            for doctor in resultado:
                doctores.append(doctor)
            return doctores
        except Exception as e:
            print("Error: ", e)
            return []

    # Creando las filas para la tabla
    filas_doctores = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(doctor[0]))),
                ft.DataCell(ft.Text(doctor[1])),
                ft.DataCell(ft.Text(doctor[2])),
                ft.DataCell(ft.Text(doctor[3])),
            ]
        )
        for doctor in buscarDoctores()
    ]

    doctores = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID"), numeric=True),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Especialidad")),
        ],
        rows=filas_doctores,
    )

    tabla_con_scroll = ft.Container(
        content=ft.ListView(
            controls=[doctores],
            expand=True,
        ),
        width=600,
        height=300,
    )

    id_doctor = ft.TextField(label="ID Doctor", width=600)
    button = ft.ElevatedButton(
        text="Eliminar Doctor",
        on_click=lambda e: [
            eliminarDoctorDB(id_doctor.value),
            go_to_menu_admin(page),
        ]
    )
    buttonCancelar = ft.ElevatedButton(
        text="Cancelar",
        on_click=lambda e: go_to_menu_admin(page)
    )

    page.controls[0].controls[2].controls = [
        ft.Text("Eliminar Doctor", size=20),
        tabla_con_scroll,
        id_doctor,
        ft.Row(
            controls=[
                button,
                buttonCancelar,
            ],
        ),
    ]

    page.update()

