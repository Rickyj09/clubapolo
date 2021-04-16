from flask import Flask , render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import calendar
from flask_mail import Mail  # 1. Importamos la clase Mail
from flask_mail import Message
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# initializations
app = Flask(__name__)
mail = Mail() 
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('jerez.ricardo09@gmail.com', 'CrsbRc@2021')


#setting
app.secret_key = 'millave'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'jerez.ricardo09@gmail.com'
MAIL_PASSWORD = 'CrsbRc@2021'


# routes
@app.route('/')
def home():
 return render_template('home.html')

@app.route('/tray')
def lab():
    return render_template('tray.html')

@app.route('/ocupa')
def ocupa():
    return render_template('ocupa.html')

@app.route('/envia_mail', methods=['POST'])
def envia_mail():
    if request.method == 'POST':
        nom = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        mensaje1 = 'Subject: {}\n\n{}'.format(email,nom)
        server.sendmail("jerez.ricardo09@gmail.com", "jerez_ricardo9@hotmail.com", mensaje1, mensaje)
        server.quit()
        return redirect( url_for('home'))


if __name__ == "__main__":
    app.run(port=5000, debug=True)


    