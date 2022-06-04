/*AUDITORIA ASIGNATURAS*/
DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_INSERT_ASIGNATURA`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `AUDITORIA_INSERT_ASIGNATURA` BEFORE INSERT ON `roducweb_asignatura` FOR EACH ROW BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
	)
    VALUES(
		'Asignatura',
        'I',
        NULL,
        CONCAT('Codigo: ', NEW.cod_asignatura, '| Descripcion: ', NEW.descripcion, '| Horas Catedras:', NEW.horas_catedra, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Curso: ', NEW.curso, '| Semestre: ', NEW.cod_semestre_id, '| Plan Estudio: ', NEW.cod_plan_estudio_id, '| Carrera: ', NEW.cod_carrera_id),
        NEW.alta_usuario,
        NOW()
    );
END$$
DELIMITER ;


DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_ASIGNATURA`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `AUDITORIA_UPDATE_ASIGNATURA` BEFORE UPDATE ON `roducweb_asignatura` FOR EACH ROW BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Asignatura',
        /*(CASE NEW.estado WHEN 0 THEN 'D' ELSE 'U' END),*/
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
        CONCAT('Codigo: ', OLD.cod_asignatura, '| Descripcion: ', OLD.descripcion, '| Horas Catedras:', OLD.horas_catedra, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha, '| Curso: ', OLD.curso, '| Semestre: ', OLD.cod_semestre_id, '| Plan Estudio: ', OLD.cod_plan_estudio_id, '| Carrera: ', OLD.cod_carrera_id),
		CONCAT('Codigo: ', NEW.cod_asignatura, '| Descripcion: ', NEW.descripcion, '| Horas Catedras:', NEW.horas_catedra, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha, '| Curso: ', NEW.curso, '| Semestre: ', NEW.cod_semestre_id, '| Plan Estudio: ', NEW.cod_plan_estudio_id, '| Carrera: ', NEW.cod_carrera_id),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA ASIGNATURA_USUARIO*/

DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_INSERT_ASIGNATURA_USUARIO`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_ASIGNATURA_USUARIO` BEFORE INSERT ON `roducweb_asignatura_usuario` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Asignatura_Usuario',
        'I',
        NULL,
        CONCAT('Codigo: ',NEW.cod_asignatura_usuario, '| Estado:', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Rol Usuario: ', NEW.cod_usuario_rol_id, '| Asignatura: ', NEW.cod_asignatura_id),
        NEW.alta_usuario,
        NOW()
    );
END$$
DELIMITER ;


DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_ASIGNATURA_USUARIO`;

DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_ASIGNATURA_USUARIO` BEFORE UPDATE ON `roducweb_asignatura_usuario` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Asignatura_Usuario',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
        CONCAT('Codigo: ', OLD.cod_asignatura_usuario, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha, '| Rol:', OLD.cod_usuario_rol_id, '| Asignatura: ', OLD.cod_asignatura_id),
		CONCAT('Codigo: ', NEW.cod_asignatura_usuario, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha, '| Rol:', NEW.cod_usuario_rol_id, '| Asignatura: ', NEW.cod_asignatura_id),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA USUARIOS*/

DROP TRIGGER IF EXISTS `roducdb`. `AUDITORIA_INSERT_USUARIO`;
DELIMITER $$
USE `roducdb` $$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_USUARIO` BEFORE INSERT ON `roducweb_usuario` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
		accion,
		datos_viejos,
		datos_nuevos,
		usuario,
		fecha
	)
	VALUES(
		'Usuarios',
		'I',
		NULL,
		CONCAT('Codigo: ', (SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'roducdb' AND TABLE_NAME = 'roducweb_usuario'), '| Nombre Usuario: ', NEW.nombre_usuario, '| Contraseña: ', NEW.contraseña, '| Nombres del usuario: ', NEW.nombres_del_usuario, '| Apellidos del Usuario: ', NEW.apellidos_del_usuario, '| Direccion Email: ', NEW.direccion_email, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha),
		NEW.alta_usuario,
		NOW()
	);
END$$
DELIMITER ;


DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_USUARIO`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_USUARIO` BEFORE UPDATE ON `roducweb_usuario` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Usuario',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
		CONCAT('Codigo: ', OLD.cod_usuario, '| Nombre Usuario: ', OLD.nombre_usuario, '| Contraseña: ', OLD.contraseña, '| Nombres del usuario: ', OLD.nombres_del_usuario, '| Apellidos del Usuario: ', OLD.apellidos_del_usuario, '| Direccion Email: ', OLD.direccion_email, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha),
		CONCAT('Codigo: ', NEW.cod_usuario, '| Nombre Usuario: ', NEW.nombre_usuario, '| Contraseña: ', NEW.contraseña, '| Nombres del usuario: ', NEW.nombres_del_usuario, '| Apellidos del Usuario: ', NEW.apellidos_del_usuario, '| Direccion Email: ', NEW.direccion_email, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA FACULTAD*/
DROP TRIGGER IF EXISTS `roducdb`. `AUDITORIA_INSERT_FACULTAD`;
DELIMITER $$
USE `roducdb` $$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_FACULTAD` BEFORE INSERT ON `roducweb_facultad` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
		accion,
		datos_viejos,
		datos_nuevos,
		usuario,
		fecha
	)
	VALUES(
		'Facultad',
		'I',
		NULL,
		CONCAT('Codigo: ', (SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'roducdb' AND TABLE_NAME = 'roducweb_facultad'), '| Descripcion: ', NEW.descripcion, '| Fecha Fundacion: ', NEW.fecha_fundacion, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha),
		NEW.alta_usuario,
		NOW()
	);
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_FACULTAD`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_FACULTAD` BEFORE UPDATE ON `roducweb_facultad` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Facultad',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
		CONCAT('Codigo: ', OLD.cod_facultad, '| Descripcion: ', OLD.descripcion, '| Fecha Fundacion: ', OLD.fecha_fundacion, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha),
		CONCAT('Codigo: ', NEW.cod_facultad, '| Descripcion: ', NEW.descripcion, '| Fecha Fundacion: ', NEW.fecha_fundacion, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA CARRERA*/
DROP TRIGGER IF EXISTS `roducdb`. `AUDITORIA_INSERT_CARRERA`;
DELIMITER $$
USE `roducdb` $$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_CARRERA` BEFORE INSERT ON `roducweb_carrera` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
		accion,
		datos_viejos,
		datos_nuevos,
		usuario,
		fecha
	)
	VALUES(
		'Carrera',
		'I',
		NULL,
		CONCAT('Codigo: ', (SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'roducdb' AND TABLE_NAME = 'roducweb_carrera'), '| Facultad: ', NEW.cod_facultad_id, '| Descripcion: ', NEW.descripcion, '| Duracion: ', NEW.duracion, '| Titulo Obtenido: ', NEW.titulo_obtenido, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha),
		NEW.alta_usuario,
		NOW()
	);
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_CARRERA`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_CARRERA` BEFORE UPDATE ON `roducweb_carrera` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Carrera',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
		CONCAT('Codigo: ', OLD.cod_carrera, '| Facultad: ', OLD.cod_facultad_id, '| Descripcion: ', OLD.descripcion, '| Duracion: ', OLD.duracion, '| Titulo Obtenido: ', OLD.titulo_obtenido, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha),
		CONCAT('Codigo: ', NEW.cod_carrera, '| Facultad: ', NEW.cod_facultad_id, '| Descripcion: ', NEW.descripcion, '| Duracion: ', NEW.duracion, '| Titulo Obtenido: ', NEW.titulo_obtenido, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA SEMESTRE*/
DROP TRIGGER IF EXISTS `roducdb`. `AUDITORIA_INSERT_SEMESTRE`;
DELIMITER $$
USE `roducdb` $$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_SEMESTRE` BEFORE INSERT ON `roducweb_semestre` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
		accion,
		datos_viejos,
		datos_nuevos,
		usuario,
		fecha
	)
	VALUES(
		'Semestre',
		'I',
		NULL,
		CONCAT('Codigo: ', (SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'roducdb' AND TABLE_NAME = 'roducweb_semestre'), '| Descripcion: ', NEW.descripcion, '| Fecha Inicio: ', NEW.fecha_inicio, '| Fecha Fin: ', NEW.fecha_fin, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha),
		NEW.alta_usuario,
		NOW()
	);
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_SEMESTRE`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_SEMESTRE` BEFORE UPDATE ON `roducweb_semestre` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Semestre',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
		CONCAT('Codigo: ', OLD.cod_semestre, '| Descripcion: ', OLD.descripcion, '| Fecha Inicio: ', OLD.fecha_inicio, '| Fecha Fin: ', OLD.fecha_fin, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha),
		CONCAT('Codigo: ', NEW.cod_semestre, '| Descripcion: ', NEW.descripcion, '| Fecha Inicio: ', NEW.fecha_inicio, '| Fecha Fin: ', NEW.fecha_fin, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA PLAN ESTUDIO*/
DROP TRIGGER IF EXISTS `roducdb`. `AUDITORIA_INSERT_PLAN_ESTUDIO`;
DELIMITER $$
USE `roducdb` $$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_PLAN_ESTUDIO` BEFORE INSERT ON `roducweb_plan_estudio` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
		accion,
		datos_viejos,
		datos_nuevos,
		usuario,
		fecha
	)
	VALUES(
		'Plan de Estudio',
		'I',
		NULL,
		CONCAT('Codigo: ', (SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'roducdb' AND TABLE_NAME = 'roducweb_plan_estudio'), '| Carrera: ', NEW.cod_carrera_id, '| Descripcion: ', NEW.descripcion, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha),
		NEW.alta_usuario,
		NOW()
	);
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_PLAN_ESTUDIO`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_PLAN_ESTUDIO` BEFORE UPDATE ON `roducweb_plan_estudio` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Plan de Estudio',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
		CONCAT('Codigo: ', OLD.cod_plan_estudio, '| Carrera: ', OLD.cod_carrera_id, '| Descripcion: ', OLD.descripcion, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha),
		CONCAT('Codigo: ', NEW.cod_plan_estudio, '| Carrera: ', NEW.cod_carrera_id, '| Descripcion: ', NEW.descripcion, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA USUARIOS_ROL*/
DROP TRIGGER IF EXISTS `roducdb`. `AUDITORIA_INSERT_USUARIOS_ROL`;
DELIMITER $$
USE `roducdb` $$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_USUARIOS_ROL` BEFORE INSERT ON `roducweb_usuario_rol` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
		accion,
		datos_viejos,
		datos_nuevos,
		usuario,
		fecha
	)
	VALUES(
		'Usuario Rol',
		'I',
		NULL,
		CONCAT('Codigo: ', (SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'roducdb' AND TABLE_NAME = 'roducweb_usuario_rol'), '| Usuario: ', NEW.cod_usuario_id, '| Rol: ', NEW.cod_rol_usuario_id, '| Carrera: ', NEW.cod_carrera_id, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha),
		NEW.alta_usuario,
		NOW()
	);
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_USUARIOS_ROL`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_USUARIOS_ROL` BEFORE UPDATE ON `roducweb_usuario_rol` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Plan de Estudio',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
		CONCAT('Codigo: ', OLD.cod_usuario_rol, '| Usuario: ', OLD.cod_usuario_id, '| Rol: ', OLD.cod_rol_usuario_id, '| Carrera: ', OLD.cod_carrera_id, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha),
		CONCAT('Codigo: ', NEW.cod_usuario_rol, '| Usuario: ', NEW.cod_usuario_id, '| Rol: ', NEW.cod_rol_usuario_id, '| Carrera: ', NEW.cod_carrera_id, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA TIPO_CLASE*/
DROP TRIGGER IF EXISTS `roducdb`. `AUDITORIA_INSERT_TIPO_CLASE`;
DELIMITER $$
USE `roducdb` $$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_TIPO_CLASE` BEFORE INSERT ON `roducweb_tipo_clase` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
		accion,
		datos_viejos,
		datos_nuevos,
		usuario,
		fecha
	)
	VALUES(
		'Tipo Clase',
		'I',
		NULL,
		CONCAT('Codigo: ', (SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'roducdb' AND TABLE_NAME = 'roducweb_tipo_clase'), '| Descripcion:', NEW.descripcion, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha),
		NEW.alta_usuario,
		NOW()
	);
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_TIPO_CLASE`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_TIPO_CLASE` BEFORE UPDATE ON `roducweb_tipo_clase` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Tipo Clase',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
		CONCAT('Codigo: ', OLD.cod_tipo_clase, '| Descripcion: ', OLD.descripcion, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha),
		CONCAT('Codigo: ', NEW.cod_tipo_clase, '| Descripcion: ', NEW.descripcion,'| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA UNIDAD_APRENDIZAJE*/
DROP TRIGGER IF EXISTS `roducdb`. `AUDITORIA_INSERT_UNIDAD_APRENDIZAJE`;
DELIMITER $$
USE `roducdb` $$
CREATE TRIGGER `roducdb`.`AUDITORIA_INSERT_UNIDAD_APRENDIZAJE` BEFORE INSERT ON `roducweb_unidad_aprendizaje` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
		accion,
		datos_viejos,
		datos_nuevos,
		usuario,
		fecha
	)
	VALUES(
		'Unidad Aprendizaje',
		'I',
		NULL,
		CONCAT('Codigo: ', (SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'roducdb' AND TABLE_NAME = 'roducweb_unidad_aprendizaje'), '| Descripcion:', NEW.descripcion, '| Asignatura: ', NEW.cod_asignatura_id, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha),
		NEW.alta_usuario,
		NOW()
	);
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_UNIDAD_APRENDIZAJE`;
DELIMITER $$
USE `roducdb`$$
CREATE TRIGGER `roducdb`.`AUDITORIA_UPDATE_UNIDAD_APRENDIZAJE` BEFORE UPDATE ON `roducweb_unidad_aprendizaje` FOR EACH ROW
BEGIN
	INSERT INTO roducweb_auditoria(
		tabla,
        accion,
        datos_viejos,
        datos_nuevos,
        usuario,
        fecha
    )
    VALUES(
		'Unidad Aprendizaje',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
		CONCAT('Codigo: ', OLD.cod_unidad_aprendizaje, '| Descripcion: ', OLD.descripcion, '| Carrera: ', OLD.cod_asignatura_id, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha),
		CONCAT('Codigo: ', NEW.cod_unidad_aprendizaje, '| Descripcion: ', NEW.descripcion, '| Carrera: ', NEW.cod_asignatura_id, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/