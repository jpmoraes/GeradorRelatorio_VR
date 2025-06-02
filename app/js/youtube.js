 // Solicita permissão para microfone ao carregar a página
  async function solicitarPermissaoAudio() {
    try {
      await navigator.mediaDevices.getUserMedia({ audio: true });
      console.log("Permissão para microfone concedida.");
    } catch (err) {
      console.error("Permissão para microfone negada:", err);
    }
  }

  solicitarPermissaoAudio();

  let player;
  let checou24 = false;
  let intervaloMonitoramento;

  function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
      height: '100%',
      width: '100%',
      videoId: 'b4CdKWKRM_A',
      playerVars: {
        autoplay: 1,
        controls: 1,
        mute: 1,      // Mudo para permitir autoplay automático
        rel: 0
      },
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
  }

  function onPlayerReady(event) {
    event.target.playVideo();
  }

  function onPlayerStateChange(event) {
    if (event.data === YT.PlayerState.PLAYING) {
      console.log("Vídeo começou a tocar. Iniciando monitoramento de tempo...");
      iniciarMonitoramento();
    } else if (event.data === YT.PlayerState.PAUSED || event.data === YT.PlayerState.ENDED) {
      console.log("Vídeo pausado ou terminado. Parando monitoramento.");
      pararMonitoramento();
    }
  }

  function iniciarMonitoramento() {
    if (intervaloMonitoramento) return; // Evita múltiplos intervalos

    intervaloMonitoramento = setInterval(() => {
      if (!player) return;

      const tempoAtual = player.getCurrentTime();
      //console.log("Tempo atual do vídeo:", tempoAtual.toFixed(2));

      // Use uma margem de +-0.5s para evitar perder o momento exato
      if (tempoAtual >= 24 && !checou24) {
        checou24 = true;
        console.log("Chegou em 00:24, enviando requisição...");
        enviarRequisicaoFlask();
        pararMonitoramento(); // Para o monitoramento após enviar
      }
    }, 300);
  }

  function pararMonitoramento() {
    if (intervaloMonitoramento) {
      clearInterval(intervaloMonitoramento);
      intervaloMonitoramento = null;
    }
  }

  function enviarRequisicaoFlask() {
    fetch('/rota-flask', { method: 'POST' })
      .then(response => {
        if (!response.ok) throw new Error('Erro na requisição Flask');
        return response.text();
      })
      .then(data => {
        console.log('Resposta do Flask:', data);
      })
      .catch(err => {
        console.error('Erro ao chamar Flask:', err);
      });
  }