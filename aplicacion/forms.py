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
    iden = StringField('Cédula Pasaporte', validators=[DataRequired(),Length(min=10,max=14)], render_kw={"placeholder": "Identificación"})
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
    status = StringField('Status', validators=[])
    foto = StringField('Foto', validators=[])
    email = EmailField('Email')
       
    submit = SubmitField('Enviar')


class campeonato(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    puntua = SelectField('Es Puntuable',choices=[('S', 'Si'), ('N', 'No'),],default = 'C',render_kw={}, id='est_civil')
    fecha = DateField('Fecha del evento', validators=[DataRequired()],render_kw={"placeholder": "Fecha del evento"})
    obs  = StringField('Observacones',validators=[])
       
    submit = SubmitField('Enviar')

class fechas(FlaskForm):
    fec_ini = DateField('Fecha de Inicio', validators=[DataRequired()],render_kw={"placeholder": "Fecha Inicio"})
    fec_fin = DateField('Fecha de Final', validators=[DataRequired()],render_kw={"placeholder": "Fecha Final"})
    iden = StringField('Cédula Pasaporte', validators=[],render_kw={"placeholder": "Identificación"})
    apellidos = StringField('Apellidos', validators=[])

   
    submit = SubmitField('Enviar')

class hepaticas(FlaskForm):
    SGOT = StringField('', validators=[],render_kw={"placeholder": "S.G.O.T"})
    SGPT = StringField('', validators=[],render_kw={"placeholder": "S.G.P.T"})
    BILIRRUBIN_TOTAL = StringField('', validators=[],render_kw={"placeholder": "BILIRRUBINA TOTAL"})
    BILIRRUBINA_DIRECTA = StringField('', validators=[],render_kw={"placeholder": "BILIRRUBINA DIRECTA"})
    BILIRRUBINA_INDIRECTA = StringField('',validators=[],render_kw={"placeholder": "BILIRRUBINA INDIRECTA"})
    PROTEINAS_TOTALES = StringField('',validators=[],render_kw={"placeholder": "PROTEINAS TOTALES"})
    AMILASA = StringField('', validators=[],render_kw={"placeholder": "AMILASA"})
    LIPASA =  StringField('', validators=[],render_kw={"placeholder": "LIPASA"})
        
    submit = SubmitField('Enviar')



class pemo(FlaskForm):
    COLOR = StringField('COLOR', validators=[],render_kw={"placeholder": "COLOR"})
    ASPECTO = StringField('ASPECTO', validators=[],render_kw={"placeholder": "ASPECTO"})
    pH = StringField('pH', validators=[],render_kw={"placeholder": "pH"})
    DENSIDAD = StringField('DENSIDAD', validators=[],render_kw={"placeholder": ""})
    REACCION = StringField('REACCION',validators=[],render_kw={"placeholder": ""})
    NITRITOS = StringField('NITRITOS',validators=[],render_kw={"placeholder": ""})
    LEUCOCITOS = StringField('LEUCOCITOS', validators=[],render_kw={"placeholder": ""})
    GLUCOSA =  StringField('GLUCOSA', validators=[],render_kw={"placeholder": ""})
    PROTEINAS = StringField('PROTEINAS', validators=[],render_kw={"placeholder": ""})
    UROBILINOGENO = StringField('UROBILINOGENO', validators=[],render_kw={"placeholder": ""})
    SANGRE = StringField('SANGRE', validators=[],render_kw={"placeholder": ""})
    HEMOGLOBINA = StringField('HEMOGLOBINA', validators=[],render_kw={"placeholder": ""})
    BILIRRUBINAS = StringField('BILIRRUBINAS',validators=[],render_kw={"placeholder": ""})
    CUERPOSCETONICOS = StringField('CUERPOS CETONICOS',validators=[],render_kw={"placeholder": ""})
    CELULASEPITELIALESBAJAS = StringField('CELULAS EPITELIALES BAJAS', validators=[],render_kw={"placeholder": ""})
    CELULASREDONDAS =  StringField('CELULAS REDONDAS', validators=[],render_kw={"placeholder": ""})
    PIOCITOS =  StringField('PIOCITOS', validators=[],render_kw={"placeholder": ""})
    HEMATIES = StringField('HEMATIES', validators=[],render_kw={"placeholder": ""})
    BACTERIAS = StringField('BACTERIAS', validators=[],render_kw={"placeholder": ""})
    CILINDROSGRANULOSOS = StringField('CILINDROS GRANULOSOS', validators=[],render_kw={"placeholder": ""})
    LEVADURAS = StringField('LEVADURAS', validators=[],render_kw={"placeholder": ""})
    HIFASHONGOS = StringField('HIFAS DE HONGOS',validators=[],render_kw={"placeholder": ""})
    CRISTALESACIDOURICO = StringField('CRISTALES ACIDO URICO',validators=[],render_kw={"placeholder": ""})
    CRISTALESOXALATOCALCIO = StringField('CRISTALES DE OXALATO DE CALCIO', validators=[],render_kw={"placeholder": ""})
    FILAMENTOMUCOSO =  StringField('FILAMENTO MUCOSO', validators=[],render_kw={"placeholder": ""})
        
    submit = SubmitField('Enviar')


class pcopro(FlaskForm):
    COLOR = StringField('COLOR', validators=[],render_kw={"placeholder": ""})
    CONSISTENCIA = StringField('CONSISTENCIA', validators=[],render_kw={"placeholder": ""})
    ASPECTO = StringField('ASPECTO', validators=[],render_kw={"placeholder": ""})
    SANGRE = StringField('SANGRE', validators=[],render_kw={"placeholder": ""})
    MOCO = StringField('MOCO',validators=[],render_kw={"placeholder": ""})
    RESTOS_ALIMENTICIOS = StringField('RESTOS ALIMENTICIOS',validators=[],render_kw={"placeholder": ""})
    RESTOS_VEGETALES = StringField('RESTOS VEGETALES: (++)', validators=[],render_kw={"placeholder": ""})
    ALMIDONES =  StringField('ALMIDONES: (+)', validators=[],render_kw={"placeholder": ""})
    GRASAS = StringField('GRASAS: (++)', validators=[],render_kw={"placeholder": ""})
    LEVADURAS = StringField('LEVADURAS: (+)',validators=[],render_kw={"placeholder": ""})
    HIFAS_HONGOS = StringField('HIFAS DE HONGOS:',validators=[],render_kw={"placeholder": ""})
    LEUCOCITOS = StringField('LEUCOCITOS', validators=[],render_kw={"placeholder": ""})
    HEMATIES =  StringField('HEMATÍES', validators=[],render_kw={"placeholder": ":"})
    FLORA_BACTERIANA =  StringField('FLORA BACTERIANA:', validators=[],render_kw={"placeholder": ""}) 
    QUISTES_AMEBA_COLI =  StringField('QUISTES DE AMEBA COLI: (+)', validators=[],render_kw={"placeholder": ":"})
    QUISTES_AMEBA_HISTOLITICA =  StringField('QUISTES DE AMEBA HISTOLITICA: (+)', validators=[],render_kw={"placeholder": ""}) 


    submit = SubmitField('Enviar')


class pcultivo(FlaskForm):
    GERMEN_AISLADO = StringField('GERMEN AISLADO', validators=[],render_kw={"placeholder": ""})
    CONTAJE = StringField('CONTAJE', validators=[],render_kw={"placeholder": ""})
    ACIDO_NALIDIXICO = StringField('ACIDO NALIDIXICO', validators=[],render_kw={"placeholder": ""})
    AMOXICILINA_AC_CLAVULANICO = StringField('AMOXICILINA + AC CLAVULANICO', validators=[],render_kw={"placeholder": ""})
    CEFOTAXIMA = StringField('CEFOTAXIMA',validators=[],render_kw={"placeholder": ""})
    CEFUROXIME = StringField('CEFUROXIME',validators=[],render_kw={"placeholder": ""})
    CIPROFLOXACINA = StringField('CIPROFLOXACINA:', validators=[],render_kw={"placeholder": ""})
    COTRIMOXAZOL =  StringField('COTRIMOXAZOL:', validators=[],render_kw={"placeholder": ""})
    FOSFOMICINA = StringField('FOSFOMICINA:', validators=[],render_kw={"placeholder": ""})
    AMIKACINA = StringField('AMIKACINA:',validators=[],render_kw={"placeholder": ""})
    AMPICILINA = StringField('AMPICILINA:',validators=[],render_kw={"placeholder": ""})
    GENTAMICINA = StringField('GENTAMICINA', validators=[],render_kw={"placeholder": ""})
    NITROFURANTOINA =  StringField('NITROFURANTOINA', validators=[],render_kw={"placeholder": ":"})
  
    submit = SubmitField('Enviar')


class phto(FlaskForm):
    HEMATOCRITO = StringField('HEMATOCRITO', validators=[],render_kw={"placeholder": ""})
    HEMOGLOBINA = StringField('HEMOGLOBINA', validators=[],render_kw={"placeholder": ""})
 
    submit = SubmitField('Enviar')


class pespecial(FlaskForm):
    RESULTADO = StringField('RESULTADO', validators=[],render_kw={"placeholder": ""})
    METODO = StringField('METODO', validators=[],render_kw={"placeholder": ""})
 
    submit = SubmitField('Enviar')

class pasto(FlaskForm):
    ASTO = StringField('A.S.T.O.', validators=[],render_kw={"placeholder": ""})
    PCR = StringField('P.C.R.', validators=[],render_kw={"placeholder": ""})
    LATEX = StringField('L.A.T.E.X.', validators=[],render_kw={"placeholder": ""})
 
    submit = SubmitField('Enviar')


class pgrupo(FlaskForm):
    GRUPO = StringField('GRUPO', validators=[],render_kw={"placeholder": ""})
    FACTOR_Rh = StringField('FACTOR Rh', validators=[],render_kw={"placeholder": ""})
   
    submit = SubmitField('Enviar')


class pAGLUTI(FlaskForm):
    TIFICO_O = StringField('TIFICO O', validators=[],render_kw={"placeholder": ""})
    TIFICO_H = StringField('TIFICO H', validators=[],render_kw={"placeholder": ""})
    PARATIFICA_A = StringField('PARATIFICA A', validators=[],render_kw={"placeholder": ""})
    PARATIFICO_B = StringField('PARATIFICO B', validators=[],render_kw={"placeholder": ""})
    PROTEUS_OX19 = StringField('PROTEUS OX19', validators=[],render_kw={"placeholder": ""})
    BRUCELLA_ABORTUS = StringField('BRUCELLA ABORTUS', validators=[],render_kw={"placeholder": ""})
   
    submit = SubmitField('Enviar')


class pGram_GF(FlaskForm):
    RESULTADO = StringField('RESULTADO', validators=[],render_kw={"placeholder": ""})
    Cocos_Gram_Positivos = StringField('Cocos_Gram_Positivos', validators=[],render_kw={"placeholder": ""})
   
    submit = SubmitField('Enviar')


class pvdrl(FlaskForm):
    HIV_1_2 = StringField('H.I.V. 1 - 2', validators=[],render_kw={"placeholder": ""})

    submit = SubmitField('Enviar')


class pTOXI(FlaskForm):
      MARIHUANA = StringField('MARIHUANA(THC)', validators=[],render_kw={"placeholder": ""})
      COCAINA = StringField('COCAINA (COC)', validators=[],render_kw={"placeholder": ""})
   
      submit = SubmitField('Enviar')


class pruebas(FlaskForm):
    tp = RadioField('TP:',choices=[('TP', 'TP')],render_kw={}, id='tp')
    ttp = RadioField('T.T P:',choices=[('T.T P', 'T.T P')],render_kw={}, id='ttp')
    inr = RadioField('INR:',choices=[('INR', 'INR')],render_kw={}, id='inr')
    dimero = RadioField('DIMERO D:',choices=[('DIMERO D', 'DIMERO D')],render_kw={}, id='dimero')
    t3 = RadioField('T3:',choices=[('T3', 'T3')],render_kw={}, id='t3')
    t4 = RadioField('T4:',choices=[('T4', 'T4')],render_kw={}, id='t4')
    tsh = RadioField('TSH:',choices=[('TSH', 'TSH')],render_kw={}, id='tsh')
    tf3 = RadioField('TF3 Libre:',choices=[('TF3 Libre', 'TF3 Libre')],render_kw={}, id='tf3')
    tf4 = RadioField('TF4 Libre:',choices=[('TF4 Libre', 'TF4 Libre')],render_kw={}, id='tf4')
    proge = RadioField('Progesterona:',choices=[('Progesterona', 'Progesterona')],render_kw={}, id='proge')
    prolac = RadioField('Prolactina:',choices=[('Prolactina', 'Prolactina')],render_kw={}, id='prolac')
    na = RadioField('Na:',choices=[('Na', 'Na')],render_kw={}, id='na')
    k = RadioField('K:',choices=[('K', 'K')],render_kw={}, id='k')
    cl = RadioField('Cl:',choices=[('Cl', 'Cl')],render_kw={}, id='cl')
    calt = RadioField('CALCIO TOTAL:',choices=[('CALCIO TOTAL', 'CALCIO TOTAL')],render_kw={}, id='calt')
    fosf = RadioField('FOSFORO:',choices=[('FOSFORO', 'FOSFORO')],render_kw={}, id='fosf')
    magn = RadioField('MAGNESIO:',choices=[('MAGNESIO', 'MAGNESIO')],render_kw={}, id='magn')
    gluc = RadioField('GLUCOSA:',choices=[('GLUCOSA', 'GLUCOSA')],render_kw={}, id='gluc')
    urea = RadioField('UREA:',choices=[('UREA', 'UREA')],render_kw={}, id='urea')
    bun = RadioField('BUN:',choices=[('BUN', 'BUN')],render_kw={}, id='bun')
    creatinina = RadioField('CREATININA:',choices=[('CREATININA', 'CREATININA')],render_kw={}, id='creatinina')
    acid_uri = RadioField('ACIDO URICO:',choices=[('ACIDO URICO', 'ACIDO URICO')],render_kw={}, id='acid_uri')
    coles = RadioField('COLESTEROL:',choices=[('COLESTEROL', 'COLESTEROL')],render_kw={}, id='coles')
    trigli = RadioField('TRIGLLICERIDOS:',choices=[('TRIGLLICERIDOS', 'TRIGLLICERIDOS')],render_kw={}, id='trigli')
    col_hdl = RadioField('COLESTEROL HDL:',choices=[('COLESTEROL HDL', 'COLESTEROL HDL')],render_kw={}, id='col_hdl')
    col_ldl = RadioField('COLESTEROL LDL:',choices=[('COLESTEROL LDL', 'COLESTEROL LDL')],render_kw={}, id='col_ldl')
    bilirr = RadioField('BILIRRUBINA:',choices=[('BILIRRUBINA', 'BILIRRUBINA')],render_kw={}, id='bilirr')
    d = RadioField('D:',choices=[('D', 'D')],render_kw={}, id='d')
    i = RadioField('I:',choices=[('I', 'I')],render_kw={}, id='i')
    t = RadioField('T:',choices=[('T', 'T')],render_kw={}, id='t')
    gluc_pp = RadioField('GLUCOSA PP 2Horas:',choices=[('GLUCOSA PP 2Horas', 'GLUCOSA PP 2Horas')],render_kw={}, id='gluc_pp')
    prot_tot = RadioField('PROTEINAS TOTALES:',choices=[('PROTEINAS TOTALES', 'PROTEINAS TOTALES')],render_kw={}, id='prot_tot')
    albumina = RadioField('ALBUMINA:',choices=[('ALBUMINA', 'ALBUMINA')],render_kw={}, id='albumina')
    globu = RadioField('GLOBULINAS:',choices=[('GLOBULINAS', 'GLOBULINAS')],render_kw={}, id='globu')
    test_su = RadioField('TEST DE SULLIVAN:',choices=[('GLOBULINAS', 'GLOBULINAS')],render_kw={}, id='test_su')
    tgo = RadioField('TGO:',choices=[('TGO', 'TGO')],render_kw={}, id='tgo')
    tgp = RadioField('TGP:',choices=[('TGP', 'TGP')],render_kw={}, id='tgp')
    fosf_alc = RadioField('FOSFATASA ALCALINA:',choices=[('FOSFATASA ALCALINA', 'FOSFATASA ALCALINA')],render_kw={}, id='fosf_alc')
    fosf_aci_t = RadioField('FOSFATASA ACIDA TOTAL:',choices=[('FOSFATASA ACIDA TOTAL', 'FOSFATASA ACIDA TOTAL')],render_kw={}, id='fosf_aci_t')
    fosf_aci_pro = RadioField('FOSFATASA ACIDA PROSTÁTICA:',choices=[('FOSFATASA ACIDA PROSTÁTICA', 'FOSFATASA ACIDA PROSTÁTICA')],render_kw={}, id='fosf_aci_pro')
    desh_lac = RadioField('DESHIDROGENASA LÁCTICA:',choices=[('DESHIDROGENASA LÁCTICA', 'DESHIDROGENASA LÁCTICA')],render_kw={}, id='desh_lac')
    coline = RadioField('COLINESTERASA:',choices=[('COLINESTERASA', 'COLINESTERASA')],render_kw={}, id='coline')
    amilasa = RadioField('AMILASA:',choices=[('AMILASA', 'AMILASA')],render_kw={}, id='amilasa')
    lipasa = RadioField('LIPASA:',choices=[('LIPASA', 'LIPASA')],render_kw={}, id='lipasa')
    gamm_gt = RadioField('GAMMA GT:',choices=[('GAMMA GT', 'GAMMA GT')],render_kw={}, id='gamm_gt')




    submit = SubmitField('Enviar')


class FormChangePassword(FlaskForm):
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Aceptar')


class UploadForm(FlaskForm):
    photo = FileField('selecciona imagen:',validators=[FileRequired()])
    submit = SubmitField('Submit')