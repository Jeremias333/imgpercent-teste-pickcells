from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import shutil
from django.conf import settings
import os

import numpy as np
import cv2
import time
#criará arquivo com objetos detectados.
from csv import DictWriter

contexto = {
	"obj": "",
	"percent": "",
	"img_path_new": ""
}

def index(req):
	return render(req, "index.html")


        filename = fs.save(myfile.name, myfile)#salva o arquivo + o nome dele.

        uploaded_file_url = fs.url(filename)

        #volta para mesma página mostrando onde se encontra o arquivo.
        return render(req, 'index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(req, 'index.html')#acessa a página pedida