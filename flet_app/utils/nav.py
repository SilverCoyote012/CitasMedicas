def go_to_main_page(page):
    from main import mainPage
    mainPage(page)

def go_to_menu_admin(page):
    from modules.modulesAdmin.menuAdmin import menuAdmin
    menuAdmin(page)

def go_to_menu_doctor(page):
    from modules.modulesDoctor.menuDoctor import menuDoctor
    menuDoctor(page)

def go_to_menu_paciente(page):
    from modules.modulesPatient.menuPaciente import menuPaciente
    menuPaciente(page)