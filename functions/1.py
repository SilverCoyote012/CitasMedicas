import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Servicio de autenticación simulado
class AuthService:
    users = {
        "doctor@example.com": {"password": "doctor123", "role": "doctor"},
        "patient@example.com": {"password": "patient123", "role": "patient"},
        "admin@example.com": {"password": "admin123", "role": "admin"}
    }

    @staticmethod
    def login_user(email, password):
        user = AuthService.users.get(email)
        if user and user["password"] == password:
            return user["role"]
        return None

    @staticmethod
    def register_user(email, password, role):
        if email in AuthService.users:
            return False
        AuthService.users[email] = {"password": password, "role": role}
        return True

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clinica Management System")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        # Configuración de estilos
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Arial', 12, 'bold'), padding=10, background='#4CAF50', foreground='white')
        self.style.configure('TLabel', font=('Arial', 12), background="#f0f0f0", foreground='#333')
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('TFrame', background='#f0f0f0')

        self.current_user_role = None
        self.create_menu()
        self.create_login_screen()

    def create_menu(self):
        # Crear barra de menú
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Salir", command=self.quit)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        menu_bar.add_cascade(label="Ayuda", menu=help_menu)

        self.config(menu=menu_bar)

    def show_about(self):
        messagebox.showinfo("Acerca de", "Clinica Management System v1.0")

    def create_login_screen(self):
        # Limpiar pantalla actual
        for widget in self.winfo_children():
            widget.destroy()

        login_frame = ttk.Frame(self, padding="20", style='TFrame')
        login_frame.pack(pady=50)

        ttk.Label(login_frame, text="Email", style='TLabel').grid(row=0, column=0, pady=5, sticky='w')
        self.email_entry = ttk.Entry(login_frame, style='TEntry')
        self.email_entry.grid(row=0, column=1, pady=5)

        ttk.Label(login_frame, text="Contraseña", style='TLabel').grid(row=1, column=0, pady=5, sticky='w')
        self.password_entry = ttk.Entry(login_frame, show="*", style='TEntry')
        self.password_entry.grid(row=1, column=1, pady=5)

        ttk.Button(login_frame, text="Iniciar sesión", command=self.login, style='TButton').grid(row=2, columnspan=2, pady=10)
        ttk.Button(login_frame, text="Registrarse", command=self.create_register_screen, style='TButton').grid(row=3, columnspan=2, pady=10)

    def create_register_screen(self):
        # Limpiar pantalla actual
        for widget in self.winfo_children():
            widget.destroy()

        register_frame = ttk.Frame(self, padding="20", style='TFrame')
        register_frame.pack(pady=50)

        ttk.Label(register_frame, text="Email", style='TLabel').grid(row=0, column=0, pady=5, sticky='w')
        self.reg_email_entry = ttk.Entry(register_frame, style='TEntry')
        self.reg_email_entry.grid(row=0, column=1, pady=5)

        ttk.Label(register_frame, text="Contraseña", style='TLabel').grid(row=1, column=0, pady=5, sticky='w')
        self.reg_password_entry = ttk.Entry(register_frame, show="*", style='TEntry')
        self.reg_password_entry.grid(row=1, column=1, pady=5)

        ttk.Label(register_frame, text="Rol", style='TLabel').grid(row=2, column=0, pady=5, sticky='w')
        self.role_combobox = ttk.Combobox(register_frame, values=["patient", "doctor", "admin"], style='TEntry')
        self.role_combobox.grid(row=2, column=1, pady=5)

        ttk.Button(register_frame, text="Registrarse", command=self.register, style='TButton').grid(row=3, columnspan=2, pady=10)
        ttk.Button(register_frame, text="Volver", command=self.create_login_screen, style='TButton').grid(row=4, columnspan=2, pady=10)

    def register(self):
        email = self.reg_email_entry.get()
        password = self.reg_password_entry.get()
        role = self.role_combobox.get()
        if AuthService.register_user(email, password, role):
            messagebox.showinfo("Éxito", "¡Registro exitoso!")
            self.create_login_screen()
        else:
            messagebox.showerror("Error", "El usuario ya existe")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = AuthService.login_user(email, password)
        if role:
            messagebox.showinfo("Éxito", "¡Inicio de sesión exitoso!")
            self.current_user_role = role
            if role == 'patient':
                self.create_patient_screen()
            elif role == 'doctor':
                self.create_doctor_screen()
            elif role == 'admin':
                self.create_admin_screen()
            else:
                messagebox.showerror("Error", "Rol desconocido")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def create_patient_screen(self):
        # Limpiar pantalla actual
        for widget in self.winfo_children():
            widget.destroy()
        self.create_patient_menu()
        ttk.Label(self, text="¡Bienvenido, Paciente!", style='TLabel').pack(pady=20)
        ttk.Button(self, text="Cerrar sesión", command=self.logout, style='TButton').pack(pady=10)

    def create_patient_menu(self):
        menu_bar = tk.Menu(self)
        patient_menu = tk.Menu(menu_bar, tearoff=0)
        patient_menu.add_command(label="Ver citas", command=self.view_appointments)
        patient_menu.add_command(label="Actualizar perfil", command=self.update_profile)
        patient_menu.add_command(label="Cerrar sesión", command=self.logout)
        menu_bar.add_cascade(label="Paciente", menu=patient_menu)
        self.config(menu=menu_bar)

    def create_doctor_screen(self):
        # Limpiar pantalla actual
        for widget in self.winfo_children():
            widget.destroy()
        self.create_doctor_menu()
        ttk.Label(self, text="¡Bienvenido, Doctor!", style='TLabel').pack(pady=20)
        ttk.Button(self, text="Cerrar sesión", command=self.logout, style='TButton').pack(pady=10)

    def create_doctor_menu(self):
        menu_bar = tk.Menu(self)
        doctor_menu = tk.Menu(menu_bar, tearoff=0)
        doctor_menu.add_command(label="Ver pacientes", command=self.view_patients)
        doctor_menu.add_command(label="Actualizar perfil", command=self.update_profile)
        doctor_menu.add_command(label="Cerrar sesión", command=self.logout)
        menu_bar.add_cascade(label="Doctor", menu=doctor_menu)
        self.config(menu=menu_bar)

    def create_admin_screen(self):
        # Limpiar pantalla actual
        for widget in self.winfo_children():
            widget.destroy()
        self.create_admin_menu()
        ttk.Label(self, text="¡Bienvenido, Administrador!", style='TLabel').pack(pady=20)
        ttk.Button(self, text="Cerrar sesión", command=self.logout, style='TButton').pack(pady=10)

    def create_admin_menu(self):
        menu_bar = tk.Menu(self)
        admin_menu = tk.Menu(menu_bar, tearoff=0)
        admin_menu.add_command(label="Gestionar usuarios", command=self.manage_users)
        admin_menu.add_command(label="Ver reportes", command=self.view_reports)
        admin_menu.add_command(label="Cerrar sesión", command=self.logout)
        menu_bar.add_cascade(label="Administrador", menu=admin_menu)
        self.config(menu=menu_bar)

    def logout(self):
        self.current_user_role = None
        self.create_login_screen()

    def view_appointments(self):
        messagebox.showinfo("Citas", "Aquí se mostrarán las citas del paciente.")

    def update_profile(self):
        messagebox.showinfo("Perfil", "Aquí se actualizará el perfil del usuario.")

    def view_patients(self):
        messagebox.showinfo("Pacientes", "Aquí se mostrarán los pacientes del doctor.")

    def manage_users(self):
        messagebox.showinfo("Usuarios", "Aquí se gestionarán los usuarios.")

    def view_reports(self):
        messagebox.showinfo("Reportes", "Aquí se mostrarán los reportes.")

if __name__ == "__main__":
    app = App()
    app.mainloop()