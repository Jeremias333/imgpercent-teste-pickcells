# :camera_flash: imgpercent-teste-pickcells

##### :question: É uma aplicação web feita em Django para testar imagens e dizer se identificou algum cachorro ou gato na imagem submetida dando como resultado a porcentagem de acerto relacionada aquela imagem.

> Faça o teste você mesmo, será que dá :service_dog: ou :cat2: ?

#### Instalação: :floppy_disk:

> Para utilizar precisamos baixar algumas coisas.

- Python 3.8.3: https://www.python.org/downloads/

- Após baixar e instalar o Python 3.8.3 devemos instalar o ambiente virtual projeto utiliza.
  ```terminal
  $ pip install pipenv
  ```
 
 - O Git precisa está instalado na máquina: https://git-scm.com/downloads
	```terminal
	$ git clone linkdesterepositorio
	```
	> Caso queira, pode baixar apenas o zip e extrai-lo.
  
 - Após estar com o projeto clonado, acesse a raíz do projeto com seu terminal/prompt de comando e digite este comando:
    ```
    $ cd imgpercent
    ```
 #### A primeira vez que executar o projeto o pipenv (ambiente virtual) deve instalar as dependencias caso já tenha feito o passo abaixo, pule esse.
 
 - Instalando dependências do projeto:
 
    ```
    $ pipenv install
    ```
- Agora podemos colocar nosso servidor local no ar:

    ```
    $ pipenv run python manage.py runserver
    ```
    
- Assim que aparecer no seu terminal este link: "127.0.0.1:8000/" quer dizer que já pode ser acessado.

- Abra seu navegador e acesse o seguinte link: 127.0.0.1:8000

- Pronto, aproveite o site.

#### Fluxo da aplicação: :hourglass_flowing_sand: 

> Página principal > Reconhecer imagem > Resultado > Sobre > Página principal;

- Página principal

  > Assim que acessar a aplicação será redirecionado para a tela principal que possui uma leve descrição, além de mostrar alguns exemplos na página.

  > Na barra superior existem alguns botões que podem lhe redirecionar para determinadas as determinadas páginas.

- Reconhecer imagem:
  
  > Existe algumas instrunções na página, dizendo as limitações de calculos do nosso site.
  
  > Assim que tiver acesso a esta página haverá um input de arquivo que irá receber uma imagem, assim que a imagem for selecionada o botão para submeter a imagem será habilitado podendo ser clicado.
 
  > Aparecerá uma mensagem e imagem de carregamento, esse processo demora um pouco então aguarde, então será redirecionado para a página de resultado.
  
- Resultado:

  > A página resultado mostra a imagem marcada onde foi identificado o cachorro ou gato (e outros objetos), apresentando também a justificativa caso a imagem não passe no teste.
  
  > Existe um botão que lhe ridireciona para a página de reconhecimento de imagem mais uma vez.
  
  > Daqui pode ser acessado pela barra superior a página sobre.
  
- Sobre:

  > Existe algumas informações sobre o autor e a aplicação.
  

