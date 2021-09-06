from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),
    # path('muro/', views.muro, name = 'muro'),
    path('muro/', views.muro),
    path('muro/<int:val>/', views.comentario),
    path('muro/<int:num>/delete', views.delete),
    path('muro/<int:num>/mensaje/delete', views.mensaje_delete),
    
]
