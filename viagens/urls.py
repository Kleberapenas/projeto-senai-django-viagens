
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foto/<int:foto_id>/', views.detalhe_foto, name='detalhe_foto'),
    path('sobre-nos/',views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),
    path('sucesso/',views.sucesso, name='sucesso'),
]
