from flask import Blueprint, render_template, request, redirect
from models.evento import Evento
from dao.evento_dao import EventoDAO

evento_bp = Blueprint("evento", __name__)

@evento_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        evento = Evento(
            nome=request.form["nome"],
            data=request.form["data"],
            local=request.form["local"],
            vagas=request.form["vagas"],
        )
        EventoDAO.salvar(evento)
        return redirect("/")

    eventos = EventoDAO.listar()
    return render_template("index.html", eventos=eventos)

@evento_bp.route("/editar/<int:id_evento>", methods=["GET", "POST"])
def editar(id_evento):
    evento = EventoDAO.buscar_por_id(id_evento)

    if request.method == "POST":
        evento.nome  = request.form["nome"]
        evento.data  = request.form["data"]
        evento.local = request.form["local"]
        evento.vagas = request.form["vagas"]
        EventoDAO.atualizar()
        return redirect("/")

    return render_template("editar.html", evento=evento)

@evento_bp.route("/excluir/<int:id_evento>")
def excluir(id_evento):
    evento = EventoDAO.buscar_por_id(id_evento)
    if evento:
        EventoDAO.remover(evento)
    return redirect("/")
