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
    IN nombre_insertar VARCHAR(100))
BEGIN
    INSERT INTO tipo_estreno(nombre)
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

/* Creación de procedure para insertar en la tabla especificaciones_tecnicas . */
DELIMITER //

CREATE PROCEDURE sp_insert_especificaciones_tecnicas(
    IN nacionalidad_insertar VARCHAR(100),
    IN distribuidora_insertar VARCHAR(100), 
    IN presupuestos_insertar INT,
    IN año_produccion_insertar DATE,
    IN nombre_pelicula_insertar VARCHAR(100)
)
BEGIN
    DECLARE id_pelicula_new INT;
    DECLARE nacionalidad_existe INT;

    -- Verificar si la película ya existe en la tabla pelicula y obtener su id_pelicula
    SELECT id_pelicula INTO id_pelicula_new
    FROM pelicula
    WHERE nombre = nombre_pelicula_insertar
    LIMIT 1;

    -- Si la película existe, proceder con la verificación en la tabla especificaciones_tecnicas
    IF id_pelicula_new IS NOT NULL THEN
        -- Verificar si ya existe una entrada con el mismo id_pelicula y nacionalidad en especificaciones_tecnicas
        SELECT COUNT(*) INTO nacionalidad_existe
        FROM especificaciones_tecnicas
        WHERE id_pelicula = id_pelicula_new AND nacionalidad = nacionalidad_insertar;

        -- Si no existe, proceder con la inserción en la tabla especificaciones_tecnicas
        IF nacionalidad_existe = 0 THEN
            INSERT INTO especificaciones_tecnicas(nacionalidad, distribuidora, presupuestos, año_produccion, id_pelicula)
            VALUES (nacionalidad_insertar, distribuidora_insertar, presupuestos_insertar, año_produccion_insertar, id_pelicula_new);
        END IF;
    END IF;
END //

DELIMITER ;

/* Creación de procedure para insertar en la tabla director_pelicula, donde válidalos ids,
 con con nombre. */

DELIMITER //

CREATE PROCEDURE sp_insert_director_pelicula(
    IN nombre_director_insertar VARCHAR(100),
    IN nombre_pelicula_insertar VARCHAR(100)
)
BEGIN
    DECLARE id_director_insertar INT;
    DECLARE id_pelicula_insertar INT;
    DECLARE director_found BOOLEAN DEFAULT FALSE;
    DECLARE pelicula_found BOOLEAN DEFAULT FALSE;

    -- Verificar si el nombre del director existe en la tabla director y extraer el id
    SELECT id_director INTO id_director_insertar
    FROM director
    WHERE nombre = nombre_director_insertar
    LIMIT 1;

    -- Verificar si se encontró el director
    IF id_director_insertar IS NOT NULL THEN
        SET director_found = TRUE;
    END IF;

    -- Verificar si el nombre de la película existe en la tabla pelicula y extraer el id
    SELECT id_pelicula INTO id_pelicula_insertar
    FROM pelicula
    WHERE nombre = nombre_pelicula_insertar
    LIMIT 1;

    -- Verificar si se encontró la película
    IF id_pelicula_insertar IS NOT NULL THEN
        SET pelicula_found = TRUE;
    END IF;

    -- Verificar si ambos, el director y la película, fueron encontrados
    IF director_found AND pelicula_found THEN
        -- Verificar si la relación entre el director y la película ya existe
        IF NOT EXISTS (
            SELECT 1
            FROM director_pelicula
            WHERE id_director = id_director_insertar
            AND id_pelicula = id_pelicula_insertar
        ) THEN
            -- Si la relación no existe, proceder con la inserción
            INSERT INTO director_pelicula(id_director, id_pelicula)
            VALUES (id_director_insertar, id_pelicula_insertar);
        END IF;
    END IF;
END //

DELIMITER ;

CALL sp_insert_director_pelicula()

/* Creación de procedure para insertar en la tabla genero_pelicula, donde válida los ids,
 con con nombre. */

DELIMITER //

CREATE PROCEDURE sp_insert_genero_pelicula(
    IN nombre_genero_insertar VARCHAR(100),
    IN nombre_pelicula_insertar VARCHAR(100)
)
BEGIN
    DECLARE id_genero_insertar INT;
    DECLARE id_pelicula_insertar INT;
    DECLARE genero_found BOOLEAN DEFAULT FALSE;
    DECLARE pelicula_found BOOLEAN DEFAULT FALSE;

    -- Verificar si el nombre del género existe en la tabla genero y extraer el id
    SELECT id_genero INTO id_genero_insertar
    FROM genero
    WHERE nombre = nombre_genero_insertar
    LIMIT 1;

    -- Verificar si se encontró el género
    IF id_genero_insertar IS NOT NULL THEN
        SET genero_found = TRUE;
    END IF;

    -- Verificar si el nombre de la película existe en la tabla pelicula y extraer el id
    SELECT id_pelicula INTO id_pelicula_insertar
    FROM pelicula
    WHERE nombre = nombre_pelicula_insertar
    LIMIT 1;

    -- Verificar si se encontró la película
    IF id_pelicula_insertar IS NOT NULL THEN
        SET pelicula_found = TRUE;
    END IF;

    -- Verificar si ambos, el género y la película, fueron encontrados
    IF genero_found AND pelicula_found THEN
        -- Verificar si la relación entre el género y la película ya existe
        IF NOT EXISTS (
            SELECT 1
            FROM genero_pelicula
            WHERE id_genero = id_genero_insertar
            AND id_pelicula = id_pelicula_insertar
        ) THEN
            -- Si la relación no existe, proceder con la inserción
            INSERT INTO genero_pelicula(id_genero, id_pelicula)
            VALUES (id_genero_insertar, id_pelicula_insertar);
        END IF;
    END IF;
END //

DELIMITER ;

CALL sp_insert_genero_pelicula()

/* Creación de procedure para insertar en la tabla idioma_pelicula, donde válida los ids,
 con con nombre. */
 
DELIMITER //

CREATE PROCEDURE sp_insert_idioma_pelicula(
    IN nombre_idioma_insertar VARCHAR(100),
    IN nombre_pelicula_insertar VARCHAR(100)
)
BEGIN
    DECLARE id_idioma_insertar INT;
    DECLARE id_pelicula_insertar INT;
    DECLARE idioma_found BOOLEAN DEFAULT FALSE;
    DECLARE pelicula_found BOOLEAN DEFAULT FALSE;

    -- Verificar si el nombre del idioma existe en la tabla idioma y extraer el id
    SELECT id_idioma INTO id_idioma_insertar
    FROM idioma
    WHERE nombre = nombre_idioma_insertar
    LIMIT 1;

    -- Verificar si se encontró el idioma
    IF id_idioma_insertar IS NOT NULL THEN
        SET idioma_found = TRUE;
    END IF;

    -- Verificar si el nombre de la película existe en la tabla pelicula y extraer el id
    SELECT id_pelicula INTO id_pelicula_insertar
    FROM pelicula
    WHERE nombre = nombre_pelicula_insertar
    LIMIT 1;

    -- Verificar si se encontró la película
    IF id_pelicula_insertar IS NOT NULL THEN
        SET pelicula_found = TRUE;
    END IF;

    -- Verificar si ambos, el idioma y la película, fueron encontrados
    IF idioma_found AND pelicula_found THEN
        -- Verificar si la relación entre el idioma y la película ya existe
        IF NOT EXISTS (
            SELECT 1
            FROM idioma_pelicula
            WHERE id_idioma = id_idioma_insertar
            AND id_pelicula = id_pelicula_insertar
        ) THEN
            -- Si la relación no existe, proceder con la inserción
            INSERT INTO idioma_pelicula(id_idioma, id_pelicula)
            VALUES (id_idioma_insertar, id_pelicula_insertar);
        END IF;
    END IF;
END //

DELIMITER ;

CALL sp_insert_idioma_pelicula();

/* Creación de procedure para insertar en la tabla detalle_pelicula para válidar */
DELIMITER //

CREATE PROCEDURE sp_insert_detalle_pelicula(
    IN nombre_pelicula_insertar VARCHAR(100),
    IN duracion_insertar VARCHAR(100),
    IN fecha_insertar DATE
)
BEGIN
    DECLARE id_pelicula_insertar INT;

    -- Verificar si el nombre de la película existe en la tabla pelicula y extraer el id
    SELECT id_pelicula
    INTO id_pelicula_insertar
    FROM pelicula
    WHERE nombre = nombre_pelicula_insertar
    LIMIT 1;

    -- Si la película no existe, lanzar un error
    IF id_pelicula_insertar IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La película no existe en la tabla pelicula.';
    END IF;

    -- Insertar en detalle_pelicula usando el id_pelicula y los mismos valores para los otros campos
    INSERT INTO detalle_pelicula (duracion, fecha_de_estreno, id_pelicula, id_estreno, id_directorp, id_generop, id_idiomap)
    VALUES (duracion_insertar, fecha_insertar, id_pelicula_insertar, id_pelicula_insertar, id_pelicula_insertar, id_pelicula_insertar, id_pelicula_insertar);
END //

DELIMITER ;
CALL sp_insert_detalle_pelicula()