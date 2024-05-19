
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


CREATE TABLE genero(
id_genero INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));

CREATE TABLE idioma(
id_idioma INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100));

CREATE TABLE director_pelicula
(id_directorp INT PRIMARY KEY AUTO_INCREMENT,
id_director INT,
id_pelicula INT,
FOREIGN KEY (id_director) REFERENCES director (id_director),
FOREIGN KEY (id_pelicula ) REFERENCES pelicula (id_pelicula ));

CREATE TABLE genero_pelicula
(id_generop INT PRIMARY KEY AUTO_INCREMENT,
id_genero INT,
id_pelicula INT,
FOREIGN KEY (id_genero) REFERENCES genero (id_genero),
FOREIGN KEY (id_pelicula ) REFERENCES pelicula (id_pelicula ));


CREATE TABLE idioma_pelicula
(id_idiomap INT PRIMARY KEY AUTO_INCREMENT,
id_idioma INT,
id_pelicula INT,
FOREIGN KEY (id_idioma) REFERENCES idioma (id_idioma),
FOREIGN KEY (id_pelicula ) REFERENCES pelicula (id_pelicula ));

CREATE TABLE detalle_pelicula(
id_detalles INT PRIMARY KEY AUTO_INCREMENT,
fecha DATE,
duracion VARCHAR(100),
guion VARCHAR(100),
id_pelicula INT,
id_estreno INT,
id_directorp INT,
id_generop INT,
id_idiomap INT,
FOREIGN KEY (id_pelicula) REFERENCES pelicula (id_pelicula),
FOREIGN KEY (id_estreno) REFERENCES estreno (id_estreno), 
FOREIGN KEY (id_directorp) REFERENCES director_pelicula (id_directorp),
FOREIGN KEY (id_generop) REFERENCES genero_pelicula (id_generop),
FOREIGN KEY (id_idiomap) REFERENCES idioma_pelicula (id_idiomap))









