from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask("__name__")

@app.route("/enviar_email", methods=['POST'])
def enviar_email():
    if request.method == "POST":
        titulo = request.form['titulo']
        corpo = request.form['corpo']
        
        host = "smtp.gmail.com"
        port = "587"
        login = "enviodeemail608@gmail.com"
        senha = "hxphydbmqlxfewxd"

        server = smtplib.SMTP(host,port)

        server.ehlo()
        server.starttls()
        server.login(login,senha)

        # Construir o email
        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = "gilbertodosas@gmail.com"
        email_msg['Subject'] = titulo
        email_msg.attach(MIMEText(corpo, 'plain'))
        
        # Enviar o email
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        
        return "Email enviado com sucesso!"


@app.route("/")
def hello_world():
    return render_template("home.html", title = "Curso de Violão - Gilberto Soares")

@app.route("/contatos", methods=['GET', 'POST'])
def contatos():
    return render_template("contatos.html", title = "Contatos")

if __name__ == '__main__':
    app.run(debug=True)