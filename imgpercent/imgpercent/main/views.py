from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import shutil
from django.conf import settings
import os

import numpy as np#biblioteca para utilizar matrizes e arrays multidimensionais.
import cv2
#criará arquivo com objetos detectados.
from csv import DictWriter

#Criado dicionário para persistir dados da submissão da imagem.
contexto = {
	"obj": "",
	"percent": "",
	"img_path_new": ""
}

#renderiza a página principal
def index(req):
	return render(req, "index.html")

#renderiza a página de resultados
def result(req):
	#no contexto é passado o dicionário chamado contexto com seus determinados valores.
	return render(req, "result.html", {"img_path_new": contexto["img_path_new"], "obj": contexto["obj"], "percent": contexto["percent"]})

#renderiza a página de reconhecimento
def submit(req):
	#objeto para gerenciar arquivos de imagem
	fs = FileSystemStorage()
	
	""" 
	Verifica se a pasta 'media' existe, caso ela exista é excluída (pois irá possuir
	imagens de submissões anteriores.), caso ela já tenha sido excluída é então
	recriada mais uma vez.
	"""
	if(fs.exists(fs.location)):
		shutil.rmtree(fs.location)
	else:
		os.mkdir(fs.location)
	
	"""
	Irá verificar se foi passado na requisição um arquivo de imagem e se o method HTTP
	passado é do tipo POST
	"""
	if req.method == 'POST' and req.FILES['myFile']:
		myfile = req.FILES['myFile']#Põe a imagem em um objeto.

		"""
		O arquivo é salvo no método abaixo que retorna seu caminho para a variável filename.
		"""
		filename = fs.save(myfile.name, myfile)#retorna o nome do arquivo.extensão.

		uploaded_file_url = fs.url(filename)#retorna o caminho completo do nome de arquivo passado.

		module_dir = os.path.dirname(__file__)#pega o diretório atual do arquivo.
		file_path = os.path.join(module_dir, "yolofiles/yoloDados/")

		#objeto para gerenciar arquivos de imagem
		fs = FileSystemStorage()
		img_path = os.path.join(fs.location, filename)

		image = cv2.imread(img_path)
		
		#variaveis de captura
		h, w = None, None

		#carrega os arquivos com o nome dos objetos que foi treinado para identificar
		with open(f"{file_path}YoloNames.names") as f:
			#cria uma lista com todos os nomes
			labels = [line.strip() for line in f]

		#carrega arquivos treinados pelo framework
		network = cv2.dnn.readNetFromDarknet(f"{file_path}yolov3.cfg", f"{file_path}yolov3.weights")

		#captura ua lista com todos os nomes dos objetos treinados pelo framework
		layers_names_all = network.getLayerNames()

		#obtendo apenas o nome de camadas de saida que precisamos para o algoritmo Yolov3
		#com função de retornar o indice das camadas com saidas desconectadas

		layers_names_output = \
			[layers_names_all[i[0] - 1] for i in network.getUnconnectedOutLayers()]

		# Definir probabilidade minima para eliminar previsões fracas
		probability_minimum = 0.5

		#Definir limite para filtrar caixas delimitadoras fracas
		#com supressão não máxima
		threshold = 0.3

		#Gera cores aleatórias nas caixas de cada objeto detectados.
		#colours = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

		#loop de captura e detecção de objetos
		with open(f"{module_dir}/results.csv", "w") as arquivo:#criando/lendo o arquivo que vai guardar os testes
			cabecalho = ["Objeto", "Porcentagem"]
			escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
			escritor_csv.writeheader()

			while True:
				if w is None or h is None:
					#fatiar apenas dois primeiros elementos da tupla
					h, w = image.shape[:2]

				#A forma resultante possui um numero de quadros, numero de canais, largura e altura
				#E.G.:
				blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)

				#Implementando o passe direto com nosso blob somente atraves das camadas de saída
				#Calculo ao mesmo tempo, tempo necessário para encaminhamento
				network.setInput(blob) #definindo blob como entrada para a rede
				output_from_network = network.forward(layers_names_output)

				#preparando listas para caixas delimitadoras detectadas
				bounding_boxes = []
				confidences = []
				class_numbers = []

				#passando por todas as camadas de saída após o avanço da alimentação
				#fase de detecção dos objetos
				for result in output_from_network:
					for detected_objects in result:
						scores = detected_objects[5:]
						class_current = np.argmax(scores)

						confidence_current = scores[class_current]

						#eliminando previsões fracas com probablilidade minima
						if confidence_current > probability_minimum:
							box_current = detected_objects[0:4] * np.array([w, h, w, h])
							x_center, y_center, box_width, box_height = box_current
							x_min = int(x_center - (box_width / 2))
							y_min = int(y_center - (box_height / 2))

							#Adicionando resultados em listas preparadas
							bounding_boxes.append([x_min, y_min, int(box_width), int(box_height)])
							confidences.append(float(confidence_current))
							class_numbers.append(class_current)

				results = cv2.dnn.NMSBoxes(bounding_boxes, confidences, probability_minimum, threshold)

				#verificando se existe pelo menos um objeto detectado
				if len(results) > 0:
					for i in results.flatten():
						x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
						box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]
						colours_box_current = (0,255,0)
						image_new = cv2.rectangle(image, (x_min, y_min), (x_min + box_width, y_min + box_height), colours_box_current, 2)

						#modificando porcentagem para 2 casas decimais.
						percent = str(confidences[i])
						percent_formatted = int(percent[2:6])
						percent_formatted = str(percent_formatted/100)+"%"

						#Preparando texto com rótulo e acuracia para o objeto detectado.
						text_box_current = "{}: {}".format(labels[int(class_numbers[i])], percent_formatted)

						# Coloca o texto nos objetos detectados
						cv2.putText(image, text_box_current, (x_min, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colours_box_current, 2)

						escritor_csv.writerow( {"Objeto": text_box_current.split(":")[0], "Porcentagem": text_box_current.split(":")[1]})
				
				if(text_box_current.split(":")[0] == "Gato" or text_box_current.split(":")[0] == "Cachorro"):
					contexto["obj"] = text_box_current.split(":")[0]
					contexto["percent"] = text_box_current.split(":")[1]
					contexto["img_path_new"] = "../../media/new"+filename

					#unindo caminho para salvar imagem com retangulo e descrição.
					img_path_new = os.path.join(fs.location, "new"+filename)
					cv2.imwrite(f"{img_path_new}", image_new)#salvando nova imagem.
				else:
					contexto["img_path_new"] = "../../media/"+filename
					contexto["obj"] = "0"
	
				return redirect("../result")
	return render(req, 'submitimg.html')#acessa a página pedida


def about(req):
	return render(req, "about.html")