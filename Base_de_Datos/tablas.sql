
CREATE DATABASE sensacine;

USE sensacine;

CREATE TABLE pelicula(
id_pelicula INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));

CREATE TABLE puntaje(
id_puntaje INT PRIMARY KEY AUTO_INCREMENT, 
medios INT,
usuarios INT, 
sensacine INT,
id_pelicula INT,
FOREIGN KEY (id_pelicula) REFERENCES  pelicula (id_pelicula));

CREATE TABLE especificaciones_tecnicas(
id_especificaciones INT PRIMARY KEY AUTO_INCREMENT,
nacionalidad VARCHAR(100),
distribuidora VARCHAR(100),
presupuestos INT,
fecha_retorno VARCHAR(100),
año_produccion  DATE,
id_pelicula INT,
FOREIGN KEY (id_pelicula) REFERENCES  pelicula (id_pelicula));

CREATE TABLE director(
id_director INT PRIMARY KEY AUTO_INCREMENT,
Nombre VARCHAR(100));

CREATE TABLE estreno(
id_estreno INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));