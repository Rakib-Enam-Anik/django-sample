from django.urls import path
from .views import UploadedImageListCreateView

urlpatterns = [
    path('images/', UploadedImageListCreateView.as_view(), name='images'),
]

