from django.urls import path
from . import views

app_name = 'coloring_book_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_image, name='upload_image'),
    path('settings/', views.adjust_settings, name='adjust_settings'),
    path('convert/', views.convert_image, name='convert_image'),
    path('download/', views.download_pdf, name='download_pdf'),
]