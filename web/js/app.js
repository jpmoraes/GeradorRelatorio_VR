// JS para envio do form e depois chamada da API que envia e-mail
function enviarAvaliacao() {
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;

    const experiencia_geral = parseInt(document.querySelector('input[name="experiencia_geral"]').value);
    const contribuicao_engajamento = parseInt(document.querySelector('input[name="contribuicao_engajamento"]').value);
    const expectativa_feedback = parseInt(document.querySelector('input[name="expectativa_feedback"]').value);
    const motivacao_aprendizado = parseInt(document.querySelector('input[name="motivacao_aprendizado"]').value);
    const interesse_futuro = parseInt(document.querySelector('input[name="interesse_futuro"]').value);
    const aspectos_mais_gostou = document.getElementById("aspectos").value;

    console.log(experiencia_geral)
    const dados = {
        nome,
        email,
        experiencia_geral,
        contribuicao_engajamento,
        expectativa_feedback,
        motivacao_aprendizado,
        aspectos_mais_gostou,
        interesse_futuro
    };

    fetch("/avaliacao/inserir", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        alert("Avaliação enviada com sucesso!");
        console.log(data);

        // Enviar e-mail com nome e email
        fetch("/avaliacao/enviar-email", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                nome: nome,
                email: email
            })
        })
        .then(response => response.json())
        .then(emailResponse => {
            console.log("E-mail enviado:", emailResponse);
            window.location.reload()
        })
        .catch(error => {
            console.error("Erro ao enviar o e-mail:", error);
        });

    })
    .catch(error => {
        console.error("Erro ao enviar a avaliação:", error);
        alert("Erro ao enviar a avaliação.");
    });
}