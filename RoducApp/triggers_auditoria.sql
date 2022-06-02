/*AUDITORIA ASIGNATURAS*/
--INSERT--
DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_INSERT_ASIGNATURA`;
DELIMITER $$
USE `roducdb`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `AUDITORIA_INSERT_ASIGNATURA` BEFORE INSERT ON `roducweb_asignatura` FOR EACH ROW BEGIN
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

--UPDATE OR DELETE--
DROP TRIGGER IF EXISTS `roducdb`.`AUDITORIA_UPDATE_ASIGNATURA`;
DELIMITER $$
USE `roducdb`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `AUDITORIA_UPDATE_ASIGNATURA` BEFORE UPDATE ON `roducweb_asignatura` FOR EACH ROW BEGIN
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

/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

/*AUDITORIA ASIGNATURA_USUARIO*/
--INSERT--
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

--UPDATE OR DELETE--
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
    VALUE(
		'Asignatura_Usuario',
        (IF(NEW.estado = 0 AND OLD.estado = 1, 'D', 'U')),
        CONCAT('Codigo: ', OLD.cod_asignatura_usuario, '| Estado: ', OLD.estado, '| Usuario Alta: ', OLD.alta_usuario, '| Fecha Alta: ', OLD.alta_fecha, '| Modif. Usuario: ', OLD.modif_usuario, '| Modif. Fecha: ', OLD.modif_fecha, '| Rol:', OLD.cod_usuario_rol_id, '| Asignatura: ', OLD.cod_asignatura_id),
		CONCAT('Codigo: ', NEW.cod_asignatura_usuario, '| Estado: ', NEW.estado, '| Usuario Alta: ', NEW.alta_usuario, '| Fecha Alta: ', NEW.alta_fecha, '| Modif. Usuario: ', NEW.modif_usuario, '| Modif. Fecha: ', NEW.modif_fecha, '| Rol:', NEW.cod_usuario_rol_id, '| Asignatura: ', NEW.cod_asignatura_id),
        NEW.modif_usuario,
        NOW()
    );
END$$
DELIMITER ;

/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
