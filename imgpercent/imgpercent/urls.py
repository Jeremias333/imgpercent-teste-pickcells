from django.contrib import admin
from django.urls import path
from imgpercent.main.views import index

#Para submissão de imagens
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
]

#para submissão de imagens
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
