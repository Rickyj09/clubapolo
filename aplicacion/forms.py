from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField,\
    TextAreaField, SelectField, PasswordField
from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FileField, SelectField,RadioField
from wtforms import FloatField
from wtforms.validators import DataRequired, Email, Length, ValidationError,AnyOf
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField, FileRequired
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required

def validar_obvio(form,field):
    if field.data=="12345678":
        raise ValidationError('La clave debe ser más segura!!')

class Publicaciones(FlaskForm):
    post = TextAreaField('Notas de las fotos', validators=[
        DataRequired(), Length(min=1, max=140)
    ])
    imagen = FileField('image')
 
    submit = SubmitField('Subir')

class FormArticulo(FlaskForm):
    nombre = StringField("Nombre:",
                         validators=[Required("Tienes que introducir el dato")]
                         )
    precio = DecimalField("Precio:", default=0,
                          validators=[Required("Tienes que introducir el dato")
                                      ])
    iva = IntegerField("IVA:", default=21,
                       validators=[Required("Tienes que introducir el dato")])
    descripcion = TextAreaField("Descripción:")
    photo = FileField('Selecciona imagen:')
    stock = IntegerField("Stock:", default=1,
                         validators=[Required("Tienes que introducir el dato")]
                         )
    CategoriaId = SelectField("Categoría:", coerce=int)
    submit = SubmitField('Enviar')

class FormSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')



class buscapac(FlaskForm):
    iden = IntegerField('Cédula Pasaporte', validators=[DataRequired(),Length(min=10,max=14)], render_kw={"placeholder": "Identificación"})
    submit = SubmitField('Buscar')




class LoginForm(FlaskForm):
    username = StringField('User', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Entrar')


class FormUsuario(FlaskForm):
    username = StringField('Login', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    nombre = StringField('Nombre completo')
    email = EmailField('Email')
    submit = SubmitField('Aceptar')


class alumno(FlaskForm):
    iden = StringField('Cédula Pasaporte', validators=[DataRequired()],render_kw={"placeholder": "Identificación"})
    tipo_iden  = SelectField('Tipo Identificación',choices=[('C', 'Cédula'), ('P', 'Pasaporte'),('R', 'Ruc')],default = 'C',render_kw={}, id='tipo_iden')
    apellido1 = StringField('Apellido Paterno', validators=[DataRequired()])
    apellido2 = StringField('Apellido Materno', validators=[DataRequired()])
    nombres = StringField('Nombres', validators=[DataRequired()])
    est_civil = SelectField('Estado Civil',choices=[('S', 'Soltero'), ('C', 'Casado'),('D', 'Divorciado'),('V', 'Viudo')],default = 'C',render_kw={}, id='est_civil')
    fec_nac = DateField('Fecha de Nacimiento', validators=[DataRequired()],render_kw={"placeholder": "Fecha de Nacimiento"})
    fec_ingreso = DateField('Fecha de Ingreso', validators=[],render_kw={"placeholder": "Fecha de Ingreso"})
    sexo  = SelectField('Genero',choices=[('M', 'Masculino'), ('F', 'Femenino'),('N', 'No Identificado')],default = 'C',render_kw={}, id='sexo')
    direccion = StringField('Dirección', validators=[])
    ocupacion = StringField('Ocupación', validators=[])
    tipo_s = StringField('Tipo de Sangre', validators=[])
    Nivel_edu = StringField('Nivel Educación', validators=[])
    telefono1 = StringField('Teléfono Domicilio', validators=[])
    telefono2 = StringField('Teléfono Movil', validators=[])
    status = SelectField('Status',choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')],default = 'Activo',render_kw={}, id='status')
    email = EmailField('Email')
    cinturon = StringField('Cinturón', validators=[])
    horario = SelectField('Horario',choices=[('1', '09:00-10:30'), ('2', '15:30-17:00'),('3', '17:00-18:30'),('4', '18:30-20:00')],default = '',render_kw={}, id='horario')
    peso = StringField('Peso Kg', validators=[])
    estatura = StringField('Estatura cm', validators=[])
    flexibilidad = StringField('Nivel de flexibilidad', validators=[])
       
    submit = SubmitField('Enviar')


class datos_alumno(FlaskForm):
    iden = StringField('Cédula Pasaporte', validators=[DataRequired()],render_kw={"placeholder": "Identificación"})
    cinturon = StringField('Cinturón', validators=[])
    peso = StringField('Peso Kg', validators=[])
    estatura = StringField('Estatura cm', validators=[])
    flexibilidad = StringField('Nivel de flexibilidad', validators=[])
       
    submit = SubmitField('Enviar')

class campeonato(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    puntua = SelectField('Es Puntuable',choices=[('S', 'Si'), ('N', 'No'),],default = 'C',render_kw={}, id='est_civil')
    fecha = DateField('Fecha del evento', validators=[DataRequired()],render_kw={"placeholder": "Fecha del evento"})
    obs  = StringField('Observacones',validators=[])
       
    submit = SubmitField('Enviar')

class campeonato_combate(FlaskForm):
    iden = IntegerField('Identificación', validators=[DataRequired()])
    nombre = StringField('Nombre del Campeonato', validators=[DataRequired()])
    puntua = SelectField('Es Puntuable',choices=[('S', 'Si'), ('N', 'No'),],default = 'C',render_kw={}, id='est_civil')
    fecha = DateField('Fecha del evento', validators=[DataRequired()],render_kw={"placeholder": "Fecha del evento"})
    ubicacion = SelectField('Medalla Obtenida',choices=[('Oro', 'Oro'), ('Plata', 'Plata'),('Bronce', 'Bronce'), ('Cuarto', 'Cuarto'),('Sin Podio', 'Sin Podio')],default = '',render_kw={}, id='medalla')
    cinturon = StringField('Cinturon', validators=[DataRequired()])
    edad = StringField('Edad', validators=[DataRequired()])
    peso = StringField('Peso', validators=[DataRequired()])
    num_part = IntegerField('Número de participantes', validators=[DataRequired()],render_kw={"placeholder": ""})
    obs  = StringField('Observacones',validators=[])
       
    submit = SubmitField('Enviar')


class campeonato_pommse(FlaskForm):
    iden = IntegerField('Identificación', validators=[DataRequired()])
    nombre = StringField('Nombre del Campeonato', validators=[DataRequired()])
    puntua = SelectField('Es Puntuable',choices=[('S', 'Si'), ('N', 'No'),],default = 'C',render_kw={}, id='est_civil')
    fecha = DateField('Fecha del evento', validators=[DataRequired()],render_kw={"placeholder": "Fecha del evento"})
    ubicacion = SelectField('Medalla Obtenida',choices=[('Oro', 'Oro'), ('Plata', 'Plata'),('Bronce', 'Bronce'),('Cuarto', 'Cuarto'),('Sin Podio', 'Sin Podio')],default = '',render_kw={}, id='medalla')
    cinturon = StringField('Cinturon', validators=[DataRequired()])
    edad = StringField('Edad', validators=[DataRequired()])
    num_part = IntegerField('Número de participantes', validators=[DataRequired()],render_kw={"placeholder": ""})
    obs  = StringField('Observacones',validators=[])
       
    submit = SubmitField('Enviar')

class fechas(FlaskForm):
    fec_ini = DateField('Fecha de Inicio', validators=[DataRequired()],render_kw={"placeholder": "Fecha Inicio"})
    fec_fin = DateField('Fecha de Final', validators=[DataRequired()],render_kw={"placeholder": "Fecha Final"})
    iden = StringField('Cédula Pasaporte', validators=[],render_kw={"placeholder": "Identificación"})
    apellidos = StringField('Apellidos', validators=[])

   
    submit = SubmitField('Enviar')


class FormChangePassword(FlaskForm):
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Aceptar')


class UploadForm(FlaskForm):
    photo = FileField('selecciona imagen:',validators=[FileRequired()])
    submit = SubmitField('Submit')


class horario_ent(FlaskForm):
    iden = IntegerField('Identificación', validators=[DataRequired()])
    horario = SelectField('Horario',choices=[('1', '09:00-10:30'), ('2', '15:30-17:00'),('3', '17:00-18:30'),('4', '18:30-20:00')],default = '',render_kw={}, id='horario')

    submit = SubmitField('Submit')