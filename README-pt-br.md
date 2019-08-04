<img height="20px"  src="https://i.imgur.com/1ubgfmC.png"><a href="README-pt-br.md"> – Leia em português!</a><br/>
<img height="20px"  src="https://i.imgur.com/UrpOBOr.png"><a href="README.md"> – Read in English!</a>
------------------------------------------------------------
# Snes Game Manager

SGM é uma aplicação que visa organizar as roms de seu emulador de Super Nintendo de uma forma visual, simples e prática.  
Algumas das funções da aplicação incluem:
* Detectar arquivos de roms e organizá-los em forma de lista ordenada.
* Baixar as capas dos jogos automaticamente, tendo como referencia o nome do jogo.
* Rodar a rom em seu emulador favorito.

## Instalação

### Linux

Se você estiver usando uma distribuição linux baseada em debian, simplesmente baixe a versão .deb nas [releases](https://github.com/allanvobraun/SnesGameManager/releases/download/1.0/sgm_1.0_all.deb) e então execute o arquivo com o seu instalador de pacotes favorito. Isso deve instalar sgm sem dificuldade.

Caso prefira, existe uma versão flatpak disponivel [aqui](https://github.com/allanvobraun/SnesGameManager/releases/download/1.0/sgm_1.0_64x.flatpak) para todas as distribuições linux com suporte a pacotes flatpak.  
Porém a versão flatpak requer internet para se baixar dependencias, sendo comum que a instalação seja lenta.
Antes de começar a instalação, verifique se o flatpak esta instalado em seu computador digitando o seguinte comando em um terminal:

```bash
flatpak --version
```
Se a resposta ao comando **não** mostrar a versão do flatpak, então tenha certeza que o flatpak esta instalado no seu computador.
Prosseguindo digite:

```bash
flatpak install caminho/para/arquivo/sgm_1.0_64x.flatpak
```

Após isso confirme a instalação dos pacotes e digite sua senha root quando necessário.
Após a instalação (é comum demorar) localize o arquivo .desktop que foi criado e então o abra normalmente (também é comum demorar alguns segundos para abrir).
Pronto instalação concluida!

### Windows

Você pode instalar sgm no windows por meio de um instalador simplificado [aqui](https://github.com/allanvobraun/SnesGameManager/releases/download/1.0/sgm_windows_1.0.exe).
Simplesmente execute o instalador e siga dos passos mostrados na tela.


Você também pode baixar a versão .zip de sgm.
Se esse for o caso extraia os arquivos na pasta desejada e execute o arquivo "sgm.exe" para abrir a aplicação.

## Usando
Ao se executar o programa essa será a sua tela principal.  
Clique em "File" e então em "Open roms folder" para se adicionar sua pasta de roms.  

![passo1](https://i.imgur.com/yCnvfU9.png)
  

Uma janela devera abrir como buscador de arquivos do seu sistema operacional, selecione a pasta onde suas roms de super nintendo estão armazenadas.

![passo2](https://i.imgur.com/xTnTeZJ.png)
  

Após isto os arquivos serão carregados e organizados.  
Para se baixar as capas dos jogos aperte em "Functions" e em seguida "Download game covers".  

![passo3](https://i.imgur.com/0lpWDuA.png)
  
O download será iniciado, após seu termino feche a janela.  
Note que algumas vezes o download de uma capa pode falhar. 
Isto provavelmente é devido ao nome do arquivo da ROM. 
Tente modificá-lo para ficar compatível com o nome original do jogo, use letras capitalizadas.  

![passo4](https://i.imgur.com/JTslF16.png)

É nescessário que você tenha algum emulador instalado no seu computador, [Zsnes](https://www.zsnes.com/), [Higan](https://higan.byuu.org/) e [snes9x](http://www.snes9x.com/) são boas escolhas.
Agora é a hora de se configurar o emulador que será usado para rodar os jogos.
Aperte em "Settings" e então selecione "Emulator Configuration". 
Se você estiver usando sgm em alguma distribuição linux, sgm vai preencher os comandos shell dos emuladores: Zsnes, Higan e Snes9x de forma automática.  
Então selecione o emulador desejado ou configure o seu propio na opção "custom". Após finalizar aperte "Apply".

![passo5linux](https://i.imgur.com/BfpDXe7.png)

Se você estiver usando a versão Windows, devera clicar no botão "..." para procurar com o explorador de arquivos o executável de determinado emulador.  
Assim como na versão de Linux você pode selecionar outro emulador com a opção "custom".
Após finalizar selecione o seu emulador padrão e então aperte "Apply".  

![passo5windows](https://i.imgur.com/HcljO94.png)

Para se jogar o jogo, simplesmente o selecione e aperte o botão Play. O seu emulador padrão deve iniciar o jogo.  
Ou clique com o botão direito no jogo para selecionar um emulador especifico.

### Extra

Se desejar mudar a aparência da aplicação os temas Breeze Dark e Breeze Light estão disponiveis na versão linux.
Ja na versão Windows somente o tema Breeze Dark esta funcional por enquanto.

Para se mudar o tema, na janela princial aperte em "Settings" e então selecione "Change theme".
Aqui você pode mudar o tema e ver um pequeno preview, após finalizar clique em "Apply".

![passo6](https://i.imgur.com/vW6LTKr.png)

## Adições futuras
Em futuras versões SGM vai trazer funcionalidades como:

* Sistema de notificações de bugs e avisos.
* Função para se configurar controles e atalhos.
* Suporte a capas de jogos japoneses.
* Função de display em "carrossel"
* Função para se configurar melhor a lista de jogos.

## Estrutura do projeto
O projeto é escrito em python 3.6.8, usando a biblioteca de UI PYQT5.  
A UI foi construída toda se utilizando o QT designer.  
Para se "compilar" o projeto em forma de executável foi utilizado o [pyinstaler](https://www.pyinstaller.org/).
A versão flatpak não faz uso do pyinstaller.  
Para se fazer o download das imagens foi utilizado a biblioteca requests do python.  
Todas as imagens são baixadas desse incrível [repositorio](https://github.com/ZeroSuf3r/nintendo-games-icons).  
O código esta todo adequado para a língua inglesa, apesar de que os comentários estão escritos em pt-br.
 Isto não deve ser um obstaculo muito grande, porém vou procurar traduzir essa parte no futuro.
 

## Contribuindo
Pull requests são bem vindos. Para grandes mudanças, ou bugs, por favor abra uma issue para discução.  
Para contato direto, me envie um e-mail: allanvobraun@gmail.com

## Licença
Software livre.  
[MIT](https://choosealicense.com/licenses/mit/)