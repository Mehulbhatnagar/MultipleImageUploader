from django.urls import path
from . import views

app_name = 'TASK' 

urlpatterns = [
    path('upload/', views.UploadImageView.as_view(), name='upload_image'),
    path('list/', views.list_images, name='list_images'),
]
