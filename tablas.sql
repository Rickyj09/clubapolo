CREATE TABLE `apolo`.`alumno` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo_iden` VARCHAR(45) NULL ,
  `ident` VARCHAR(45) NULL ,
  `nombres` VARCHAR(45) NULL,
  `apellido_p` VARCHAR(45) NULL,
  `apellido_m` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  `fecha_nacimiento` DATE NULL,
  `fecha_ingreso` DATE NULL,
  `telefono1` VARCHAR(45) NULL,
  `telefono2` VARCHAR(45) NULL,
  `mail` VARCHAR(45) NULL,
  `genero` VARCHAR(45) NULL,
  `ocupacion` VARCHAR(45) NULL,
  `tipo_sangre` VARCHAR(45) NULL,
  `nivel_educacion` VARCHAR(45) NULL,
  `status` BLOB NULL,
  `foto` LONGTEXT NULL,
  PRIMARY KEY (`id`))
COMMENT = 'Información de los estudiantes de la academia';

ALTER TABLE `apolo`.`alumno` 
ADD COLUMN `ocupacion` VARCHAR(45) NULL AFTER `genero`,
ADD COLUMN `tipo_sangre` VARCHAR(45) NULL AFTER `foto`,
ADD COLUMN `nivel_educacion` VARCHAR(45) NULL AFTER `tipo_sangre`,
CHANGE COLUMN `sexo` `genero` VARCHAR(45) NULL DEFAULT NULL ;


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

CREATE TABLE `apolo`.`peso` (
  `id_alumno` INT NOT NULL,
  `valor_peso` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id))
COMMENT = 'Información del peso estudiantes de la academia';

insert into peso (id_alumno,valor_peso,fecha) VALUES (1,'67',now());

CREATE TABLE `apolo`.`estatura` (
  `id_alumno` INT NOT NULL,
  `valor_estatura` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id))
COMMENT = 'Información del estatura estudiantes de la academia';

insert into estatura (id_alumno,valor_estatura,fecha) VALUES (1,'167',now());

CREATE TABLE `apolo`.`flexibilidad` (
  `id_alumno` INT NOT NULL,
  `valor_flexibilidad` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id))
COMMENT = 'Información del flexibilidad estudiantes de la academia';



CREATE TABLE `apolo`.`horario` (
  `id_alumno` INT NOT NULL,
  `valor_horario` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id))
COMMENT = 'Información del horario estudiantes de la academia';

insert into horario (id_alumno,valor_horario,fecha) VALUES (1,'09:00 - 10:30',now());

CREATE TABLE `apolo`.`cinturon` (
  `id_alumno` INT NOT NULL,
  `color` VARCHAR(45) NULL,
  `fecha` VARCHAR(45) NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id))
COMMENT = 'Información del cinturon estudiantes de la academia';

insert into cinturon (id_alumno,color,fecha) VALUES (1,'blanco','2019-07-28');
insert into cinturon (id_alumno,color,fecha) VALUES (1,'amarillo-verde','2019-12-10');
insert into cinturon (id_alumno,color,fecha) VALUES (1,'azul','2020-07-15');
insert into cinturon (id_alumno,color,fecha) VALUES (1,'rojo','2021-12-20');

CREATE TABLE `apolo`.`campeonato` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `puntua` VARCHAR(45) NULL,
  `fecha` DATE NULL,
  `obs` VARCHAR(95) NULL,
  PRIMARY KEY (`id`))
COMMENT = 'Información de los campeonatos en los que participarón los alumnos de la academia';

CREATE TABLE `apolo`.`camp_pommse` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_campeonato` INT(45) NOT NULL,
  `id_alumno` INT NOT NULL,
  `ubicacion` VARCHAR(45) NULL,
  `cat_cinturon` VARCHAR(45) NULL,
  `cat_edad` VARCHAR(45) NULL,
  `num_participantes` VARCHAR(45) NULL,
  `obs` VARCHAR(95) NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (id_campeonato) REFERENCES campeonato(id),
  FOREIGN KEY (id_alumno) REFERENCES alumno(id))
COMMENT = 'Información de los campeonatos de pommse en los que participarón los alumnos de la academia';

CREATE TABLE `apolo`.`camp_combate` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_alumno` INT NOT NULL,
  `id_campeonato` INT NULL,
  `ubicacion` VARCHAR(45) NULL,
  `cat_cinturon` VARCHAR(45) NULL,
  `cat_edad` VARCHAR(45) NULL,
  `cat_peso` VARCHAR(45) NULL,
  `num_participantes` VARCHAR(45) NULL,
  `obs` VARCHAR(95) NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (id_campeonato) REFERENCES campeonato(id),
  FOREIGN KEY (id_alumno) REFERENCES alumno(id))
COMMENT = 'Información de los campeonatos de combate en los que participarón los alumnos de la academia';

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