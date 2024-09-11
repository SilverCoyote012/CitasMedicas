import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime  # This import is necessary for appointment_date handling
import mysql.connector
from mysql.connector import Error
import bcrypt
import re

class AuthService:
    DB_CONFIG = {
        'host': 'localhost',
        'database': 'Clinica',
        'user': 'root',
        'password': 'Alumno123'
    }

    @staticmethod
    def initialize_db():
        try:
            with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            email VARCHAR(255) NOT NULL UNIQUE,
                            password VARCHAR(255) NOT NULL,
                            role VARCHAR(50) NOT NULL
                        )
                    ''')
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS doctors (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            user_id INT NOT NULL,
                            specialty VARCHAR(255) NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES users(id)
                        )
                    ''')
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS patients (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            user_id INT NOT NULL,
                            name VARCHAR(255) NOT NULL,
                            age INT NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES users(id)
                        )
                    ''')
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS appointments (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            patient_id INT NOT NULL,
                            doctor_id INT NOT NULL,
                            appointment_date DATETIME NOT NULL,
                            status VARCHAR(50) NOT NULL,
                            FOREIGN KEY (patient_id) REFERENCES patients(id),
                            FOREIGN KEY (doctor_id) REFERENCES doctors(id)
                        )
                    ''')
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS medications (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            appointment_id INT NOT NULL,
                            medication_name VARCHAR(255) NOT NULL,
                            dosage VARCHAR(255) NOT NULL,
                            FOREIGN KEY (appointment_id) REFERENCES appointments(id)
                        )
                    ''')
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS logs (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            user_type VARCHAR(255) NOT NULL,
                            message TEXT NOT NULL,
                            level VARCHAR(255) NOT NULL,
                            timestamp DATETIME NOT NULL
                        )
                    ''')
                    conn.commit()
        except Error as e:
            print(f"Error: {e}")

    @staticmethod
    def register_user(email, password, role):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        INSERT INTO users (email, password, role) VALUES (%s, %s, %s)
                    ''', (email, hashed_password, role))
                    conn.commit()
                    return True
        except Error as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def register_doctor(email, password, specialty):
        if AuthService.register_user(email, password, 'doctor'):
            try:
                with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                    with conn.cursor() as cursor:
                        cursor.execute('''
                            SELECT id FROM users WHERE email = %s
                        ''', (email,))
                        user_id = cursor.fetchone()[0]
                        cursor.execute('''
                            INSERT INTO doctors (user_id, specialty) VALUES (%s, %s)
                        ''', (user_id, specialty))
                        conn.commit()
                        return True
            except Error as e:
                print(f"Error: {e}")
                return False
        return False

    @staticmethod
    def register_patient(email, password, name, age):
        if AuthService.register_user(email, password, 'patient'):
            try:
                with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                    with conn.cursor() as cursor:
                        cursor.execute('''
                            SELECT id FROM users WHERE email = %s
                        ''', (email,))
                        user_id = cursor.fetchone()[0]
                        cursor.execute('''
                            INSERT INTO patients (user_id, name, age) VALUES (%s, %s, %s)
                        ''', (user_id, name, age))
                        conn.commit()
                        return True
            except Error as e:
                print(f"Error: {e}")
                return False
        return False

    @staticmethod
    def login_user(email, password):
        try:
            with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT password, role FROM users WHERE email = %s
                    ''', (email,))
                    user = cursor.fetchone()
                    if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
                        return user[1]  # Return the role of the user
                    else:
                        return None
        except Error as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def create_appointment(patient_email, doctor_email, appointment_date):
        try:
            with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT id FROM users WHERE email = %s
                    ''', (patient_email,))
                    patient_id = cursor.fetchone()[0]
                    cursor.execute('''
                        SELECT id FROM users WHERE email = %s
                    ''', (doctor_email,))
                    doctor_id = cursor.fetchone()[0]
                    cursor.execute('''
                        INSERT INTO appointments (patient_id, doctor_id, appointment_date, status) VALUES (%s, %s, %s, %s)
                    ''', (patient_id, doctor_id, appointment_date, 'scheduled'))
                    conn.commit()
                    return True
        except Error as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def view_appointments(email, role):
        try:
            with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    if role == 'patient':
                        cursor.execute('''
                            SELECT a.id, d.user_id, a.appointment_date, a.status
                            FROM appointments a
                            JOIN patients p ON a.patient_id = p.id
                            JOIN doctors d ON a.doctor_id = d.id
                            JOIN users u ON p.user_id = u.id
                            WHERE u.email = %s
                        ''', (email,))
                    elif role == 'doctor':
                        cursor.execute('''
                            SELECT a.id, p.user_id, a.appointment_date, a.status
                            FROM appointments a
                            JOIN patients p ON a.patient_id = p.id
                            JOIN doctors d ON a.doctor_id = d.id
                            JOIN users u ON d.user_id = u.id
                            WHERE u.email = %s
                        ''', (email,))
                    appointments = cursor.fetchall()
                    return appointments
        except Error as e:
            print(f"Error: {e}")
            return []

    @staticmethod
    def assign_medication(appointment_id, medication_name, dosage):
        try:
            with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        INSERT INTO medications (appointment_id, medication_name, dosage) VALUES (%s, %s, %s)
                    ''', (appointment_id, medication_name, dosage))
                    cursor.execute('''
                        UPDATE appointments SET status = %s WHERE id = %s
                    ''', ('completed', appointment_id))
                    conn.commit()
                    return True
        except Error as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def view_users():
        try:
            with mysql.connector.connect(**AuthService.DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT id, email, role FROM users
                    ''')
                    users = cursor.fetchall()
                    return users
        except Error as e:
            print(f"Error: {e}")
            return []

class App(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Clinica Management System")
        self.geometry("600x400")
        self.configure(bg="#f0f0f0")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 12), padding=10, background="#4CAF50", foreground="white")
        self.style.configure('TLabel', font=('Helvetica', 12), background="#f0f0f0")
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.current_user_role = None
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        ttk.Label(self, text="Email").pack(pady=5)
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack(pady=5)
        ttk.Label(self, text="Password").pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        ttk.Button(self, text="Login", command=self.login).pack(pady=5)
        ttk.Button(self, text="Register Doctor", command=self.create_register_doctor_screen).pack(pady=5)
        ttk.Button(self, text="Register Patient", command=self.create_register_patient_screen).pack(pady=5)

    def create_register_doctor_screen(self):
        self.clear_screen()
        ttk.Label(self, text="Email").pack(pady=5)
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack(pady=5)
        ttk.Label(self, text="Password").pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        ttk.Label(self, text="Specialty").pack(pady=5)
        self.specialty_entry = ttk.Entry(self)
        self.specialty_entry.pack(pady=5)
        ttk.Button(self, text="Register", command=self.register_doctor).pack(pady=5)
        ttk.Button(self, text="Back", command=self.create_login_screen).pack(pady=5)

    def create_register_patient_screen(self):
        self.clear_screen()
        ttk.Label(self, text="Email").pack(pady=5)
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack(pady=5)
        ttk.Label(self, text="Password").pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        ttk.Label(self, text="Name").pack(pady=5)
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)
        ttk.Label(self, text="Age").pack(pady=5)
        self.age_entry = ttk.Entry(self)
        self.age_entry.pack(pady=5)
        ttk.Button(self, text="Register", command=self.register_patient).pack(pady=5)
        ttk.Button(self, text="Back", command=self.create_login_screen).pack(pady=5)

    def create_patient_screen(self):
        self.clear_screen()
        ttk.Button(self, text="Create Appointment", command=self.create_appointment_screen).pack(pady=5)
        ttk.Button(self, text="View Appointments", command=self.view_appointments).pack(pady=5)
        ttk.Button(self, text="Logout", command=self.logout).pack(pady=5)

    def create_doctor_screen(self):
        self.clear_screen()
        ttk.Button(self, text="View Appointments", command=self.view_appointments).pack(pady=5)
        ttk.Button(self, text="Logout", command=self.logout).pack(pady=5)

    def create_admin_screen(self):
        self.clear_screen()
        ttk.Button(self, text="View Users", command=self.view_users).pack(pady=5)
        ttk.Button(self, text="Logout", command=self.logout).pack(pady=5)

    def create_appointment_screen(self):
        self.clear_screen()
        ttk.Label(self, text="Doctor Email").pack(pady=5)
        self.doctor_email_entry = ttk.Entry(self)
        self.doctor_email_entry.pack(pady=5)
        ttk.Label(self, text="Appointment Date (YYYY-MM-DD HH:MM:SS)").pack(pady=5)
        self.appointment_date_entry = ttk.Entry(self)
        self.appointment_date_entry.pack(pady=5)
        ttk.Button(self, text="Create", command=self.create_appointment).pack(pady=5)
        ttk.Button(self, text="Back", command=self.create_patient_screen).pack(pady=5)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = AuthService.login_user(email, password)
        if role:
            self.current_user_role = role
            if role == 'patient':
                self.create_patient_screen()
            elif role == 'doctor':
                self.create_doctor_screen()
            elif role == 'admin':
                self.create_admin_screen()
            else:
                messagebox.showerror("Error", "Unknown role")
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register_doctor(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        specialty = self.specialty_entry.get()
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format")
            return
        
        if AuthService.register_doctor(email, password, specialty):
            messagebox.showinfo("Success", "Doctor registered successfully")
            self.create_login_screen()
        else:
            messagebox.showerror("Error", "Doctor registration failed")

    def register_patient(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format")
            return
        
        if AuthService.register_patient(email, password, name, age):
            messagebox.showinfo("Success", "Patient registered successfully")
            self.create_login_screen()
        else:
            messagebox.showerror("Error", "Patient registration failed")

    def create_appointment(self):
        patient_email = self.email_entry.get()
        doctor_email = self.doctor_email_entry.get()
        appointment_date = self.appointment_date_entry.get()
        if AuthService.create_appointment(patient_email, doctor_email, appointment_date):
            messagebox.showinfo("Success", "Appointment created successfully")
            self.create_patient_screen()
        else:
            messagebox.showerror("Error", "Appointment creation failed")

    def view_appointments(self):
        email = self.email_entry.get()
        appointments = AuthService.view_appointments(email, self.current_user_role)
        self.clear_screen()
        for appointment in appointments:
            ttk.Label(self, text=f"Appointment ID: {appointment[0]}, User ID: {appointment[1]}, Date: {appointment[2]}, Status: {appointment[3]}").pack(pady=5)
        ttk.Button(self, text="Back", command=self.create_patient_screen if self.current_user_role == 'patient' else self.create_doctor_screen).pack(pady=5)

    def view_users(self):
        users = AuthService.view_users()
        self.clear_screen()
        for user in users:
            ttk.Label(self, text=f"User ID: {user[0]}, Email: {user[1]}, Role: {user[2]}").pack(pady=5)
        ttk.Button(self, text="Back", command=self.create_admin_screen).pack(pady=5)

    def logout(self):
        self.current_user_role = None
        self.create_login_screen()

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

if __name__ == "__main__":
    AuthService.initialize_db()
    app = App()
    app.mainloop()