fetch("/api/eventos")
    .then(resposta => resposta.json())
    .then(eventos => {
        console.log(eventos);
    });