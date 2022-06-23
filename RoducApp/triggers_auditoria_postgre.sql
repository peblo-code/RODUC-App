/*                      ASIGNATURA                        */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_ASIGNATURA() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Asignatura';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_asignatura      || '|' ||
                    OLD.descripcion         || '|' ||
                    OLD.horas_catedra       || '|' ||
                    OLD.curso               || '|' ||
                    OLD.estado              || '|' ||
                    OLD.alta_usuario        || '|' ||
                    OLD.alta_fecha          || '|' ||
                    OLD.modif_usuario       || '|' ||
                    OLD.modif_fecha         || '|' ||
                    OLD.cod_carrera_id      || '|' ||
                    OLD.cod_plan_estudio_id || '|' ||
                    OLD.cod_semestre_id     || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_asignatura      || '|' ||
                    NEW.descripcion         || '|' ||
                    NEW.horas_catedra       || '|' ||
                    NEW.curso               || '|' ||
                    NEW.estado              || '|' ||
                    NEW.alta_usuario        || '|' ||
                    NEW.alta_fecha          || '|' ||
                    NEW.modif_usuario       || '|' ||
                    NEW.modif_fecha         || '|' ||
                    NEW.cod_carrera_id      || '|' ||
                    NEW.cod_plan_estudio_id || '|' ||
                    NEW.cod_semestre_id     || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE OR REPLACE TRIGGER AUDITORIA_ASIGNATURA
    AFTER INSERT OR UPDATE ON "RoducWeb_asignatura"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_ASIGNATURA();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                    ASIGNATURA_USUARIO                  */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_ASIGNATURA_USUARIO() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Asignatura_Usuario';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_asignatura_usuario      || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' ||
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|' ||
                    OLD.cod_asignatura_id           || '|' ||
                    OLD.cod_usuario_rol_id          || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_asignatura_usuario      || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' ||
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|' ||
                    NEW.cod_asignatura_id           || '|' ||
                    NEW.cod_usuario_rol_id          || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_ASIGNATURA_USUARIO
    AFTER INSERT OR UPDATE ON "RoducWeb_asignatura_usuario"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_ASIGNATURA_USUARIO();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  USUARIOS                              */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_USUARIO() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Usuario';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_usuario             || '|' ||
                    OLD.nombre_usuario          || '|' ||
                    OLD.contraseña              || '|' ||
                    OLD.nombres_del_usuario     || '|' ||
                    OLD.apellidos_del_usuario   || '|' ||
                    OLD.direccion_email         || '|' ||
                    OLD.estado                  || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|'; 
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_usuario             || '|' ||
                    NEW.nombre_usuario          || '|' ||
                    NEW.contraseña              || '|' ||
                    NEW.nombres_del_usuario     || '|' ||
                    NEW.apellidos_del_usuario   || '|' ||
                    NEW.direccion_email         || '|' ||
                    NEW.estado                  || '|' ||
                    NEW.alta_usuario            || '|' || 
                    NEW.alta_fecha              || '|' ||
                    NEW.modif_usuario           || '|' ||
                    NEW.modif_fecha             || '|'; 
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_USUARIO
    AFTER INSERT OR UPDATE ON "RoducWeb_usuario"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_USUARIO();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  FACULTAD                              */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_FACULTAD() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Facultad';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_facultad            || '|' ||
                    OLD.descripcion             || '|' ||
                    OLD.fecha_fundacion         || '|' ||
                    OLD.estado                  || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|'; 
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_facultad            || '|' ||
                    NEW.descripcion             || '|' ||
                    NEW.fecha_fundacion         || '|' ||
                    NEW.estado                  || '|' ||
                    NEW.alta_usuario            || '|' || 
                    NEW.alta_fecha              || '|' ||
                    NEW.modif_usuario           || '|' ||
                    NEW.modif_fecha             || '|'; 
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_FACULTAD
    AFTER INSERT OR UPDATE ON "RoducWeb_facultad"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_FACULTAD();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  CARRERA                               */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_CARRERA() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Carrera';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_carrera             || '|' ||
                    OLD.descripcion             || '|' ||
                    OLD.duracion                || '|' ||
                    OLD.titulo_obtenido         || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|' || 
                    OLD.cod_facultad_id         || '|' ||
                    OLD.estado                  || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_carrera             || '|' ||
                    NEW.descripcion             || '|' ||
                    NEW.duracion                || '|' ||
                    NEW.titulo_obtenido         || '|' ||
                    NEW.alta_usuario            || '|' || 
                    NEW.alta_fecha              || '|' ||
                    NEW.modif_usuario           || '|' ||
                    NEW.modif_fecha             || '|' || 
                    NEW.cod_facultad_id         || '|' ||
                    NEW.estado                  || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_CARRERA
    AFTER INSERT OR UPDATE ON "RoducWeb_carrera"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_CARRERA();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  SEMESTRE                              */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_SEMESTRE() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Semestre';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_semestre            || '|' ||
                    OLD.descripcion             || '|' ||
                    OLD.estado                  || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|' || 
                    OLD.fecha_inicio            || '|' ||
                    OLD.fecha_fin               || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_semestre            || '|' ||
                    NEW.descripcion             || '|' ||
                    NEW.estado                  || '|' ||
                    NEW.alta_usuario            || '|' || 
                    NEW.alta_fecha              || '|' ||
                    NEW.modif_usuario           || '|' ||
                    NEW.modif_fecha             || '|' || 
                    NEW.fecha_inicio            || '|' ||
                    NEW.fecha_fin               || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_SEMESTRE
    AFTER INSERT OR UPDATE ON "RoducWeb_semestre"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_SEMESTRE();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  PLAN ESTUDIO                          */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_PLAN_ESTUDIO() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Plan_Estudio';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_plan_estudio        || '|' ||
                    OLD.descripcion             || '|' ||
                    OLD.estado                  || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|' || 
                    OLD.cod_carrera_id          || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_plan_estudio        || '|' ||
                    NEW.descripcion             || '|' ||
                    NEW.estado                  || '|' ||
                    NEW.alta_usuario            || '|' || 
                    NEW.alta_fecha              || '|' ||
                    NEW.modif_usuario           || '|' ||
                    NEW.modif_fecha             || '|' || 
                    NEW.cod_carrera_id          || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_PLAN_ESTUDIO
    AFTER INSERT OR UPDATE ON "RoducWeb_plan_estudio"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_PLAN_ESTUDIO();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  USUARIO_ROL                          */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_USUARIO_ROL() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Usuario_Rol';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_usuario_rol         || '|' ||
                    OLD.estado                  || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|' || 
                    OLD.cod_rol_usuario_id      || '|' ||
                    OLD.cod_usuario_id          || '|' ||
                    OLD.cod_carrera_id          || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := OLD.cod_usuario_rol         || '|' ||
                    OLD.estado                  || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|' || 
                    OLD.cod_rol_usuario_id      || '|' ||
                    OLD.cod_usuario_id          || '|' ||
                    OLD.cod_carrera_id          || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_USUARIO_ROL
    AFTER INSERT OR UPDATE ON "RoducWeb_usuario_rol"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_USUARIO_ROL();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  TIPO_CLASE                          */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_TIPO_CLASE() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Tipo_Clase';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.tipo_clase              || '|' ||
                    OLD.descripcion             || '|' ||
                    OLD.estado                  || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|'; 
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.tipo_clase              || '|' ||
                    NEW.descripcion             || '|' ||
                    NEW.estado                  || '|' ||
                    NEW.alta_usuario            || '|' || 
                    NEW.alta_fecha              || '|' ||
                    NEW.modif_usuario           || '|' ||
                    NEW.modif_fecha             || '|'; 
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_TIPO_CLASE
    AFTER INSERT OR UPDATE ON "RoducWeb_tipo_clase"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_TIPO_CLASE();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  UNIDAD_APRENDIZAJE                    */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_UNIDAD_APRENDIZAJE() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Unidad_Aprendizaje';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_unidad_aprendizaje  || '|' ||
                    OLD.numero_unidad           || '|' ||
                    OLD.descripcion             || '|' ||
                    OLD.estado                  || '|' ||
                    OLD.alta_usuario            || '|' || 
                    OLD.alta_fecha              || '|' ||
                    OLD.modif_usuario           || '|' ||
                    OLD.modif_fecha             || '|' ||
                    OLD.cod_asignatura_id       || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_unidad_aprendizaje  || '|' ||
                    NEW.numero_unidad           || '|' ||
                    NEW.descripcion             || '|' ||
                    NEW.estado                  || '|' ||
                    NEW.alta_usuario            || '|' || 
                    NEW.alta_fecha              || '|' ||
                    NEW.modif_usuario           || '|' ||
                    NEW.modif_fecha             || '|' ||
                    NEW.cod_asignatura_id       || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_UNIDAD_APRENDIZAJE
    AFTER INSERT OR UPDATE ON "RoducWeb_unidad_aprendizaje"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_UNIDAD_APRENDIZAJE();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  CONTENIDO                             */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_CONTENIDO() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Contenido';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_contenido               || '|' ||
                    OLD.descripcion                 || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' || 
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|' || 
                    OLD.cod_unidad_aprendizaje_id   || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_contenido               || '|' ||
                    NEW.descripcion                 || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' || 
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|' || 
                    NEW.cod_unidad_aprendizaje_id   || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_CONTENIDO
    AFTER INSERT OR UPDATE ON "RoducWeb_contenido"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_CONTENIDO();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  INSTRUMENTO EVALUACION                */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_INSTRUMENTO_EVALUACION() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Instrumento_evaluacion';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_instrumento_evaluacion  || '|' ||
                    OLD.descripcion                 || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' || 
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|'; 
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_instrumento_evaluacion  || '|' ||
                    NEW.descripcion                 || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' || 
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_INSTRUMENTO_EVALUACION
    AFTER INSERT OR UPDATE ON "RoducWeb_instrumento_evaluacion"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_INSTRUMENTO_EVALUACION();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  METODOLOGIA ENSEÑANZA                 */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_METODOLOGIA_ENSEÑANZA() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Metodologia_Enseñanza';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_metodologia_enseñanza   || '|' ||
                    OLD.descripcion                 || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' || 
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|'; 
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_metodologia_enseñanza   || '|' ||
                    NEW.descripcion                 || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' || 
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_METODOLOGIA_ENSEÑANZA
    AFTER INSERT OR UPDATE ON "RoducWeb_metodologia_enseñanza"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_METODOLOGIA_ENSEÑANZA();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  RECURSO AUXILIAR                      */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_RECURSO_AUXILIAR() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Recurso_Auxiliar';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_recurso_auxiliar        || '|' ||
                    OLD.descripcion                 || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' || 
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|'; 
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_recurso_auxiliar        || '|' ||
                    NEW.descripcion                 || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' || 
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_RECURSO_AUXILIAR
    AFTER INSERT OR UPDATE ON "RoducWeb_recursos_auxiliar"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_RECURSO_AUXILIAR();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  TIPO EVALUACION                       */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_TIPO_EVA() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Tipo_Eva';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_tipo_eva                || '|' ||
                    OLD.descripcion                 || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' || 
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|'; 
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_tipo_eva                || '|' ||
                    NEW.descripcion                 || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' || 
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_TIPO_EVA
    AFTER INSERT OR UPDATE ON "RoducWeb_tipo_eva"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_TIPO_EVA();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                  TRABAJO AUTONOMO                      */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_TRABAJO_AUTONOMO() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    V_TABLA      VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DE LA TABLA DENTRO DE LA DB
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)	   default NULL;
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Trabajo_Autonomo';
   /*--------------------- ACCION PARA UPDATE O DELETE --------------------------*/
   IF (NEW.estado = 0 AND OLD.estado = 1) THEN 
  		V_ACCION := 'D';
   ELSE 
  		V_ACCION := 'U';
   END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_trabajo_autonomo                || '|' ||
                    OLD.descripcion                 || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' || 
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|'; 
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_trabajo_autonomo                || '|' ||
                    NEW.descripcion                 || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' || 
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

    /*------------------ CREACION DE TRIGGER -----------------*/
CREATE TRIGGER AUDITORIA_TRABAJO_AUTONOMO
    AFTER INSERT OR UPDATE ON "RoducWeb_trabajo_autonomo"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_TRABAJO_AUTONOMO();
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
    /*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_CABECERA_PLANILLA() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)    DEFAULT NULL;    -- ACCION EN CASO DE UPDATE O DELETE
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Cabecera_Planilla';
    /*-------------------- SETEO DE ACCION -------------------*/
    IF (NEW.estado = 0 AND OLD.estado = 1) THEN
        V_ACCION := 'D';
    ELSE
        V_ACCION := 'U';
    END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_cabecera_planilla       || '|' ||
                    OLD.cod_tipo_clase_id           || '|' ||
                    OLD.cod_asignatura_id           || '|' ||
                    OLD.cod_usuario_id              || '|' ||
                    OLD.fecha_clase                 || '|' ||
                    OLD.hora_entrada                || '|' ||
                    OLD.hora_salida                 || '|' ||
                    OLD.fecha_vencimiento           || '|' ||
                    OLD.evaluacion                  || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' ||
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_cabecera_planilla       || '|' ||
                    NEW.cod_tipo_clase_id           || '|' ||
                    NEW.cod_asignatura_id           || '|' ||
                    NEW.cod_usuario_id              || '|' ||
                    NEW.fecha_clase                 || '|' ||
                    NEW.hora_entrada                || '|' ||
                    NEW.hora_salida                 || '|' ||
                    NEW.fecha_vencimiento           || '|' ||
                    NEW.evaluacion                  || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' ||
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';
/*-------------------- CREACION DE TRIGGER -------------------*/
CREATE OR REPLACE TRIGGER AUDITORIA_CABECERA_PLANILLA
    AFTER INSERT OR UPDATE ON "RoducWeb_cabecera_planilla"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_CABECERA_PLANILLA();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*              CONTENIDOS DADOS                              */
/*------------- CREACION DE LA FUNCION A EJECUTAR ------------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_CONTENIDOS_DADOS() 
RETURNS TRIGGER AS 
$BODY$
    /*------------ DECLARACION DE VARIABLES A USAR -----------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)    DEFAULT NULL;    -- ACCION EN CASO DE UPDATE O DELETE
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Contenidos_Dados';
    /*-------------------- SETEO DE ACCION -------------------*/
    IF (NEW.estado = 0 AND OLD.estado = 1) THEN
        V_ACCION := 'D';
    ELSE
        V_ACCION := 'U';
    END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_contenidos_dados        || '|' ||
                    OLD.cod_cabecera_planilla_id    || '|' ||
                    OLD.cod_contenido_id            || '|' ||
                    OLD.estado                      || '|' ||
                    OLD.alta_usuario                || '|' ||
                    OLD.alta_fecha                  || '|' ||
                    OLD.modif_usuario               || '|' ||
                    OLD.modif_fecha                 || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_contenidos_dados        || '|' ||
                    NEW.cod_cabecera_planilla_id    || '|' ||
                    NEW.cod_contenido_id            || '|' ||
                    NEW.estado                      || '|' ||
                    NEW.alta_usuario                || '|' ||
                    NEW.alta_fecha                  || '|' ||
                    NEW.modif_usuario               || '|' ||
                    NEW.modif_fecha                 || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';
/*-------------------- CREACION DE TRIGGER -------------------*/
CREATE OR REPLACE TRIGGER AUDITORIA_CONTENIDOS_DADOS
    AFTER INSERT OR UPDATE ON "RoducWeb_contenidos_dados"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_CONTENIDOS_DADOS();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*              EVALUACIONES                                  */
/*------------- CREACION DE LA FUNCION A EJECUTAR ------------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_EVALUACIONES() 
RETURNS TRIGGER AS 
$BODY$
/*-------------- DECLARACION DE VARIABLES A USAR -------------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)    DEFAULT NULL;    -- ACCION EN CASO DE UPDATE O DELETE
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Evaluaciones';
    /*-------------------- SETEO DE ACCION -------------------*/
    IF (NEW.estado = 0 AND OLD.estado = 1) THEN
        V_ACCION := 'D';
    ELSE
        V_ACCION := 'U';
    END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_evaluacion                  || '|' ||
                    OLD.cod_cabecera_planilla_id        || '|' ||
                    OLD.cod_instrumento_evaluacion_id   || '|' ||
                    OLD.cod_tipo_eva_id                 || '|' ||
                    OLD.estado                          || '|' ||
                    OLD.alta_usuario                    || '|' ||
                    OLD.alta_fecha                      || '|' ||
                    OLD.modif_usuario                   || '|' ||
                    OLD.modif_fecha                     || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_evaluacion                  || '|' ||
                    NEW.cod_cabecera_planilla_id        || '|' ||
                    NEW.cod_instrumento_evaluacion_id   || '|' ||
                    NEW.cod_tipo_eva_id                 || '|' ||
                    NEW.estado                          || '|' ||
                    NEW.alta_usuario                    || '|' ||
                    NEW.alta_fecha                      || '|' ||
                    NEW.modif_usuario                   || '|' ||
                    NEW.modif_fecha                     || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';
/*-------------------- CREACION DE TRIGGER -------------------*/
CREATE OR REPLACE TRIGGER AUDITORIA_EVALUACIONES
    AFTER INSERT OR UPDATE ON "RoducWeb_evaluaciones"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_EVALUACIONES();


/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*              TRABAJOS UTILIZADOS                           */
/*------------- CREACION DE LA FUNCION A EJECUTAR ------------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_TRABAJOS_UTILIZADOS() 
RETURNS TRIGGER AS 
$BODY$
/*-------------- DECLARACION DE VARIABLES A USAR -------------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)    DEFAULT NULL;    -- ACCION EN CASO DE UPDATE O DELETE
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Trabajos_Utilizados';
    /*-------------------- SETEO DE ACCION -------------------*/
    IF (NEW.estado = 0 AND OLD.estado = 1) THEN
        V_ACCION := 'D';
    ELSE
        V_ACCION := 'U';
    END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_trabajos_utilizados         || '|' ||
                    OLD.cod_cabecera_planilla_id        || '|' ||
                    OLD.cod_trabajo_autonomo_id         || '|' ||
                    OLD.estado                          || '|' ||
                    OLD.alta_usuario                    || '|' ||
                    OLD.alta_fecha                      || '|' ||
                    OLD.modif_usuario                   || '|' ||
                    OLD.modif_fecha                     || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_trabajos_utilizados         || '|' ||
                    NEW.cod_cabecera_planilla_id        || '|' ||
                    NEW.cod_trabajo_autonomo_id         || '|' ||
                    NEW.estado                          || '|' ||
                    NEW.alta_usuario                    || '|' ||
                    NEW.alta_fecha                      || '|' ||
                    NEW.modif_usuario                   || '|' ||
                    NEW.modif_fecha                     || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';
/*-------------------- CREACION DE TRIGGER -------------------*/
CREATE OR REPLACE TRIGGER AUDITORIA_TRABAJOS_UTILIZADOS
    AFTER INSERT OR UPDATE ON "RoducWeb_trabajos_utilizados"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_TRABAJOS_UTILIZADOS();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*              METODOLOGIA UTILIZADA                         */
/*------------- CREACION DE LA FUNCION A EJECUTAR ------------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_METODOLOGIA_UTILIZADA() 
RETURNS TRIGGER AS 
$BODY$
/*-------------- DECLARACION DE VARIABLES A USAR -------------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)    DEFAULT NULL;    -- ACCION EN CASO DE UPDATE O DELETE
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Metodologia_Utilizada';
    /*-------------------- SETEO DE ACCION -------------------*/
    IF (NEW.estado = 0 AND OLD.estado = 1) THEN
        V_ACCION := 'D';
    ELSE
        V_ACCION := 'U';
    END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_metodologia_utilizada       || '|' ||
                    OLD.cod_cabecera_planilla_id        || '|' ||
                    OLD.cod_metodologia_enseñanza_id        || '|' ||
                    OLD.estado                          || '|' ||
                    OLD.alta_usuario                    || '|' ||
                    OLD.alta_fecha                      || '|' ||
                    OLD.modif_usuario                   || '|' ||
                    OLD.modif_fecha                     || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_metodologia_utilizada       || '|' ||
                    NEW.cod_cabecera_planilla_id        || '|' ||
                    NEW.cod_metodologia_enseñanza_id        || '|' ||
                    NEW.estado                          || '|' ||
                    NEW.alta_usuario                    || '|' ||
                    NEW.alta_fecha                      || '|' ||
                    NEW.modif_usuario                   || '|' ||
                    NEW.modif_fecha                     || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';
/*-------------------- CREACION DE TRIGGER -------------------*/
CREATE OR REPLACE TRIGGER AUDITORIA_METODOLOGIA_UTILIZADA
    AFTER INSERT OR UPDATE ON "RoducWeb_metodologia_utilizada"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_METODOLOGIA_UTILIZADA();

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*              RECURSOS UTILIZADOS                           */
/*------------- CREACION DE LA FUNCION A EJECUTAR ------------*/
CREATE OR REPLACE 
FUNCTION AUDITORIA_RECURSOS_UTILIZADOS() 
RETURNS TRIGGER AS 
$BODY$
/*-------------- DECLARACION DE VARIABLES A USAR -------------*/
DECLARE
    V_MODULO     VARCHAR(300)  DEFAULT NULL;    -- NOMBRE DEL MODULO QUE SE AUDITA
    DATOS_VIEJOS VARCHAR(5000) DEFAULT NULL;    -- DATOS VIEJOS DEL REGISTRO   
    DATOS_NUEVOS VARCHAR(5000) DEFAULT NULL;    -- DATOS NUEVOS DEL REGISTRO
    V_ACCION     VARCHAR(1)    DEFAULT NULL;    -- ACCION EN CASO DE UPDATE O DELETE
BEGIN
    /*-------------------- MODULO Y TABLA --------------------*/
    V_MODULO := 'Recursos_Utilizados';
    /*-------------------- SETEO DE ACCION -------------------*/
    IF (NEW.estado = 0 AND OLD.estado = 1) THEN
        V_ACCION := 'D';
    ELSE
        V_ACCION := 'U';
    END IF;
    /*------------- IGUALACION DE DATOS VIEJOS ---------------*/
    DATOS_VIEJOS := OLD.cod_recursos_utilizados         || '|' ||
                    OLD.cod_cabecera_planilla_id        || '|' ||
                    OLD.cod_recurso_auxiliar_id             || '|' ||
                    OLD.estado                          || '|' ||
                    OLD.alta_usuario                    || '|' ||
                    OLD.alta_fecha                      || '|' ||
                    OLD.modif_usuario                   || '|' ||
                    OLD.modif_fecha                     || '|';
    /*-------------- IGUALACION DE DATOS NUEVOS --------------*/
    DATOS_NUEVOS := NEW.cod_recursos_utilizados         || '|' ||
                    NEW.cod_cabecera_planilla_id        || '|' ||
                    NEW.cod_recurso_auxiliar_id             || '|' ||
                    NEW.estado                          || '|' ||
                    NEW.alta_usuario                    || '|' ||
                    NEW.alta_fecha                      || '|' ||
                    NEW.modif_usuario                   || '|' ||
                    NEW.modif_fecha                     || '|';
    /*----------------- INSERCION A LA TABLA -----------------*/
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            'I',
            NULL,
            DATOS_NUEVOS,
            NEW.alta_usuario,
            NOW()
        );
    END IF;
    /*-------------- ACTUALIZACION O ELIMINACION -------------*/
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO "RoducWeb_auditoria"(
            tabla,
            accion,
            datos_viejos,
            datos_nuevos,
            usuario,
            fecha
        )
        VALUES(
            V_MODULO,
            V_ACCION,
            DATOS_VIEJOS,
            DATOS_NUEVOS,
            NEW.modif_usuario,
            NOW()
        );
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';
/*-------------------- CREACION DE TRIGGER -------------------*/
CREATE OR REPLACE TRIGGER AUDITORIA_RECURSOS_UTILIZADOS
    AFTER INSERT OR UPDATE ON "RoducWeb_recursos_utilizados"
    FOR EACH ROW
    EXECUTE PROCEDURE AUDITORIA_RECURSOS_UTILIZADOS();

/*--------------------------------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------------*/

/*                 ELIMINACION DE DETALLE                 */
/*----------- CREACION DE LA FUNCION A EJECUTAR ----------*/
CREATE OR REPLACE 
FUNCTION ELIMINAR_DETALLE() 
RETURNS TRIGGER AS 
$BODY$
DECLARE 
    V_COD_CABECERA NUMERIC(5) DEFAULT NULL;
BEGIN
    /*--------------- IGUALACION A VARIABLE --------------*/
    V_COD_CABECERA := NEW.cod_cabecera_planilla;
    /*------- ELIMINACION DE DETALLE DE LA CABECERA ------*/
    IF (TG_OP = 'UPDATE') THEN
        IF (NEW.estado = 0 and OLD.estado = 1) THEN
            IF (NEW.evaluacion = 0) THEN                --SI NO ES EVALUACION
                UPDATE "RoducWeb_contenidos_dados"      --LOS CONTENIDOS QUE SE DIERON PASAN ASOCIADOS A LA CABECERA A ESTADO CERO
                    SET estado              = 0,
                        modif_usuario       = NEW.modif_usuario   
                WHERE cod_cabecera_planilla_id = V_COD_CABECERA;
                UPDATE "RoducWeb_trabajos_utilizados"   --LOS TRABAJOS AUTONOMOS UTILIZADOS ASOCIADOS A LA CABECERA PASAN A ESTADO CERO
                    SET estado              = 0,
                        modif_usuario       = NEW.modif_usuario  
                WHERE cod_cabecera_planilla_id = V_COD_CABECERA;
                UPDATE "RoducWeb_metodologia_utilizada" --LAS METODOLOGIAS UTILIZADAS ASOCIADOS A LA CABECERA PASAN A ESTADO CERO
                    SET estado              = 0,
                        modif_usuario       = NEW.modif_usuario
                WHERE cod_cabecera_planilla_id = V_COD_CABECERA;
                UPDATE "RoducWeb_recursos_utilizados"   --LOS RECURSOS AUXILIARES ASOCIADOS A LA CABECERA PASAN A ESTADO CERO
                    SET estado              = 0,
                        modif_usuario       = NEW.modif_usuario    
                WHERE cod_cabecera_planilla_id = V_COD_CABECERA;
            ELSE                                        --SI ES EVALUACION
                UPDATE "RoducWeb_evaluaciones"          --LAS EVALUACIONES QUE ESTEN ASOCIADOS A LA CABECERA PASAN A ESTADO CERO
                    SET estado              = 0,
                        modif_usuario       = NEW.modif_usuario
                WHERE cod_cabecera_planilla_id = V_COD_CABECERA;
            END IF;
        END IF;
    END IF;
    RETURN NEW;
END;
$BODY$ LANGUAGE 'plpgsql';

/*-------------------- CREACION DE TRIGGER -------------------*/
CREATE OR REPLACE TRIGGER ELIMINAR_DETALLE
    AFTER UPDATE ON "RoducWeb_cabecera_planilla"
    FOR EACH ROW
    EXECUTE PROCEDURE ELIMINAR_DETALLE();