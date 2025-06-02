const video = document.getElementById('video360');
    let checou24 = false;

    document.body.addEventListener('click', () => {
      if (video.paused) {
        video.play().then(() => {
          console.log("Vídeo iniciado com sucesso.");
        }).catch(err => {
          console.error("Erro ao iniciar vídeo:", err);
        });
      }
    }, { once: true });

    video.addEventListener('timeupdate', () => {
      if (!checou24 && video.currentTime >= 24) {
        checou24 = true;
        console.log("Chegou em 00:24! Enviando requisição para Flask...");

        fetch('/feedbackia', { method: 'GET' })
          .then(res => res.ok ? res.text() : Promise.reject("Erro"))
          .then(texto => console.log("Resposta Flask:", texto))
          .catch(err => console.error("Erro na requisição:", err));
      }
    });