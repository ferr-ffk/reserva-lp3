from flask import render_template, app, Flask, request, url_for, redirect
from service.reserva_service import *
from service.sala_service import *
from service.usuario_service import *

app = Flask(__name__)

# As reservas serão feitas e armazenadas na lista de reservas     
reservas = obter_reservas()

# As salas serão cadastradas e armazenadas na lista de salas
salas = obter_salas()


@app.route("/login")
def pagina_login() -> None:
    return render_template("login.html")


@app.route("/login", methods=['post'])
def pagina_login_post() -> None:
    criar_usuario(request.form['nome'], request.form['email'], request.form['senha'])

    return redirect(url_for(pagina_principal.__name__))


@app.route("/cadastro")
def pagina_cadastro() -> None:
    return render_template("cadastro.html")


@app.route("/reservas")
def pagina_reservas() -> None:
    return render_template("reservas.html", reservas=obter_reservas())


@app.route("/reservar-sala")
def pagina_reservar_sala() -> None:
    return render_template("reservar-sala.html", salas=obter_salas(), reservas=obter_reservas())


@app.route("/reservar-sala", methods=['post'])
def pagina_reservar_sala_post() -> None:
    criar_reserva(1, request.form['sala'], request.form['data_e_hora_de_inicio'], request.form['data_e_hora_do_fim'])

    return redirect(url_for(pagina_reservas.__name__))


@app.route("/detalhe-reserva/<id>")
def pagina_detalhe_reserva(id) -> None:
    return render_template("reserva/detalhe-reserva.html", reserva=obter_reserva(id))


@app.route("/cadastrar-sala")
def pagina_cadastrar_sala() -> None:
    return render_template("cadastrar-sala.html")


@app.route("/cadastrar-sala/<id>")
def pagina_cadastrar_sala_detalhe(id) -> None:
    return render_template("cadastrar-sala.html", sala=obter_sala(id))


@app.route("/cadastrar-sala", methods=['post'])
def pagina_cadastrar_sala_post() -> None:
    criar_sala(request.form['codigo_sala'], request.form['capacidade'], request.form['tipo'], request.form['descricao'])
    
    return redirect(url_for(pagina_principal.__name__))


@app.route("/")
def pagina_principal():
    return render_template("listar-salas.html", salas=obter_salas())


if __name__ == "__main__":
    # Define que a aplicação rodará no modo debug, para que não seja necessário reinicar o servidor toda vez que uma mudança for feita
    app.debug = True
    
    # Para iniciar o servidor, é necessário apenas executar o código, ao invés de rodar a aplicação pela linha de comando
    app.run()
