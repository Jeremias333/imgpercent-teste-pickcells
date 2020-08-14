from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

#def index(req):
	#return render(req, "index.html")

def index(req):
    if req.method == 'POST' and req.FILES['myFile']:
        myfile = req.FILES['myFile']

        fs = FileSystemStorage()#objeto para salvar o arquivo

        filename = fs.save(myfile.name, myfile)#salva o arquivo + o nome dele.

        uploaded_file_url = fs.url(filename)

        #volta para mesma página mostrando onde se encontra o arquivo.
        return render(req, 'index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(req, 'index.html')#acessa a página pedida