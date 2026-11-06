
const lista = document.getElementById("listaEventos");
const formulario = document.getElementById("formEvento");
const botaoAtualizar = document.getElementById("atualizarEventos");
const aviso = document.getElementById("avisoEvento");

// Mostra mensagens na tela
function mostrarAviso(mensagem) {
    aviso.textContent = mensagem;
}

// Acrescenta um evento na lista

function acrescentarNaLista(dados) {
    const item = document.createElement("li");

    const texto = document.createTextNode(
        dados.nome + " — " +
        dados.data + " — " +
        (dados.local || "") + " (" +
        (dados.vagas ?? "") + " vagas) "
    );

    item.appendChild(texto);

    const editar = document.createElement("a");
    editar.href = "/editar/" + dados.id;
    editar.textContent = "editar";

    const excluir = document.createElement("a");
    excluir.href = "/excluir/" + dados.id;
    excluir.textContent = "excluir";

    item.appendChild(editar);
    item.appendChild(document.createTextNode(" "));
    item.appendChild(excluir);

    lista.appendChild(item);
}


// Desenha a lista recebida do servidor
function desenharLista(eventos) {
    lista.innerHTML = "";

    for (let i = 0; i < eventos.length; i++) {
        acrescentarNaLista(eventos[i]);
    }
}

// Consulta os eventos usando GET
function atualizarLista() {
    fetch("/api/eventos")
        .then(function (resposta) {
            if (!resposta.ok) {
                throw new Error("Erro HTTP: " + resposta.status);
            }

            return resposta.json();
        })
        .then(function (eventos) {
            desenharLista(eventos);
            mostrarAviso("Lista atualizada com sucesso.");
        })
        .catch(function () {
            mostrarAviso("Nao foi possivel atualizar a lista.");
        });
}

// Botao Atualizar lista
botaoAtualizar.addEventListener("click", atualizarLista);

// Cadastro usando POST
formulario.addEventListener("submit", function (evento) {
    evento.preventDefault();

    const dados = {
        nome: document.getElementById("nome").value,
        data: document.getElementById("data").value,
        local: document.getElementById("local").value,
        vagas: document.getElementById("vagas").value
    };

    fetch("/api/eventos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    })
        .then(function (resposta) {
            return resposta.json().then(function (corpo) {
                if (!resposta.ok) {
                    mostrarAviso(corpo.erro || "Erro ao cadastrar evento.");
                    return;
                }

                acrescentarNaLista(corpo);
                formulario.reset();
                mostrarAviso("Evento cadastrado sem recarregar a pagina.");
            });
        })
        .catch(function () {
            mostrarAviso("Não foi possivel falar com o servidor.");
        });
});
