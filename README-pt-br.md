<img height="20px"  src="https://i.imgur.com/1ubgfmC.png"><a href="README-pt-br.md"> – Leia em português!</a><br/>
<img height="20px"  src="https://i.imgur.com/UrpOBOr.png"><a href="README.md"> – Read in English!</a>
------------------------------------------------------------
# Snes Game Manager

SGM é uma aplicação que visa organizar as roms de seu emulador de Super Nintendo de uma forma visual, simples e pratica.  
Algumas das funções da aplicação incluem:
* Detectar arquivos de roms e organizá-los em forma de lista ordenada.
* Baixar as capas dos jogos automaticamente, tendo como referencia o nome do jogo.
* Rodar a rom em seu emulador favorito.

## Instalação

### Executável
Por enquanto a versão executável do SGM só é compatível com linux.  
Disponível para download [aqui](https://drive.google.com/file/d/1fCHrqvh0bogIbvInQLTkmPVjFTGgjGNI/view?usp=sharing).  
Após descompactar o arquivo. Forneça as permissões necessárias para o executável SGM no diretório principal.
Simplesmente rode o executável.  
Por enquanto SGM só é compatível com o emulador zsnes. Então tenha certeza de baixá-lo com:  

(ubuntu)

```bash
sudo apt install zsnes
```
### Python
Para uma versão mais versátil use o SMG direto pelo python. 
Essa versão ainda não foi testado mais provavelmente funciona em windows e mac.  
Tenha certeza de ter instalado em seu computador o python 3.6 com as bibliotecas "PyQt5" e "requests".  
Descompacte o projeto baixado na pagina do [github](https://github.com/allanvobraun/SnesGameManager).
 Então rode o main.py com:

```bash
python3.6 main.py
```

## Usando
Ao se executar o programa essa será a sua tela principal.  
Clique em "File" e então em "Open roms folder" para se adicionar sua pasta de roms.  

![passo1](https://i.imgur.com/697bgOA.png)
  

Uma janela devera abrir como buscador de arquivos, selecione a pasta desejada e clique em “open”.  

![passo2](https://i.imgur.com/934gK4T.png)
  

Após isto os arquivos serão carregados e organizados.  
Para se baixar as capas dos jogos apreste em "Functions" e em seguida "Download game covers".  

![passo3](https://i.imgur.com/qHYPUxB.png)
  

O download será iniciado, após seu termino feche a caixa de dialogo.  
Note que algumas vezes o download de uma capa pode falhar. 
Isto provavelmente é devido ao nome do arquivo da ROM. 
Tente modificá-lo para ficar compatível com o nome original do jogo em letras capitalizadas.  

![passo4](https://i.imgur.com/ZZfPKQk.png)

  
Para se jogar o jogo, simplesmente o selecione e aperte o botão Play. O seu emulador deve cuidar do resto.

## Adições futuras
Em futuras versões SGM vai trazer funcionalidades como:
* Suporte Windows, Mac OS.
* Suporte a outros emuladores como higan e snes9x.
* Função para se configurar controles e atalhos.
* Suporte a capas de jogos japoneses.
* Função de display em "carrossel"
* Função para se configurar melhor a lista de jogos.

## Estrutura do projeto
O projeto é escrito em python 3.6, usando a biblioteca de UI PYQT5.  
A UI foi construída toda se utilizando o QT designer.  
Para se "compilar" o projeto em forma de executável foi utilizado o [pyinstaler](https://www.pyinstaller.org/).  
Para se fazer o download das imagens foi utilizado a biblioteca requests do python.  
Todas as imagens são baixadas desse incrível [repositorio](https://github.com/ZeroSuf3r/nintendo-games-icons).  
O código esta todo adequado para a língua inglesa, apesar de que os comentários estão escritos em pt-br.
 Isto não deve ser um obstaculo muito grande, porém vou procurar traduzir essa parte no futuro.
 



## Contribuindo
Pull requests são bem vindos. Para grandes mudanças, por favor abra uma issue para discutir a mudança.  
Para contato direto, me envie um e-mail: allanvobraun@gmail.com
## Licença
Software livre.  
[MIT](https://choosealicense.com/licenses/mit/)