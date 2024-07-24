from flask import render_template, app, Flask

app = Flask(__name__)

# As reservas serão feitas e armazenadas na lista de reservas     
reservas = []

# As salas serão cadastradas e armazenadas na lista de salas
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
    # Define que a aplicação rodará no modo debug, para que não seja necessário reinicar o servidor toda vez que uma mudança for feita
    app.debug = True
    
    # Para iniciar o servidor, é necessário apenas executar o código, ao invés de rodar a aplicação pela linha de comando
    app.run()
