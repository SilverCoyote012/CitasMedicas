CREATE DATABASE IF NOT EXISTS Clinica;
USE Clinica;

CREATE TABLE IF NOT EXISTS USUARIOS (
    ID_Usuario INTEGER PRIMARY KEY AUTO_INCREMENT,
    Correo VARCHAR(100) NOT NULL UNIQUE,
    Password VARCHAR(100) NOT NULL,
    Rol VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS DOMICILIO_PACIENTES (
    ID_Domicilio INTEGER PRIMARY KEY AUTO_INCREMENT,
    Calle VARCHAR(100) NOT NULL,
    Numero_Domicilio VARCHAR(100) NOT NULL,
    Codigo_Postal VARCHAR(100) NOT NULL,
    Colonia VARCHAR(100) NOT NULL,
    Ciudad VARCHAR(100) NOT NULL,
    Estado VARCHAR(100) NOT NULL,
    Pais VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS PACIENTES (
    ID_Paciente INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Fecha_Nacimiento DATE NOT NULL,
    Sexo VARCHAR(100) NOT NULL,
    Telefono VARCHAR(100) NOT NULL,
    ID_Direccion INTEGER NOT NULL,
    ID_Usuario INTEGER NOT NULL,
    FOREIGN KEY (ID_Direccion) REFERENCES DOMICILIO_PACIENTES(ID_Domicilio),
    FOREIGN KEY (ID_Usuario) REFERENCES USUARIOS(ID_Usuario)
);

CREATE TABLE IF NOT EXISTS ESPECIALIDADES (
    ID_Especialidad INTEGER PRIMARY KEY AUTO_INCREMENT,
    Especialidad VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS DOMICILIO_DOCTORES (
    ID_Domicilio INTEGER PRIMARY KEY AUTO_INCREMENT,
    Calle VARCHAR(100) NOT NULL,
    Numero_Domicilio VARCHAR(100) NOT NULL,
    Codigo_Postal VARCHAR(100) NOT NULL,
    Colonia VARCHAR(100) NOT NULL,
    Ciudad VARCHAR(100) NOT NULL,
    Estado VARCHAR(100) NOT NULL,
    Pais VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS DOCTORES (
    ID_Doctor INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Telefono VARCHAR(100) NOT NULL,
    ID_Especialidad INTEGER NOT NULL,
    ID_Direccion INTEGER NOT NULL,
    ID_Usuario INTEGER NOT NULL,
    FOREIGN KEY (ID_Especialidad) REFERENCES ESPECIALIDADES(ID_Especialidad),
    FOREIGN KEY (ID_Direccion) REFERENCES DOMICILIO_DOCTORES(ID_Domicilio),
    FOREIGN KEY (ID_Usuario) REFERENCES USUARIOS(ID_Usuario)
);

CREATE TABLE IF NOT EXISTS CITAS (
    ID_Cita INTEGER PRIMARY KEY AUTO_INCREMENT,
    ID_Paciente INTEGER NOT NULL,
    ID_Doctor INTEGER NOT NULL,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    Motivo VARCHAR(100) NOT NULL,
    FOREIGN KEY (ID_Paciente) REFERENCES PACIENTES(ID_Paciente),
    FOREIGN KEY (ID_Doctor) REFERENCES DOCTORES(ID_Doctor)
);

CREATE TABLE IF NOT EXISTS CONSULTAS (
    ID_Consulta INTEGER PRIMARY KEY AUTO_INCREMENT,
    ID_Cita INTEGER NOT NULL,
    Diagnostico VARCHAR(100) NOT NULL,
    Tratamiento VARCHAR(100) NOT NULL,
    Notas VARCHAR(100) NOT NULL,
    FOREIGN KEY (ID_Cita) REFERENCES CITAS(ID_Cita)
);

-- ================================================================================================= --

-- Inserción de 30 registros en la tabla USUARIOS
INSERT INTO USUARIOS (Correo, Password, Rol) VALUES
('usuario1@example.com', 'password1', 'Doctor'),
('usuario2@example.com', 'password2', 'Doctor'),
('usuario3@example.com', 'password3', 'Doctor'),
('usuario4@example.com', 'password4', 'Doctor'),
('usuario5@example.com', 'password5', 'Doctor'),
('usuario6@example.com', 'password6', 'Doctor'),
('usuario7@example.com', 'password7', 'Doctor'),
('usuario8@example.com', 'password8', 'Doctor'),
('usuario9@example.com', 'password9', 'Doctor'),
('usuario10@example.com', 'password10', 'Doctor'),
('usuario11@example.com', 'password11', 'Doctor'),
('usuario12@example.com', 'password12', 'Doctor'),
('usuario13@example.com', 'password13', 'Doctor'),
('usuario14@example.com', 'password14', 'Doctor'),
('usuario15@example.com', 'password15', 'Doctor'),
('usuario16@example.com', 'password16', 'Paciente'),
('usuario17@example.com', 'password17', 'Paciente'),
('usuario18@example.com', 'password18', 'Paciente'),
('usuario19@example.com', 'password19', 'Paciente'),
('usuario20@example.com', 'password20', 'Paciente'),
('usuario21@example.com', 'password21', 'Paciente'),
('usuario22@example.com', 'password22', 'Paciente'),
('usuario23@example.com', 'password23', 'Paciente'),
('usuario24@example.com', 'password24', 'Paciente'),
('usuario25@example.com', 'password25', 'Paciente'),
('usuario26@example.com', 'password26', 'Paciente'),
('usuario27@example.com', 'password27', 'Paciente'),
('usuario28@example.com', 'password28', 'Paciente'),
('usuario29@example.com', 'password29', 'Paciente'),
('usuario30@example.com', 'password30', 'Paciente');

-- Inserción de 30 registros en la tabla DOMICILIO_USUARIOS
INSERT INTO DOMICILIO_PACIENTES (Calle, Numero_Domicilio, Codigo_Postal, Colonia, Ciudad, Estado, Pais) VALUES
('Calle 1', '123', '10000', 'Colonia A', 'Ciudad A', 'Estado A', 'Pais A'),
('Calle 2', '456', '10001', 'Colonia B', 'Ciudad B', 'Estado B', 'Pais B'),
('Calle 3', '789', '10002', 'Colonia C', 'Ciudad C', 'Estado C', 'Pais C'),
('Calle 4', '101', '10003', 'Colonia D', 'Ciudad D', 'Estado D', 'Pais D'),
('Calle 5', '202', '10004', 'Colonia E', 'Ciudad E', 'Estado E', 'Pais E'),
('Calle 6', '303', '10005', 'Colonia F', 'Ciudad F', 'Estado F', 'Pais F'),
('Calle 7', '404', '10006', 'Colonia G', 'Ciudad G', 'Estado G', 'Pais G'),
('Calle 8', '505', '10007', 'Colonia H', 'Ciudad H', 'Estado H', 'Pais H'),
('Calle 9', '606', '10008', 'Colonia I', 'Ciudad I', 'Estado I', 'Pais I'),
('Calle 10', '707', '10009', 'Colonia J', 'Ciudad J', 'Estado J', 'Pais J'),
('Calle 11', '808', '10010', 'Colonia K', 'Ciudad K', 'Estado K', 'Pais K'),
('Calle 12', '909', '10011', 'Colonia L', 'Ciudad L', 'Estado L', 'Pais L'),
('Calle 13', '111', '10012', 'Colonia M', 'Ciudad M', 'Estado M', 'Pais M'),
('Calle 14', '222', '10013', 'Colonia N', 'Ciudad N', 'Estado N', 'Pais N'),
('Calle 15', '333', '10014', 'Colonia O', 'Ciudad O', 'Estado O', 'Pais O');

-- Inserción de 30 registros en la tabla PACIENTES
INSERT INTO PACIENTES (Nombre, Apellido, Fecha_Nacimiento, Sexo, Telefono, ID_Direccion, ID_Usuario) VALUES
('Gabriela', 'Romero', '1992-04-16', 'Femenino', '555-2526', 1, 16),
('Andrés', 'Vargas', '1987-05-17', 'Masculino', '555-2728', 2, 17),
('Marta', 'Peña', '1976-06-18', 'Femenino', '555-2930', 3, 18),
('Pablo', 'Santos', '1986-07-19', 'Masculino', '555-3132', 4, 19),
('Raquel', 'Iglesias', '1994-08-20', 'Femenino', '555-3334', 5, 20),
('Diego', 'Ramos', '1979-09-21', 'Masculino', '555-3536', 6, 21),
('Lucía', 'Medina', '1983-10-22', 'Femenino', '555-3738', 7, 22),
('Ramón', 'Suárez', '1990-11-23', 'Masculino', '555-3940', 8, 23),
('Isabel', 'Delgado', '1985-12-24', 'Femenino', '555-4142', 9, 24),
('Javier', 'Muñoz', '1980-01-25', 'Masculino', '555-4344', 10, 25),
('Mariana', 'Gil', '1996-02-26', 'Femenino', '555-4546', 11, 26),
('Fernando', 'Reyes', '1977-03-27', 'Masculino', '555-4748', 12, 27),
('Silvia', 'Cruz', '1982-04-28', 'Femenino', '555-4950', 13, 28),
('Gustavo', 'Pérez', '1991-05-29', 'Masculino', '555-5152', 14, 29),
('Natalia', 'Hernández', '1987-06-30', 'Femenino', '555-5354', 15, 30);

-- Inserción de 30 registros en la tabla ESPECIALIDADES
INSERT INTO ESPECIALIDADES (Especialidad) VALUES
('Cardiología'),
('Dermatología'),
('Endocrinología'),
('Gastroenterología'),
('Geriatría'),
('Ginecología'),
('Hematología'),
('Infectología'),
('Medicina interna'),
('Nefrología'),
('Neumología'),
('Neurología'),
('Nutriología'),
('Oftalmología'),
('Oncología'),
('Otorrinolaringología'),
('Pediatría'),
('Psiquiatría'),
('Reumatología'),
('Traumatología');

-- Inserción de 30 registros en la tabla DOMICILIO_DOCTORES
INSERT INTO DOMICILIO_DOCTORES (Calle, Numero_Domicilio, Codigo_Postal, Colonia, Ciudad, Estado, Pais) VALUES
('Calle A', '101', '20000', 'Colonia A', 'Ciudad A', 'Estado A', 'Pais A'),
('Calle B', '202', '20001', 'Colonia B', 'Ciudad B', 'Estado B', 'Pais B'),
('Calle C', '303', '20002', 'Colonia C', 'Ciudad C', 'Estado C', 'Pais C'),
('Calle D', '404', '20003', 'Colonia D', 'Ciudad D', 'Estado D', 'Pais D'),
('Calle E', '505', '20004', 'Colonia E', 'Ciudad E', 'Estado E', 'Pais E'),
('Calle F', '606', '20005', 'Colonia F', 'Ciudad F', 'Estado F', 'Pais F'),
('Calle G', '707', '20006', 'Colonia G', 'Ciudad G', 'Estado G', 'Pais G'),
('Calle H', '808', '20007', 'Colonia H', 'Ciudad H', 'Estado H', 'Pais H'),
('Calle I', '909', '20008', 'Colonia I', 'Ciudad I', 'Estado I', 'Pais I'),
('Calle J', '1010', '20009', 'Colonia J', 'Ciudad J', 'Estado J', 'Pais J'),
('Calle K', '1111', '20010', 'Colonia K', 'Ciudad K', 'Estado K', 'Pais K'),
('Calle L', '1212', '20011', 'Colonia L', 'Ciudad L', 'Estado L', 'Pais L'),
('Calle M', '1313', '20012', 'Colonia M', 'Ciudad M', 'Estado M', 'Pais M'),
('Calle N', '1414', '20013', 'Colonia N', 'Ciudad N', 'Estado N', 'Pais N'),
('Calle O', '1515', '20014', 'Colonia O', 'Ciudad O', 'Estado O', 'Pais O');

-- Inserción de 30 registros en la tabla DOCTORES
INSERT INTO DOCTORES (Nombre, Apellido, Telefono, ID_Especialidad, ID_Direccion, ID_Usuario) VALUES
('Dr. Juan', 'Martínez', '555-0011', 1, 1, 1),
('Dr. Ana', 'García', '555-0022', 2, 2, 2),
('Dr. Luis', 'Pérez', '555-0033', 3, 3, 3),
('Dr. Carlos', 'Hernández', '555-0044', 4, 4, 4),
('Dr. Laura', 'López', '555-0055', 5, 5, 5),
('Dr. Roberto', 'Díaz', '555-0066', 6, 6, 6),
('Dr. Sofía', 'Méndez', '555-0077', 7, 7, 7),
('Dr. José', 'Fernández', '555-0088', 8, 8, 8),
('Dr. Elena', 'Ruiz', '555-0099', 9, 9, 9),
('Dr. Jorge', 'Jiménez', '555-0101', 10, 10, 10),
('Dr. Claudia', 'Morales', '555-0112', 11, 11, 11),
('Dr. Miguel', 'Ortiz', '555-0123', 12, 12, 12),
('Dr. Patricia', 'García', '555-0134', 13, 13, 13),
('Dr. Francisco', 'Castillo', '555-0145', 14, 14, 14),
('Dr. Gabriela', 'Romero', '555-0156', 15, 15, 15);

-- Inserción de 30 registros en la tabla CITAS
INSERT INTO CITAS (ID_Paciente, ID_Doctor, Fecha, Hora, Motivo) VALUES
(1, 1, '2024-09-01', '10:00', 'Chequeo general'),
(2, 2, '2024-09-01', '11:00', 'Dolor de cabeza'),
(3, 3, '2024-09-01', '12:00', 'Dolor de estómago'),
(4, 4, '2024-09-02', '09:00', 'Chequeo general'),
(5, 5, '2024-09-02', '10:30', 'Dolor muscular'),
(6, 6, '2024-09-02', '11:30', 'Dolor de garganta'),
(7, 7, '2024-09-02', '12:30', 'Chequeo general'),
(8, 8, '2024-09-02', '13:30', 'Dolor de cabeza'),
(9, 9, '2024-09-02', '14:30', 'Dolor de estómago'),
(10, 10, '2024-09-02', '15:30', 'Chequeo general'),
(11, 11, '2024-09-03', '09:00', 'Dolor muscular'),
(12, 12, '2024-09-03', '10:00', 'Chequeo general'),
(13, 13, '2024-09-03', '11:00', 'Dolor de cabeza'),
(14, 14, '2024-09-03', '12:00', 'Dolor de estómago'),
(15, 15, '2024-09-03', '13:00', 'Chequeo general'),
(1, 1, '2024-09-03', '14:00', 'Dolor muscular'),
(2, 2, '2024-09-03', '15:00', 'Dolor de garganta'),
(3, 3, '2024-09-03', '16:00', 'Chequeo general'),
(4, 4, '2024-09-04', '09:00', 'Dolor de cabeza'),
(5, 5, '2024-09-04', '10:00', 'Dolor de estómago'),
(6, 6, '2024-09-04', '11:00', 'Chequeo general'),
(7, 7, '2024-09-04', '12:00', 'Dolor muscular'),
(8, 8, '2024-09-04', '13:00', 'Dolor de garganta'),
(9, 9, '2024-09-04', '14:00', 'Chequeo general'),
(10, 10, '2024-09-04', '15:00', 'Dolor de cabeza'),
(11, 11, '2024-09-04', '16:00', 'Dolor de estómago'),
(12, 12, '2024-09-05', '09:00', 'Chequeo general'),
(13, 13, '2024-09-05', '10:00', 'Dolor muscular'),
(14, 14, '2024-09-05', '11:00', 'Dolor de garganta'),
(15, 15, '2024-09-05', '12:00', 'Chequeo general'),
(1, 1, '2024-09-05', '13:00', 'Dolor de cabeza'),
(2, 2, '2024-09-05', '14:00', 'Dolor de estómago'),
(3, 3, '2024-09-05', '15:00', 'Chequeo general'),
(4, 4, '2024-09-05', '16:00', 'Dolor muscular'),
(5, 5, '2024-09-06', '09:00', 'Dolor de garganta'),
(6, 6, '2024-09-06', '10:00', 'Chequeo general'),
(7, 7, '2024-09-06', '11:00', 'Dolor de cabeza'),
(8, 8, '2024-09-06', '12:00', 'Dolor de estómago'),
(9, 9, '2024-09-06', '13:00', 'Chequeo general'),
(10, 10, '2024-09-06', '14:00', 'Dolor muscular'),
(11, 11, '2024-09-06', '15:00', 'Dolor de garganta'),
(12, 12, '2024-09-06', '16:00', 'Chequeo general'),
(13, 13, '2024-09-07', '09:00', 'Dolor de cabeza'),
(14, 14, '2024-09-07', '10:00', 'Dolor de estómago'),
(15, 15, '2024-09-07', '11:00', 'Chequeo general');

-- Inserción de 30 registros en la tabla CONSULTAS
INSERT INTO CONSULTAS (ID_Cita, Diagnostico, Tratamiento, Notas) VALUES
(1, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(2, 'Migraña', 'Ibuprofeno 400mg', 'Dolor intenso'),
(3, 'Gastritis', 'Omeprazol 20mg', 'Recomendación de dieta'),
(4, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(5, 'Contractura muscular', 'Relajante muscular', 'Ejercicios recomendados'),
(6, 'Amigdalitis', 'Antibiótico', 'Reposo recomendado'),
(7, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(8, 'Migraña', 'Ibuprofeno 400mg', 'Dolor intenso'),
(9, 'Gastritis', 'Omeprazol 20mg', 'Recomendación de dieta'),
(10, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(11, 'Contractura muscular', 'Relajante muscular', 'Ejercicios recomendados'),
(12, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(13, 'Migraña', 'Ibuprofeno 400mg', 'Dolor intenso'),
(14, 'Gastritis', 'Omeprazol 20mg', 'Recomendación de dieta'),
(15, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(16, 'Contractura muscular', 'Relajante muscular', 'Ejercicios recomendados'),
(17, 'Amigdalitis', 'Antibiótico', 'Reposo recomendado'),
(18, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(19, 'Migraña', 'Ibuprofeno 400mg', 'Dolor intenso'),
(20, 'Gastritis', 'Omeprazol 20mg', 'Recomendación de dieta'),
(21, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(22, 'Contractura muscular', 'Relajante muscular', 'Ejercicios recomendados'),
(23, 'Amigdalitis', 'Antibiótico', 'Reposo recomendado'),
(24, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(25, 'Migraña', 'Ibuprofeno 400mg', 'Dolor intenso'),
(26, 'Gastritis', 'Omeprazol 20mg', 'Recomendación de dieta'),
(27, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(28, 'Contractura muscular', 'Relajante muscular', 'Ejercicios recomendados'),
(29, 'Amigdalitis', 'Antibiótico', 'Reposo recomendado'),
(30, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(31, 'Migraña', 'Ibuprofeno 400mg', 'Dolor intenso'),
(32, 'Gastritis', 'Omeprazol 20mg', 'Recomendación de dieta'),
(33, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(34, 'Contractura muscular', 'Relajante muscular', 'Ejercicios recomendados'),
(35, 'Amigdalitis', 'Antibiótico', 'Reposo recomendado'),
(36, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(37, 'Migraña', 'Ibuprofeno 400mg', 'Dolor intenso'),
(38, 'Gastritis', 'Omeprazol 20mg', 'Recomendación de dieta'),
(39, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(40, 'Contractura muscular', 'Relajante muscular', 'Ejercicios recomendados'),
(41, 'Amigdalitis', 'Antibiótico', 'Reposo recomendado'),
(42, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina'),
(43, 'Migraña', 'Ibuprofeno 400mg', 'Dolor intenso'),
(44, 'Gastritis', 'Omeprazol 20mg', 'Recomendación de dieta'),
(45, 'Saludable', 'No requiere tratamiento', 'Chequeo de rutina');