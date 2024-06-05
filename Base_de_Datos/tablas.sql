CREATE DATABASE sensacine;
USE sensacine;

/* Creacion de la tabla  pelicula*/
CREATE TABLE pelicula(
id_pelicula INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));

/* Creacion de la tabla  puntaje*/
CREATE TABLE puntaje(
id_puntaje INT PRIMARY KEY AUTO_INCREMENT, 
medios DECIMAL (9,1),
usuarios DECIMAL (9,1), 
sensacine DECIMAL (9,1),
id_pelicula INT,
FOREIGN KEY (id_pelicula) REFERENCES  pelicula (id_pelicula));

/* Creacion de la tabla especificaciones_tecnicas */
CREATE TABLE especificaciones_tecnicas(
id_especificaciones INT PRIMARY KEY AUTO_INCREMENT,
nacionalidad VARCHAR(100),
distribuidora VARCHAR(100),
presupuestos INT,
año_produccion DATE,
id_pelicula INT,
FOREIGN KEY (id_pelicula) REFERENCES  pelicula (id_pelicula));

/* Creacion de la tabla  director*/
CREATE TABLE director(
id_director INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));

/* Creacion de la tabla  estreno*/
CREATE TABLE tipo_estreno(
id_estreno INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));

/* Creacion de la tabla genero*/
CREATE TABLE genero(
id_genero INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));

/* Creacion de la tabla idioma*/
CREATE TABLE idioma(
id_idioma INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));

/* Creacion de la tabla  director_pelicula*/
CREATE TABLE director_pelicula
(id_directorp INT PRIMARY KEY AUTO_INCREMENT,
id_director INT,
id_pelicula INT,
FOREIGN KEY (id_director) REFERENCES director (id_director),
FOREIGN KEY (id_pelicula ) REFERENCES pelicula (id_pelicula ));

/* Creacion de la tabla  genero_pelicula*/
CREATE TABLE genero_pelicula
(id_generop INT PRIMARY KEY AUTO_INCREMENT,
id_genero INT,
id_pelicula INT,
FOREIGN KEY (id_genero) REFERENCES genero (id_genero),
FOREIGN KEY (id_pelicula ) REFERENCES pelicula (id_pelicula ));

/* Creacion de la tabla  idioma_pelicula*/
CREATE TABLE idioma_pelicula
(id_idiomap INT PRIMARY KEY AUTO_INCREMENT,
id_idioma INT,
id_pelicula INT,
FOREIGN KEY (id_idioma) REFERENCES idioma (id_idioma),
FOREIGN KEY (id_pelicula ) REFERENCES pelicula (id_pelicula ));

/* Creacion de la tabla  detalle_pelicula*/
CREATE TABLE detalle_pelicula
(id_detalles INT PRIMARY KEY AUTO_INCREMENT,
duracion VARCHAR(100),
fecha_de_estreno DATE,
id_pelicula INT,
id_estreno INT,
id_directorp INT,
id_generop INT,
id_idiomap INT,
FOREIGN KEY (id_pelicula) REFERENCES pelicula (id_pelicula),
FOREIGN KEY (id_estreno) REFERENCES tipo_estreno (id_estreno), 
FOREIGN KEY (id_directorp) REFERENCES director_pelicula (id_directorp),
FOREIGN KEY (id_generop) REFERENCES genero_pelicula (id_generop),
FOREIGN KEY (id_idiomap) REFERENCES idioma_pelicula (id_idiomap));






