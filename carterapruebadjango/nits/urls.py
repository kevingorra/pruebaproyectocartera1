from django.urls import path
from . import views


urlpatterns = [
    # Ejemplo /nits/89088098
<<<<<<< HEAD
    path('', views.Home,name="home"),
    path('vista1/', views.vista1, name="vista1"),
    path('vista2/', views.vista2, name="vista2"),
    path('busqueda/', views.busqueda,name='busqueda'),
=======
    path('', views.Home),
    path('busqueda/', views.busqueda),
>>>>>>> 4f004a043a08597b91294d4c16b79dcb59c45bba
    path("indicadores/", views.tabla_indicadores, name="Tabla Indicadores"),
    # path('buscar/', views.buscar),
]