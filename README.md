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
 - É necessário baixar o arquivo yolov3.weight que pelo fato de ser um pouco grande não pode ser enviado para o Github. Baixe neste link: https://pjreddie.com/media/files/yolov3.weigths.
 
 - O arquivo yolov3.weights deve ser colocado em: ./imgpercent/imgpercent/main/yolofiles/yoloDados/
 
 
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

- Página principal:

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
  
  
#### Funcionalidades: :chart_with_upwards_trend:

> Nosso algoritmo tem a base de dados do YoloV3, que já tem inside todos os calculos para a maioria dos objetos de nosso dia-a-dia por este motivo ele pesa 200mb+, utilizando um algoritmo que fiz, reutilizo as informações dadas pelo Yolo e trato de acordo com minha realidade que é o caso de reconhecer cachorro ou gato em uma foto.

> Deixei algumas responsabilidades no front-end, como um required na tag de imagem para evitar submissão de nenhum arquivo, ou até mesmo só habilitar botão de envio pós imagem ser selecionada.

> Em relação ao calculo do acerto, por padrão o Yolo me sempre trazia a porcentagem de acurácia (acerto) neste formato 0.90890, sendo o máximo de acurácia 1.0000. Primeiramente foi necessário pegar apenas imagens que ultrapassavam 0.5+, pois teremos mais certeza que a imagem em questão é o que esperamos pois seria identificado com mais certeza o objeto esperado. Então pego este número, excluo o primeiro 0 (zero), e divido os restantes dos números por 100, me retornando por exemplo 90,89, passo então esse número para string para acrescentar a porcentagem e então defino ela no retangulo de identificação.

> A respeito das imagens, para evitar uma grande lotação de imagens no servidor toda vez que alguém acessa a página de reconhecimento de imagem o diretório media é verificado, caso exista é excluido para limpar o local e ser usado novamente e caso já exista e esteja limpo já é utilizado passando para a parte de tratamento da imagem supracitado.

> Graças ao Jinja consegui fazer o uso de apresentação de tags de forma seletiva (se isso acontecer apresente esta tag, caso não apresente esta), o que facilitou o desenvolvimento.


#### Bibliotecas, Frameworks e APIs: :file_cabinet:
- Python 3.8.3 - https://docs.python.org/3.8/

-Django - https://docs.djangoproject.com/en/3.0/
-Bootstrap4 - https://getbootstrap.com/docs/4.5/getting-started/introduction/

-OpenCV - https://opencv-python-tutroals.readthedocs.io/en/latest/index.html
-Yolov3 - pjreddie.com/darknet/yolo/
