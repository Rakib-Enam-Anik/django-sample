
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("userdata/", include("userdata.urls")),
    #path('', views.Index, name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
