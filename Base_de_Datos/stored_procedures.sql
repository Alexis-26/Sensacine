/* Creación de procedure para insertar en la tabla pelicula, donde válida si la pelicula
insertada ya existe, si existe, no la agrega y si no existe, la agrega */
DELIMITER //

CREATE PROCEDURE sp_insert_pelicula(
IN nombre_insertar VARCHAR(100))

BEGIN
    -- Comprobar si ya existe una película con el mismo nombre
    IF NOT EXISTS (
        SELECT 1
        FROM pelicula
        WHERE nombre = nombre_insertar
    ) THEN
        -- Si no existe una película con ese nombre, proceder con la inserción
        INSERT INTO pelicula(nombre)
        VALUES (nombre_insertar);
    END IF;
END //

DELIMITER ;

CALL sp_insert_pelicula()

/* Creación de procedure para insertar en la tabla director, donde válida si el nombre
insertado ya existe, si existe, no la agrega y si no existe, la agrega. */
DELIMITER //

CREATE PROCEDURE sp_insert_director(
IN nombre_insertar VARCHAR(100))

BEGIN
    -- Comprobar si ya existe un director con el mismo nombre
    IF NOT EXISTS (
        SELECT 1
        FROM director
        WHERE nombre = nombre_insertar
    ) THEN
        -- Si no existe un director con ese nombre, proceder con la inserción
        INSERT INTO director(nombre)
        VALUES (nombre_insertar);
    END IF;
END //

DELIMITER ;

CALL sp_insert_director()

/* Creación de procedure para insertar en la tabla estreno, donde válida con el nombre */
DELIMITER //

CREATE PROCEDURE sp_insert_estreno(
    IN nombre_estreno_insertar VARCHAR(100),
    IN nombre_pelicula_insertar VARCHAR(100)
)
DELIMITER //
CREATE PROCEDURE sp_insert_estreno(
    IN nombre_insertar VARCHAR(100))
BEGIN
    INSERT INTO estreno(nombre)
    VALUES(nombre_insertar);
END//
DELIMITER ;

CALL sp_insert_estreno()

/* Creación de procedure para insertar en la tabla genero, donde válida si el nombre
insertado ya existe, si existe, no la agrega y si no existe, la agrega. */
DELIMITER //

CREATE PROCEDURE sp_insert_genero(
IN nombre_insertar VARCHAR(100))

BEGIN
    -- Comprobar si ya existe un género con el mismo nombre
    IF NOT EXISTS (
        SELECT 1
        FROM genero
        WHERE nombre = nombre_insertar
    ) THEN
        -- Si no existe un género con ese nombre, proceder con la inserción
        INSERT INTO genero(nombre)
        VALUES (nombre_insertar);
    END IF;
END //

DELIMITER ;

CALL sp_insert_genero()

/* Creación de procedure para insertar en la tabla idioma, donde válida si el nombre
insertado ya existe, si existe, no la agrega y si no existe, la agrega. */
DELIMITER //

CREATE PROCEDURE sp_insert_idioma(
IN nombre_insertar VARCHAR(100))

BEGIN
    -- Comprobar si ya existe un idioma con el mismo nombre
    IF NOT EXISTS (
        SELECT 1
        FROM idioma
        WHERE nombre = nombre_insertar
    ) THEN
        -- Si no existe un idioma con ese nombre, proceder con la inserción
        INSERT INTO idioma(nombre)
        VALUES (nombre_insertar);
    END IF;
END //

DELIMITER ;
CALL sp_insert_idioma()

/* Creación de procedure para insertar en la tabla puntaje. */
DELIMITER //

CREATE PROCEDURE sp_insert_puntaje(
IN medios_insertar DECIMAL(9,1),
IN usuarios_insertar DECIMAL(9,1), 
IN sensacine_insertar DECIMAL(9,1),
IN nombre_pelicula_insertar VARCHAR(100))

BEGIN
    DECLARE pelicula_existe INT;

    -- Verificar si la película ya existe en la tabla pelicula
    SELECT COUNT(*) INTO pelicula_existe
    FROM pelicula
    WHERE nombre = nombre_pelicula_insertar;

    -- Si la película existe, proceder con la inserción en la tabla puntaje
    IF pelicula_existe > 0 THEN
        INSERT INTO puntaje(medios, usuarios, sensacine, id_pelicula)
        SELECT medios_insertar, usuarios_insertar, sensacine_insertar, id_pelicula
        FROM pelicula
        WHERE nombre = nombre_pelicula_insertar;
    END IF;
END //

DELIMITER ;

CALL sp_insert_puntaje()
