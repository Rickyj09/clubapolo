from typing import Text
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from aplicacion.forms import LoginForm, UploadForm, fechas, hepaticas, alumno,campeonato
from jinja2 import Environment, FileSystemLoader
from os import listdir
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user


from aplicacion.forms import LoginForm, FormUsuario
import pdfkit
import os


UPLOAD_FOLDER = os.path.abspath("./static/uploads/")
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'apolo'
mysql = MySQL(app)

# setting
app.secret_key = 'millave'


@login_manager.user_loader
def load_user(user_id):
    return (user_id)


@app.route('/')
def inicio():
    return render_template("inicio.html")


@app.route('/inicio_1')
@app.route('/inicio_1/<id>')
def inicio_1(id='0'):
    from aplicacion.models import Articulos, Categorias
    categoria = Categorias.query.get(id)
    if id == '0':
        articulos = Articulos.query.all()
    else:
        articulos = Articulos.query.filter_by(CategoriaId=id)
    categorias = Categorias.query.all()
    return render_template("inicio_1.html", articulos=articulos, categorias=categorias, categoria=categoria)


@app.route('/inicio_new')
@app.route('/inicio_new/<id>')
def inicio_new(id='0'):
    from aplicacion.models import Articulos, Categorias
    categoria = Categorias.query.get(id)
    if id == '0':
        articulos = Articulos.query.all()
    else:
        articulos = Articulos.query.filter_by(CategoriaId=id)
    categorias = Categorias.query.all()
    return render_template("inicio_new.html", articulos=articulos, categorias=categorias, categoria=categoria)

@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")



@app.route('/historia')
def historia():
    return render_template("historia.html")


@app.route('/ocupa')
def ocupa():
    return render_template("ocupa.html")


@app.route('/hepaticas', methods=["get", "post"])
@login_required
def phepaticas():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = hepaticas()
    if form.validate_on_submit():
        SGOT = request.form['SGOT']
        SGPT = request.form['SGPT']
        BILIRRUBIN_TOTAL = request.form['BILIRRUBIN_TOTAL']
        BILIRRUBINA_DIRECTA = request.form['BILIRRUBINA_DIRECTA']
        BILIRRUBINA_INDIRECTA = request.form['BILIRRUBINA_INDIRECTA']
        SGPROTEINAS_TOTALESOT = request.form['PROTEINAS_TOTALES']
        AMILASA = request.form['AMILASA']
        LIPASA = request.form['LIPASA']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,sgot,sgpt,BILIRRUBINA_TOTAL,bilirrubina_directa,bilirrubina_indirecta,proteinas_totales,amilasa,lipasa,id_paci,fecha_examen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       ('hepaticas',SGOT, SGPT, BILIRRUBIN_TOTAL, BILIRRUBINA_DIRECTA, BILIRRUBINA_INDIRECTA, SGPROTEINAS_TOTALESOT, AMILASA, LIPASA, datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'hepaticas',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('resumen'))
    return render_template('hepaticas.html', form=form)


@app.route('/resumen')
@login_required
def resumen():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('resumen.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)



@app.route('/emo', methods=["get", "post"])
@login_required
def emo():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pemo()
    if form.validate_on_submit():
        COLOR = request.form['COLOR']
        ASPECTO = request.form['ASPECTO']
        pH = request.form['pH']
        DENSIDAD = request.form['DENSIDAD']
        REACCION = request.form['REACCION']
        NITRITOS = request.form['NITRITOS']
        LEUCOCITOS = request.form['LEUCOCITOS']
        GLUCOSA = request.form['GLUCOSA']
        PROTEINAS = request.form['PROTEINAS']
        UROBILINOGENO = request.form['UROBILINOGENO']
        SANGRE = request.form['SANGRE']
        HEMOGLOBINA = request.form['HEMOGLOBINA']
        BILIRRUBINAS = request.form['BILIRRUBINAS']
        CUERPOSCETONICOS = request.form['CUERPOSCETONICOS']
        CELULASEPITELIALESBAJAS = request.form['CELULASEPITELIALESBAJAS']
        CELULASREDONDAS = request.form['CELULASREDONDAS']
        PIOCITOS = request.form['PIOCITOS']
        HEMATIES = request.form['HEMATIES']
        BACTERIAS = request.form['BACTERIAS']
        CILINDROSGRANULOSOS = request.form['CILINDROSGRANULOSOS']
        LEVADURAS = request.form['LEVADURAS']
        HIFASHONGOS = request.form['HIFASHONGOS']
        CRISTALESACIDOURICO = request.form['CRISTALESACIDOURICO']
        CRISTALESOXALATOCALCIO = request.form['CRISTALESOXALATOCALCIO']
        FILAMENTOMUCOSO = request.form['FILAMENTOMUCOSO']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,COLOR,ASPECTO,pH,DENSIDAD,REACCION,NITRITOS,LEUCOCITOS,GLUCOSA,PROTEINAS,UROBILINOGENO,SANGRE,HEMOGLOBINA,BILIRRUBINAS,CUERPOS_CETONICOS,CELULAS_EPITELIALES_BAJAS,CELULAS_REDONDAS,PIOCITOS,HEMATIES,BACTERIAS,CILINDROS_GRANULOSOS,LEVADURAS,HIFAS_HONGOS,CRISTALES_ACIDO_URICO,CRISTALES_OXALATO_CALCIO,FILAMENTO_MUCOSO,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       ('emo',COLOR, ASPECTO, pH, DENSIDAD, REACCION,NITRITOS, LEUCOCITOS, GLUCOSA, PROTEINAS,UROBILINOGENO, SANGRE,HEMOGLOBINA,BILIRRUBINAS,CUERPOSCETONICOS,CELULASEPITELIALESBAJAS,CELULASREDONDAS,PIOCITOS,HEMATIES,BACTERIAS,CILINDROSGRANULOSOS,LEVADURAS,HIFASHONGOS,CRISTALESACIDOURICO,CRISTALESOXALATOCALCIO,FILAMENTOMUCOSO,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'emo',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_emo'))
    return render_template('emo.html', form=form)


@app.route('/res_emo')
@login_required
def res_emo():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_emo.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/copro', methods=["get", "post"])
@login_required
def copro():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pcopro()
    if form.validate_on_submit():
        COLOR = request.form['COLOR']
        CONSISTENCIA = request.form['CONSISTENCIA']
        ASPECTO = request.form['ASPECTO']
        SANGRE = request.form['SANGRE']
        MOCO = request.form['MOCO']
        RESTOS_ALIMENTICIOS = request.form['RESTOS_ALIMENTICIOS']
        RESTOS_VEGETALES = request.form['RESTOS_VEGETALES']
        ALMIDONES = request.form['ALMIDONES']
        GRASAS = request.form['GRASAS']
        LEVADURAS = request.form['LEVADURAS']
        HIFAS_HONGOS = request.form['HIFAS_HONGOS']
        LEUCOCITOS = request.form['LEUCOCITOS']
        HEMATIES = request.form['HEMATIES']
        FLORA_BACTERIANA = request.form['FLORA_BACTERIANA']
        QUISTES_AMEBA_COLI = request.form['QUISTES_AMEBA_COLI']
        QUISTES_AMEBA_HISTOLITICA = request.form['QUISTES_AMEBA_HISTOLITICA']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,COLOR,CONSISTENCIA,ASPECTO,SANGRE,MOCO,RESTOS_ALIMENTICIOS,RESTOS_VEGETALES,ALMIDONES,GRASAS,LEVADURAS,HIFAS_HONGOS,LEUCOCITOS,HEMATIES,FLORA_BACTERIANA,QUISTES_AMEBA_COLI,QUISTES_AMEBA_HISTOLITICA,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       ('copro',COLOR,CONSISTENCIA,ASPECTO,SANGRE,MOCO,RESTOS_ALIMENTICIOS,RESTOS_VEGETALES,ALMIDONES,GRASAS,LEVADURAS,HIFAS_HONGOS,LEUCOCITOS,HEMATIES,FLORA_BACTERIANA,QUISTES_AMEBA_COLI,QUISTES_AMEBA_HISTOLITICA,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'copro',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_copro'))
    return render_template('copro.html', form=form)


@app.route('/res_copro')
@login_required
def res_copro():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_copro.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/cultivo', methods=["get", "post"])
@login_required
def cultivo():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pcultivo()
    if form.validate_on_submit():
        GERMEN_AISLADO = request.form['GERMEN_AISLADO']
        CONTAJE = request.form['CONTAJE']
        ACIDO_NALIDIXICO = request.form['ACIDO_NALIDIXICO']
        AMOXICILINA_AC_CLAVULANICO = request.form['AMOXICILINA_AC_CLAVULANICO']
        CEFOTAXIMA = request.form['CEFOTAXIMA']
        CEFUROXIME = request.form['CEFUROXIME']
        CIPROFLOXACINA = request.form['CIPROFLOXACINA']
        COTRIMOXAZOL = request.form['COTRIMOXAZOL']
        FOSFOMICINA = request.form['FOSFOMICINA']
        AMIKACINA = request.form['AMIKACINA']
        AMPICILINA = request.form['AMPICILINA']
        GENTAMICINA = request.form['GENTAMICINA']
        NITROFURANTOINA = request.form['NITROFURANTOINA']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,GERMEN_AISLADO,CONTAJE,ACIDO_NALIDIXICO,AMOXICILINA_AC_CLAVULANICO,CEFOTAXIMA,CEFUROXIME,CIPROFLOXACINA,COTRIMOXAZOL,FOSFOMICINA,AMIKACINA,AMPICILINA,GENTAMICINA,NITROFURANTOINA,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       ('cultivo',GERMEN_AISLADO,CONTAJE,ACIDO_NALIDIXICO,AMOXICILINA_AC_CLAVULANICO,CEFOTAXIMA,CEFUROXIME,CIPROFLOXACINA,COTRIMOXAZOL,FOSFOMICINA,AMIKACINA,AMPICILINA,GENTAMICINA,NITROFURANTOINA,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'cultivo',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_cultivo'))
    return render_template('cultivo.html', form=form)


@app.route('/res_cultivo')
@login_required
def res_cultivo():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_cultivo.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/hto', methods=["get", "post"])
@login_required
def hto():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = phto()
    if form.validate_on_submit():
        HEMATOCRITO = request.form['HEMATOCRITO']
        HEMOGLOBINA = request.form['HEMOGLOBINA']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,HEMATOCRITO,HEMOGLOBINA,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',
                       ('HTO',HEMATOCRITO,HEMOGLOBINA,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'hto',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_hto'))
    return render_template('hto.html', form=form)


@app.route('/res_hto')
@login_required
def res_hto():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_hto.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/especial', methods=["get", "post"])
@login_required
def especial():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pespecial()
    if form.validate_on_submit():
        RESULTADO = request.form['RESULTADO']
        METODO = request.form['METODO']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,RESULTADO,METODO,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',
                       ('especial',RESULTADO,METODO,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'especial',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_especial'))
    return render_template('especial.html', form=form)


@app.route('/res_especial')
@login_required
def res_especial():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_especial.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/asto', methods=["get", "post"])
@login_required
def asto():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pasto()
    if form.validate_on_submit():
        ASTO = request.form['ASTO']
        PCR = request.form['PCR']
        LATEX = request.form['LATEX']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,ASTO,PCR,LATEX,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s,%s)',
                       ('asto',ASTO,PCR,LATEX,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'asto',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_asto'))
    return render_template('asto.html', form=form)


@app.route('/res_asto')
@login_required
def res_asto():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_asto.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/grupo', methods=["get", "post"])
@login_required
def grupo():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pgrupo()
    if form.validate_on_submit():
        GRUPO = request.form['GRUPO']
        FACTOR_Rh = request.form['FACTOR_Rh']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,GRUPO,FACTOR_Rh,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',
                       ('grupo',GRUPO,FACTOR_Rh,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'grupo',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_grupo'))
    return render_template('grupo.html', form=form)


@app.route('/res_grupo')
@login_required
def res_grupo():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_grupo.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)



@app.route('/AGLUTI', methods=["get", "post"])
@login_required
def AGLUTI():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pAGLUTI()
    if form.validate_on_submit():
        TIFICO_O = request.form['TIFICO_O']
        TIFICO_H = request.form['TIFICO_H']
        PARATIFICA_A = request.form['PARATIFICA_A']
        PARATIFICO_B = request.form['PARATIFICO_B']
        PROTEUS_OX19 = request.form['PROTEUS_OX19']
        BRUCELLA_ABORTUS = request.form['BRUCELLA_ABORTUS']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,TIFICO_O,TIFICO_H,PARATIFICA_A,PARATIFICO_B,PROTEUS_OX19,BRUCELLA_ABORTUS,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       ('AGLUTI',TIFICO_O,TIFICO_H,PARATIFICA_A,PARATIFICO_B,PROTEUS_OX19,BRUCELLA_ABORTUS,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'grupo',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_AGLUTI'))
    return render_template('AGLUTI.html', form=form)


@app.route('/res_AGLUTI')
@login_required
def res_AGLUTI():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_AGLUTI.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/Gram_GF', methods=["get", "post"])
@login_required
def Gram_GF():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pGram_GF()
    if form.validate_on_submit():
        RESULTADO = request.form['RESULTADO']
        Cocos_Gram_Positivos = request.form['Cocos_Gram_Positivos']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,RESULTADO,Cocos_Gram_Positivos,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',
                       ('Gram_GF',RESULTADO,Cocos_Gram_Positivos,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'grupo',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_Gram_GF'))
    return render_template('Gram_GF.html', form=form)


@app.route('/res_Gram_GF')
@login_required
def res_Gram_GF():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_Gram_GF.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/vdrl', methods=["get", "post"])
@login_required
def vdrl():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pvdrl()
    if form.validate_on_submit():
        HIV_1_2 = request.form['HIV_1_2']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,HIV_1_2,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s)',
                       ('vdrl',HIV_1_2,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'grupo',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_vdrl'))
    return render_template('vdrl.html', form=form)


@app.route('/res_vdrl')
@login_required
def res_vdrl():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_vdrl.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)


@app.route('/TOXI', methods=["get", "post"])
@login_required
def TOXI():
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    form = pTOXI()
    if form.validate_on_submit():
        MARIHUANA = request.form['MARIHUANA']
        COCAINA = request.form['COCAINA']
        cursor = mysql.connection.cursor()
        cursor.execute("select CURDATE();")
        fecha_hoy = cursor.fetchone()
        datos = request.cookies.get('cookie_pac')
        cursor.execute("SELECT nombres FROM paciente WHERE iden = %s", [datos])
        nombres = cursor.fetchone()
        cursor.execute("SELECT apellido1 FROM paciente WHERE iden = %s", [datos])
        apellido = cursor.fetchone()
        cursor.execute('insert into pruebas (nombre_prueba,MARIHUANA,COCAINA,id_paci,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',
                       ('TOXI',MARIHUANA,COCAINA,datos, fecha_hoy))
        cursor.execute('insert into pacientexexamen (iden,nombre,apellido,examen,FECHA_EXAMEN) VALUES (%s,%s,%s,%s,%s)',(datos,nombres,apellido,'grupo',fecha_hoy))
        mysql.connection.commit()
        flash('Guardado Correctamente')
        return redirect(url_for('res_TOXI'))
    return render_template('TOXI.html', form=form)


@app.route('/res_TOXI')
@login_required
def res_TOXI():
    datos = request.cookies.get('cookie_pac')
    cursor = mysql.connection.cursor()
    cursor.execute(
        "select apellido1,nombres from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    nom_pac = cursor.fetchone()
    cursor.execute(
        "select medico from paciente a inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    med = cursor.fetchone()
    cursor.execute(
        "SELECT (TIMESTAMPDIFF(YEAR,fec_nac,CURDATE())) AS edad FROM paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    edad = cursor.fetchone()
    cursor.execute("select CURDATE();")
    fec_hoy = cursor.fetchone()
    cursor.execute(
        "select iden from paciente a  inner join pruebas b on  a.iden = b.id_paci where iden = %s;" , [datos])
    ci = cursor.fetchone()
    cursor.execute(
        "select * from pruebas where id = (select MAX(id) from pruebas);")
    datos = cursor.fetchall()
    print(datos)
    cursor.close()

    return render_template('res_TOXI.html', nom_pac=nom_pac, med=med, edad=edad, fec_hoy=fec_hoy, ci=ci, datos=datos)



@login_manager.user_loader
def load_user(user_id):
    from aplicacion.models import Usuarios
    return Usuarios.query.get(int(user_id))


@app.route('/upload', methods=['get', 'post'])
def upload():
    form = UploadForm()  # carga request.from y request.file
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(app.root_path+"/static/img/subidas/"+filename)
        return redirect(url_for('inicio_foto'))
    return render_template('upload.html', form=form)


@app.route('/upload_1', methods=['get', 'post'])
def upload_1():
    form = UploadForm()  # carga request.from y request.file
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(app.root_path+"/static/img/subidas/"+filename)
        return redirect(url_for('reporte_foto'))
    return render_template('upload_1.html', form=form)


@app.route('/inicio_foto')
@login_required
def inicio_foto():
    lista = []
    for file in listdir(app.root_path+"/static/img/subidas/"):
        lista.append(file)
    return render_template("inicio_foto.html", lista=lista)


@app.route('/reporte_foto')
@login_required
def reporte_foto():
    lista = []
    for file in listdir(app.root_path+"/static/img/subidas/"):
        lista.append(file)
    return render_template("reporte_foto.html", lista=lista)


@app.route('/reporte_foto1')
@login_required
def reporte_foto1():
    lista = []
    for file in listdir(app.root_path+"/static/img/subidas/"):
        lista.append(file)
    return render_template("reporte_foto1.html", lista=lista)


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    cursor = mysql.connection.cursor()

    form = fechas()
    if form.validate_on_submit():
        fec_ini = request.form['fec_ini']
        fec_fin = request.form['fec_fin']
        cursor = mysql.connection.cursor()
        cursor.execute(
            "select apellido1,nombres from paciente a  inner join hepaticas b on  a.iden = b.id_paci;")
        datos = cursor.fetchone()
        print(datos)
        return redirect(url_for('inicio'))
    return render_template('home.html', form=form)


@app.route('/home_alumn', methods=['GET', 'POST'])
@login_required
def home_alumn():

    return render_template('home_alumn.html')


@app.route('/home_campeonato', methods=['GET', 'POST'])
@login_required
def home_campeonato():

    return render_template('home_campeonato.html')

@app.route('/pacientes', methods=['GET', 'POST'])
@login_required
def pacientes():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from paciente LIMIT 10;")
    paci = cursor.fetchall()
    print(paci)
    form = bus_pac()
    datos = request.cookies.get('cookie_pac',None)
    print(datos)
    if form.validate_on_submit():
        iden = request.form['iden']
        return  render_template("listar_paci.html", paci=paci,iden=iden)
   #iden = request.form['id']
    #print(iden)     
    return render_template("pacientes.html", form=form, paci=paci)


@app.route('/listar_paci/<id>', methods=['POST', 'GET'])
@login_required
def listar_paci(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM paciente a inner join cat_examenes b on  a.id_examen = b.id  WHERE a.iden = %s )',  [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('listar-paci.html', contact=data[0])



@app.route('/alumno_new', methods=["get", "post"])
@login_required
def alumno_new():
    form = alumno()
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        iden = request.form['iden']
        tipo_iden = request.form['tipo_iden']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        nombres = request.form['nombres']
        est_civil = request.form['est_civil']
        fec_nac = request.form['fec_nac']
        fec_ingreso = request.form['fec_ingreso']
        sexo = request.form['sexo']
        direccion = request.form['direccion']
        ocupacion = request.form['ocupacion']
        tipo_s = request.form['tipo_s']
        Nivel_edu = request.form['Nivel_edu']
        telefono1 = request.form['telefono1']
        telefono2 = request.form['telefono2']
        status = request.form['status']
        foto = request.form['foto']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute('insert into alumno (apellido_p,apellido_m,identificacion,tipo_iden,nombres,est_civil,fecha_nacimiento,fecha_ingreso,genero, ocupacion, status, foto, tipo_sangre, nivel_educacion,direccion,telefono1,telefono2,mail) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (apellido1, apellido2, iden, tipo_iden, nombres, est_civil, fec_nac,fec_ingreso, sexo,ocupacion, status,foto,tipo_s,Nivel_edu,direccion, telefono1, telefono2, email))
        mysql.connection.commit()
        flash('Alumno guardado correctamente')
        return render_template("home.html", form=form)
    return render_template("alumno_new.html", form=form)



@app.route('/campeonato_new', methods=["get", "post"])
@login_required
def campeonato_new():
    form = campeonato()
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        puntua = request.form['puntua']
        fecha = request.form['fecha']
        obs = request.form['obs']
        cursor = mysql.connection.cursor()
        cursor.execute('insert into campeonato (nombre,puntua,fecha,obs) VALUES (%s,%s,%s,%s)',
                       (nombre, puntua, fecha, obs,))
        mysql.connection.commit()
        flash('Campeonato guardado correctamente')
        return render_template("home.html", form=form)
    return render_template("campeonato_new.html", form=form)


@app.route('/edit_pac/<string:id>', methods = ['POST', 'GET'])
def get_pac(id):
    cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM paciente WHERE ci = %s", (id))
    cur.execute("SELECT * FROM paciente WHERE ci = '1711459816'")
    data = cur.fetchone()
    cur.close()
    print(id)
    print(data[2])
    return render_template('edit_pac.html', paciente = data)


@app.route('/bus_pac', methods = ['POST', 'GET'])
@login_required
def bus_pac():
    form = buscapac()
    if request.method == 'POST':
        iden = request.form['iden']
        print(iden)
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM pacientexexamen WHERE iden = %s", [iden])
        data = cursor.fetchall()
        #print(data[0])
        resp = make_response(render_template('listar-paci.html', data=data))
        resp.set_cookie('cookie_pac',str(iden))
        return resp
    return render_template("bus_pac.html", form=form)



@app.route('/update_pac/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))





@app.route('/pruebas_lab', methods=['GET', 'POST'])
@login_required
def pruebas_lab():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from cat_examenes;")
    prulab = cursor.fetchall()
    datos = request.cookies.get('cookie_pac')
    print(datos)
    return render_template('pruebas_lab.html', prulab=prulab)
    


@app.route('/genera_pdf')
@login_required
def genera_pdf():
    env = Environment(loader=FileSystemLoader('templates'))
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    pdfkit.from_file('resumen.html', 'out.pdf', options=options)
    return 'OK'


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404


@app.route('/cons_404', methods=['GET', 'POST'])
def cons_404():
    return render_template('404_cons.html')


@app.route('/login', methods=['get', 'post'])
def login():
    from aplicacion.models import Usuarios
    # Control de permisos
    if current_user.is_authenticated:
        # return 'OK'
        return redirect(url_for("home_alumn"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuarios.query.filter_by(username=form.username.data).first()
        print(user)
        pas1 = Usuarios.query.filter_by(password=form.password.data).first()
        print(pas1)
        pas = user.verify_password(form.password.data)
        print(pas)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('home_alumn'))
        form.username.errors.append("Usuario o contraseña incorrectas.")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('inicio'))


@app.route('/perfil/<username>', methods=["get", "post"])
@login_required
def perfil(username):
    from aplicacion.models import Usuarios
    user = Usuarios.query.filter_by(username=username).first()
    if user is None:
        render_template("404.html")
    form = FormUsuario(request.form, obj=user)
    del form.password
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("inicio"))
    return render_template("usuarios_new.html", form=form, perfil=True)


@login_manager.user_loader
def load_user(user_id):
    from aplicacion.models import Usuarios
    return Usuarios.query.get(int(user_id))
