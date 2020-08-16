from django.urls import path
import imgpercent.main.views as view

#Para submissão de imagens
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view.index, name="index"),
    path('recognition/', view.submit, name="submit"),
    path('about/', view.about, name="about"),
    path('result/', view.result, name="result"),
]

#para submissão de imagens
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
