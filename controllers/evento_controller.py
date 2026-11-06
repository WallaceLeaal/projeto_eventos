
from flask import Blueprint, render_template, request, redirect, jsonify
from models.evento import Evento
from data.evento_dao import EventoDAO

evento_bp = Blueprint("evento", __name__)


# Página inicial e cadastro tradicional
@evento_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        evento = Evento(
            nome=request.form["nome"],
            data=request.form["data"],
            local=request.form.get("local"),
            vagas=request.form.get("vagas") or None
        )

        EventoDAO.salvar(evento)
        return redirect("/")

    eventos = EventoDAO.listar()
    return render_template("index.html", eventos=eventos)


# Editar evento
@evento_bp.route("/editar/<int:id_evento>", methods=["GET", "POST"])
def editar(id_evento):
    evento = EventoDAO.buscar_por_id(id_evento)

    if evento is None:
        return "Evento nao encontrado.", 404

    if request.method == "POST":
        evento.nome = request.form["nome"]
        evento.data = request.form["data"]
        evento.local = request.form.get("local")
        evento.vagas = request.form.get("vagas") or None

        EventoDAO.atualizar()
        return redirect("/")

    return render_template("editar.html", evento=evento)


# Excluir evento
@evento_bp.route("/excluir/<int:id_evento>")
def excluir(id_evento):
    evento = EventoDAO.buscar_por_id(id_evento)

    if evento:
        EventoDAO.remover(evento)

    return redirect("/")


# API GET - Consultar eventos
@evento_bp.route("/api/eventos", methods=["GET"])
def listar_eventos_api():
    eventos = EventoDAO.listar()

    lista = [
        evento.para_dicionario()
        for evento in eventos
    ]

    return jsonify(lista)


# API POST - Cadastrar evento
@evento_bp.route("/api/eventos", methods=["POST"])
def api_cadastrar():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({
            "erro": "Envie um objeto JSON valido."
        }), 400

    if not dados.get("nome") or not dados.get("data"):
        return jsonify({
            "erro": "Nome e data sao obrigatorios."
        }), 400

    try:
        vagas = (
            int(dados["vagas"])
            if dados.get("vagas") not in (None, "")
            else None
        )
    except (ValueError, TypeError):
        return jsonify({
            "erro": "Vagas deve ser um numero inteiro."
        }), 400

    if vagas is not None and vagas < 0:
        return jsonify({
            "erro": "Vagas nao pode ser negativo."
        }), 400

    evento = Evento(
        nome=dados["nome"],
        data=dados["data"],
        local=dados.get("local"),
        vagas=vagas
    )

    EventoDAO.salvar(evento)

    return jsonify(evento.para_dicionario()), 201
