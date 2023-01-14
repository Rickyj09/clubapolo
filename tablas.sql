DROP TABLE alumno;

CREATE TABLE `alumno` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo_iden` VARCHAR(45) NULL ,
  `identificacion` VARCHAR(45) NULL ,
  `nombres` VARCHAR(45) NULL,
  `apellido_p` VARCHAR(45) NULL,
  `apellido_m` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  `fecha_nacimiento` DATE NULL,
  `fecha_ingreso` DATE NULL,
  `est_civil` VARCHAR(45) NULL,
  `telefono1` VARCHAR(45) NULL,
  `telefono2` VARCHAR(45) NULL,
  `mail` VARCHAR(45) NULL,
  `genero` VARCHAR(45) NULL,
  `ocupacion` VARCHAR(45) NULL,
  `tipo_sangre` VARCHAR(45) NULL,
  `nivel_educacion` VARCHAR(45) NULL,
  `status`  VARCHAR(45) NULL,
  `foto` LONGTEXT NULL,
  PRIMARY KEY (`id`))
COMMENT = 'Información de los estudiantes de la academia';

CREATE TABLE `alumno` (
  `identificacion` int NOT NULL,
  `nombres` varchar(45) DEFAULT NULL,
  `apellido_p` varchar(45) DEFAULT NULL,
  `apellido_m` varchar(45) DEFAULT NULL,
  `tipo_iden` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `fecha_ingreso` date DEFAULT NULL,
  `est_civil` varchar(45) DEFAULT NULL,
  `telefono1` varchar(45) DEFAULT NULL,
  `telefono2` varchar(45) DEFAULT NULL,
  `mail` varchar(45) DEFAULT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `ocupacion` varchar(45) DEFAULT NULL,
  `status` blob,
  `foto` longtext,
  `tipo_sangre` varchar(45) DEFAULT NULL,
  `nivel_educacion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`identificacion`)
) COMMENT='Información de los estudiantes de la academia';

ALTER TABLE `apolo`.`alumno` 
CHANGE COLUMN `identificacion` `identificacion` INT NOT NULL AFTER `id`,
DROP PRIMARY KEY,
ADD PRIMARY KEY (`id`, `identificacion`);
;
ALTER TABLE `alumno` 
ADD COLUMN `fecha_log` DATETIME NULL AFTER `nivel_educacion`;


ALTER TABLE `alumno` 
DROP COLUMN `foto`,
CHANGE COLUMN `status` `status` VARCHAR(45) NULL DEFAULT NULL ;


CREATE TABLE `alumno_foto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `iden` INT NULL,
  `foto` LONGTEXT NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `apolo`.`representante` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_alumno` INT NOT NULL,
  `nombres` VARCHAR(45) NULL,
  `apellido_p` VARCHAR(45) NULL,
  `apellido_m` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  `telefono1` VARCHAR(45) NULL,
  `telefono2` VARCHAR(45) NULL,
  `mail` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id))
COMMENT = 'Información de los representantes de los estudiantes de la academia en caso de menores de edad';


DROP TABLE IF EXISTS peso;
CREATE TABLE `peso` (
  `id_alumno` INT NOT NULL,
  `valor_peso` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumno(identificacion))
COMMENT = 'Información del peso estudiantes de la academia';

insert into peso (id_alumno,valor_peso,fecha) VALUES (1,'67',now());

CREATE TABLE `estatura` (
  `id_alumno` INT NOT NULL,
  `valor_estatura` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumno(identificacion))
COMMENT = 'Información del estatura estudiantes de la academia';

insert into estatura (id_alumno,valor_estatura,fecha) VALUES (1,'167',now());

CREATE TABLE `flexibilidad` (
  `id_alumno` INT NOT NULL,
  `valor_flexibilidad` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumno(identificacion))
COMMENT = 'Información del flexibilidad estudiantes de la academia';



CREATE TABLE `horario` (
  `id_alumno` INT NOT NULL,
  `valor_horario` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumno(identificacion))
COMMENT = 'Información del horario estudiantes de la academia';

insert into horario (id_alumno,valor_horario,fecha) VALUES (1,'09:00 - 10:30',now());

CREATE TABLE `cinturon` (
  `id_alumno` INT NOT NULL,
  `color` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumno(identificacion))
COMMENT = 'Información del cinturon estudiantes de la academia';

insert into peso (id_alumno,valor_peso,fecha) VALUES (1753962768,'68','2019-07-28');
insert into peso (id_alumno,valor_peso,fecha) VALUES (1753962768,'68','2020-08-28');
insert into peso (id_alumno,valor_peso,fecha) VALUES (1753962768,'67','2021-02-15');
insert into peso (id_alumno,valor_peso,fecha) VALUES (1753962768,'63','2021-05-20');
insert into peso (id_alumno,valor_peso,fecha) VALUES (1753962768,'59','2021-11-02');

insert into peso (id_alumno,color,fecha) VALUES (1753962768,'amarillo-verde','2019-12-10');
insert into cinturon (id_alumno,color,fecha) VALUES (1753962768,'azul','2020-07-15');
insert into cinturon (id_alumno,color,fecha) VALUES (1753962768,'rojo','2021-12-20');

CREATE TABLE `campeonato` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `puntua` VARCHAR(45) NULL,
  `fecha` DATE NULL,
  `obs` VARCHAR(95) NULL,
  PRIMARY KEY (`id`))
COMMENT = 'Información de los campeonatos en los que participarón los alumnos de la academia';

CREATE TABLE `apolo`.`camp_pommse` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `puntua` VARCHAR(45) NULL,
  `fecha` DATE NULL,
  `id_alumno` INT NOT NULL,
  `ubicacion` VARCHAR(45) NULL,
  `cat_cinturon` VARCHAR(45) NULL,
  `cat_edad` VARCHAR(45) NULL,
  `num_participantes` VARCHAR(45) NULL,
  `obs` VARCHAR(95) NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (id_campeonato) REFERENCES campeonato(id),
  FOREIGN KEY (id_alumno) REFERENCES alumno(identificacion))
COMMENT = 'Información de los campeonatos de pommse en los que participarón los alumnos de la academia';

CREATE TABLE `camp_pommse` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `puntua` varchar(45) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `id_alumno` int NOT NULL,
  `ubicacion` varchar(45) DEFAULT NULL,
  `cat_cinturon` varchar(45) DEFAULT NULL,
  `cat_edad` varchar(45) DEFAULT NULL,
  `num_participantes` varchar(45) DEFAULT NULL,
  `obs` varchar(95) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_alumno` (`id_alumno`),
  CONSTRAINT `camp_pommse_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`identificacion`)
) COMMENT='Información de los campeonatos de pommse en los que participarón los alumnos de la academia';
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO `apolo`.`camp_pommse` (`nombre`, `puntua`, `fecha`, `id_alumno`, `ubicacion`, `cat_cinturon`, `cat_edad`, `num_participantes`) VALUES ('copa1', 'si', '2022-02-12', '1711459816', 'oro', 'negro', '48', '2');
INSERT INTO `apolo`.`camp_pommse` (`nombre`, `puntua`, `fecha`, `id_alumno`, `ubicacion`, `cat_cinturon`, `cat_edad`, `num_participantes`) VALUES ('copa1', 'si', '2022-02-12', '1711459816', 'oro', 'negro', '48', '2');
INSERT INTO `apolo`.`camp_pommse` (`nombre`, `puntua`, `fecha`, `id_alumno`, `ubicacion`, `cat_cinturon`, `cat_edad`, `num_participantes`) VALUES ('copa1', 'si', '2022-02-12', '1711459816', 'oro', 'negro', '48', '2');
INSERT INTO `apolo`.`camp_pommse` (`nombre`, `puntua`, `fecha`, `id_alumno`, `ubicacion`, `cat_cinturon`, `cat_edad`, `num_participantes`) VALUES ('copa1', 'si', '2022-02-12', '1711459816', 'oro', 'negro', '48', '2');



CREATE TABLE `apolo`.`camp_combate` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_alumno` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `puntua` VARCHAR(45) NULL,
  `fecha` DATE NULL,
  `ubicacion` VARCHAR(45) NULL,
  `cat_cinturon` VARCHAR(45) NULL,
  `cat_edad` VARCHAR(45) NULL,
  `cat_peso` VARCHAR(45) NULL,
  `num_participantes` VARCHAR(45) NULL,
  `obs` VARCHAR(95) NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (id_campeonato) REFERENCES campeonato(id),
  FOREIGN KEY (id_alumno) REFERENCES alumno(identificacion))
COMMENT = 'Información de los campeonatos de combate en los que participarón los alumnos de la academia';


CREATE TABLE `camp_combate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_alumno` int NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `puntua` varchar(45) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `ubicacion` varchar(45) DEFAULT NULL,
  `cat_cinturon` varchar(45) DEFAULT NULL,
  `cat_edad` varchar(45) DEFAULT NULL,
  `cat_peso` varchar(45) DEFAULT NULL,
  `num_participantes` varchar(45) DEFAULT NULL,
  `obs` varchar(95) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_alumno` (`id_alumno`),
  CONSTRAINT `camp_combate_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`identificacion`)
) COMMENT='Información de los campeonatos de combate en los que participarón los alumnos de la academia';
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO `apolo`.`camp_combate` (`id_alumno`, `nombre`, `puntua`, `fecha`, `ubicacion`, `cat_cinturon`, `cat_edad`, `cat_peso`, `num_participantes`, `obs`) VALUES ('1711459816', 'copa1', 'si', '2022-01-25', 'oro', 'negro', '48', '79 Kg', '2', 'test1');


CREATE TABLE `apolo`.`cat_edad` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `rango` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
COMMENT = 'Catalogo de categoria por edad';

CREATE TABLE `apolo`.`cat_cinturon` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `rango` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
COMMENT = 'Catalogo de categoria por cinturon`';

CREATE TABLE `apolo`.`cat_peso` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `rango` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
COMMENT = 'Catalogo de categoria por peso';

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password_hash` varchar(128) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

#query para buscar participante 
select * from campeonato a 
inner join camp_combate c
on c.id = a.id
where id_alumno = 2
and num_participantes > 3;

select * from campeonato a 
inner join camp_combate c
on c.id = a.id
where num_participantes > 3;

insert into usuarios (username,password_hash,nombre,email,admin) VALUES ('admin','pbkdf2:sha256:150000$M8kAgKW1$4e0b54f28eda2dbcca8096a22bf022d37f807f707fae7b62315ec6895fe70644','administrador','adm@gmail.com',true);


UPDATE alumno_foto SET iden=1753962768 WHERE id=3;

UPDATE alumno_foto SET foto='16734810465852184358532016283108.jpg' WHERE id=4;

UPDATE alumno_foto SET iden=1720705209 WHERE id=4;