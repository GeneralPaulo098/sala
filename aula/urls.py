from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('aluno/', views.aluno_list),
    path('aluno/show/<int:id>/', views.aluno_show),
    path('aluno/<int:id>/', views.aluno_delete),
    path('aluno/editar/<int:id>/',views.editar),
    path('aluno/create/', views.create),
]