from flask import render_template, app, Flask

app = Flask(__name__)

reservas = []

lista_salas = []


@app.route("/login")
def pagina_login() -> None:
    return render_template("login.html")


@app.route("/cadastro")
def pagina_cadastro() -> None:
    return render_template("cadastro.html")


@app.route("/reservas")
def pagina_reservas() -> None:
    return render_template("reservas.html")


@app.route("/reservar-sala")
def pagina_reservar_sala() -> None:
    return render_template("reservar-sala.html")

@app.route("/detalhe-reserva")
def pagina_detalhe_reserva() -> None:
    return render_template("reserva/detalhe-reserva.html", reserva="reserva")


@app.route("/cadastrar-sala")
def pagina_cadastrar_sala() -> None:
    return render_template("cadastrar-sala.html")


@app.route("/")
def pagina_principal():
    return render_template("listar-salas.html", lista_salas=lista_salas)


numero = 1209517

@app.route("/teste")
def teste():
    return render_template("teste.html", num=numero)


if __name__ == "__main__":
    app.debug = True
    app.run()
